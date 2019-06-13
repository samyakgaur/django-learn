from django.shortcuts import render
from django.http import HttpResponse

#connecting it to database 
from first_app.models import Topic , AccessRecord , Webpage

# Create your views here.
# This will display the stuff written here when this is called from the project/url 

#creating a function 
# def index(request):
#     return HttpResponse('Hello World')


#using render function now to learn templates

def index(request):
    #make a variable and fetch objects into it ordered by date field 
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records':webpages_list}
    return render(request,'first_app/index.html',context=date_dict)
    
    # we will not use my_dict as it was for practise 
    # my_dict = {'insert_me':"Hello this is from views.py"}
    # return render(request,'first_app/index.html',context=my_dict)
