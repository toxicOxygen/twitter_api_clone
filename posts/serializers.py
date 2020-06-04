from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Post,PostImage
from comments.api.serializers import CommentSerializer

class PostImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostImage
        fields = ['image',]

class PostSerializer(serializers.ModelSerializer):
    images = PostImageSerializer(many=True,read_only=True)
    comments = CommentSerializer(many=True,read_only=True)

    def create(self,validated_data):
        images_data = self.context['request'].FILES
        print(self.context['request'].user) #todo if it works add it user
        user = get_user_model().objects.filter(id=validated_data.get('userId'))[0]
        post = Post.objects.create(
            # user=self.context['request'].user,
            user = user,
            tweet=validated_data.get('tweet') 
        )
        for im in images_data.getlist('file'):
            PostImage.objects.create(post=post,image=im)
        return post

    class Meta:
        model = Post
        fields = ['id','user','tweet','images','created','comments','users_like']
        