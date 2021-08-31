from django import forms
from .models import Comment, Stockprices
from django.forms import ModelForm

class TradingForm(forms.Form):
	first_day = forms.FloatField(label='firstday')
	second_day = forms.FloatField(label='secondday')
	third_day = forms.FloatField(label='thirdday')
	'''widgets = {'first_day':attrs{'class':form-control,'id':autoSizingInput,'placeholder':firstday},
	           'second_day':attrs{'class':form-control,'id':autoSizingInput,'placeholder':secondday},
	           'third_day':attrs{'class':form-control,'id':autoSizingInput,'placeholder':thirdday}
              }'''
class reviews(ModelForm):
	class Meta:
		model = Comment
		fields = '__all__'