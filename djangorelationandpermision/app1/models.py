from django.db import models
from django.contrib.auth.models import User

class User_detail(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    father_name=models.CharField(max_length=100)
    mother_name=models.CharField(max_length=100)
    education=models.CharField(max_length=100)
    age=models.CharField(max_length=100)
    hobby=models.CharField(max_length=1000)

class Post(models.Model):
    user=models.ForeignKey(User,on_delete=models.PROTECT)
    post_text=models.CharField(max_length=500)

class Book(models.Model):
    user=models.ManyToManyField(User)
    book_name=models.CharField(max_length=100)
    writtenby=models.CharField(max_length=100)
    def writers(self):
        return ",".join([str(p) for p in self.user.all()])





    