from django.contrib import admin
#importing the models for the admin file to load 
from first_app.models import Topic , AccessRecord , Webpage

# Register your models here.

admin.site.register(Topic)
admin.site.register(AccessRecord)
admin.site.register(Webpage)