"""first_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
#for using url method use django.conf.urls
from django.conf.urls import url
from django.conf.urls import include
#import the view from the app you created 
from first_app import views
from second_app import views as view1

urlpatterns = [
    #add the follwing view url to type in so that it redirects there 'views/'
    
    #url(r'^$/',views.index,name='index'),
    path('views/',views.index,name='index'),

    
    path('view2/',view1.index),

    #using include function and connecting it to 
    url(r'^newext/',include('first_app.urls')),

    #url(r'^admin/',admin.site.urls),
    path('admin/', admin.site.urls),
]
