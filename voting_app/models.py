from django.db import models

# Create your models here.
class Voters(models.Model):
    first_name=models.CharField(max_length=10)
    last_name=models.CharField(max_length=10,null=True,blank=True)
    email=models.EmailField()
    vote=models.CharField(max_length=60)
    timestamp=models.DateTimeField(auto_now_add=True,auto_now=False)
    updated=models.DateTimeField(auto_now_add=False,auto_now=True)
    
    def __unicode__(self):
        return self.first_name+" "+self.last_name+" ("+self.email+") "
    
class Question(models.Model):
    title=models.CharField(max_length=20)
    question=models.CharField(max_length=300)
    option1=models.CharField(max_length=60)
    option2=models.CharField(max_length=60)
    option3=models.CharField(max_length=60)
    option4=models.CharField(max_length=60)
    
    def __unicode__(self):
        return self.title
    
class Question_Setter(models.Model):
    email=models.EmailField()
    timestamp=models.DateTimeField(auto_now_add=True,auto_now=False)
    updated=models.DateTimeField(auto_now_add=False,auto_now=True)
    
    def __unicode__(self):
        return self.email