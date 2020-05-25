from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class CustomUser(AbstractUser):
    photo = models.ImageField(upload_to='users/%Y/%m/%d',blank=True)
    cover_photo = models.ImageField(upload_to='users/covers/%Y/%m/%d',blank=True)
    bio = models.CharField(max_length=160,blank=True)
    website = models.URLField(max_length=100,blank=True)
    location = models.CharField(max_length=30,blank=True)
    date_of_birth = models.DateField(blank=True, null=True)
    following = models.ManyToManyField('self',through='Contact',symmetrical=False,related_name='followers')
    
    def __str__(self):
        return self.username


class Contact(models.Model):
    user_from = models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name='rel_from_set')
    user_to = models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name='rel_to_set')
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return "{} follows {}".format(self.user_from,self.user_to)