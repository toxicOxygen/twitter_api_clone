from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

class Post(models.Model):
    user = models.ForeignKey(get_user_model(),on_delete=models.CASCADE,related_name='posts')
    tweet = models.CharField(max_length=280)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    users_like = models.ManyToManyField(get_user_model(),related_name='likes',blank=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return "{} tweeted '{}'".format(self.user,self.tweet)


class PostImage(models.Model):
    post = models.ForeignKey(Post,related_name='images',on_delete=models.CASCADE)
    image = models.ImageField(upload_to='posts/%Y/%m/%d')

    def __str__(self):
        return self.post