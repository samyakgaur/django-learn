from django.db import models

# Create your models here.
# Models are classes and we write the fields of the table here 

class Topic(models.Model):
    top_name = models.CharField(max_length = 264 ,unique=True)

    # string representation of model 
    # to print out object of topic we make the str rep 
    def __str__(self):
        return self.top_name

class Webpage(models.Model):
    # include the protect method in case if the primary key i.e 
    # top_name gets deleted . for that use on_delete = models.PROTECT 
    topic = models.ForeignKey(Topic , on_delete = models.PROTECT )
    name = models.CharField(max_length = 264 ,unique=True)
    url = models.URLField(unique=True)

    def __str__(self):
        # we return the name of the webpage as its string representation 
        return self.name
        
class AccessRecord(models.Model):
    name = models.ForeignKey(Webpage , on_delete = models.PROTECT)
    date = models.DateField()

    def __str__(self):
        # as date is a date type we cast it into str 
        return str(self.date)