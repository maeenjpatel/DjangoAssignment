from django.db import models

# Create your models here.
class QueryForm(models.Model):
       sno = models.AutoField(primary_key=True)
       name = models.CharField(max_length=255)
       dept = models.CharField(max_length = 100)
       sem = models.IntegerField()
       email = models.CharField(max_length=100)
       tel = models.CharField(max_length=10)
       desc = models.TextField()

       def __str__(self):
              return self.name