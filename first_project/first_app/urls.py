from django.conf.urls import url
from first_app import views 

urlpatterns = [
    # after newext/
    # as we have set the path to none we dont have to type anything 
    # we will automatically be redirected to index of first_app 
    # but if we had written r'^path' then we would be redirected to index only 
    # when we type 123..../newext/path
    url(r'^$',views.index,name='index'),
]