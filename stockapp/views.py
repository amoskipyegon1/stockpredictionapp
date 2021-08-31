from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse
from .models import Stockprices, User, Comment
from .forms import TradingForm, reviews
from django.contrib import messages
from django.forms import formset_factory
import tensorflow as tf 
import pandas as pd
import numpy as np

loaded_model = tf.keras.models.load_model('/home/ditto/mysite/saved_model/my_model')
def homeview(request):
    data = Stockprices.objects.all()
    comments = Comment.objects.all()
    context = {'data':data, 'comments':comments}

    return render(request, 'stockapp/home.html',context)

def signinpage(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
            
    context = {'form':form} 
    return render(request, 'stockapp/signin.html',context)

def trade(request):
    #TradingFormset = TradingForm()
    #reviewsFormset = reviews()
    if request.method == 'POST':
        forms = TradingForm(request.POST)
        if forms.is_valid():
            p = {}
            p['first_day'] = request.POST.get('first_day')
            p['second_day'] = request.POST.get('second_day')
            p['third_day'] = request.POST.get('third_day')
            p['first_day']= float(p['first_day'])
            p['second_day']= float(p['second_day'])
            p['third_day']= float(p['third_day'])
            df = pd.DataFrame(p,index=[1])
            df = np.array(df)
            df = df / 373.279999
            #df = df.reshape(1,-1)
            
            df = df.reshape(1,3,1)
            pre = loaded_model.predict(df)
            pre = pre * 373.279999
            pre = float(pre)
            #print(pre)
            messages.info(request,('the next predicted close value is ${}.').format(pre))
        rates = reviews(request.POST)
        if rates.is_valid():
            print(request.POST.dict())
            r = request.POST.dict()
            rates.save()
            messages.success(request, 'Thanks for your comment')
    else:
        forms = TradingForm()
        rates = reviews()
    
    return render(request, 'stockapp/trading.html',{'forms':forms, 'rates':rates})
