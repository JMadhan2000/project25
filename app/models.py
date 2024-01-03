from django.db import models

# Create your models here.
class Topic(models.Model):
    Topic_name=models.CharField(max_length=100,primary_key=True)

    def __str__(self):
        return self.Topic_name
    

    

class WebPage(models.Model):
    topic_name=models.ForeignKey(Topic,on_delete=models.CASCADE)
    name=models.CharField(max_length=100,primary_key=True)
    url=models.URLField()
    email=models.EmailField()

    def __str__(self):
        return self.name