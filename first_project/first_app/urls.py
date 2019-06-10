<<<<<<< HEAD
#this folder is created so that we can call urls from application itself and do not need to 
#write a lot of url statements in the urls.py of django project 
=======
>>>>>>> ef3501c909573d881d25d5aa5cfa40ac1c26645a
from django.conf.urls import url
from first_app import views 

urlpatterns = [
    url(r'^$',views.index,name='index'),
]