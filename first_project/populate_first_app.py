import os 
# to make this run we need os environ
os.environ.setdefault('DJANGO_SETTINGS_MODULE','first_project.settings')

import django 
django.setup()

# now the fake script 

import random 
# importing models 
from first_app.models import AccessRecord, Webpage , Topic
# importing faker lib 
from faker import Faker

#object for faker 
fakegen = Faker()
# creating topics 
topics = ['Search','Social','Marketplace','News','Games']

# creating functions to populate it 
def add_topic():
    # similar to shell command which either gets the object if exsists or creates it
    # grab the first object of the tuple thats the reason [0] 
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t 

def populate():
    for _ in range(5):
        
        # get the topic for the entry 
        top = add_topic()
        
        #create the fake url    
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()

        # create the new webpage entry 
        webpg= Webpage.objects.get_or_create(topic=top,url=fake_url,name=fake_name)[0]

        # create a fake access record 
        acc_rec = AccessRecord.objects.get_or_create(name=webpg,date=fake_date)[0]

if __name__ == "__main__":
    print("*********************populating script*********************")
    populate()
    print("*********************populating complete*********************")  


     
