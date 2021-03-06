from django.db import models
from posts.models import Post
from django.contrib.auth import get_user_model

# Create your models here.
# class CommentReply(models.Model):
#     user = models.ForeignKey(get_user_model(),related_name='comment_replies',on_delete=models.CASCADE)
#     comment = models.CharField(max_length=140)

class Comment(models.Model):
    user = models.ForeignKey(get_user_model(),on_delete=models.CASCADE,related_name='comments')
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
    comment = models.CharField(max_length=140)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(get_user_model(),related_name='comment_likes',blank=True)

    def __str__(self):
        return self.comment