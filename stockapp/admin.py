from django.contrib import admin
from .models import Profile, Stockprices, User, Comment

# Register your models here.



admin.site.register(Profile)
admin.site.register(Stockprices)
admin.site.register(User)
admin.site.register(Comment)