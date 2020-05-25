from django.shortcuts import get_object_or_404
from rest_framework import serializers
from comments.models import Comment
from posts.models import Post



class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id','comment','user','post','created']
    
    def create(self,validated_data):
        post_id = validated_data.get('post')
        comment = Comment.objects.create(
            user=self.context['request'].user,
            comment=validated_data.get('comment'),
            post=post_id #TODO if this fails check here
        )
        return comment