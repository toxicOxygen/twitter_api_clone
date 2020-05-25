from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
# Create your models here.

class Action(models.Model):
    user = models.ForeignKey(get_user_model(),on_delete=models.CASCADE,related_name='actions',db_index=True)
    verb = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True,db_index=True)
    target_ct = models.ForeignKey(ContentType,blank=True, null=True,related_name='related_obj',on_delete=models.CASCADE)
    target_id = models.PositiveIntegerField(blank=True, null=True,db_index=True)
    target = GenericForeignKey('target_ct','target_id')

    class Meta:
        ordering = ('-created',)
    
    def __str__(self):
        return self.user.usernmae

