from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from posts.serializers import PostSerializer
from posts.models import Post,PostImage
from posts.permissions import IsAuthourOrReadOnly
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView
from actions.utils import create_action

class PostListCreateView(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthourOrReadOnly,]
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class LikePostView(APIView):
    def post(self,request,format=None):
        try:
            id = request.POST['id']
            action = request.POST['action']
            post = Post.objects.get(id=id)
            if action == 'like':
                post.users_like.add(request.user)
                create_action(request.user,'liked',target=post)
            else:
                post.users_like.remove(request.user)
            res_obj = PostSerializer(instance=post)
            return Response(res_obj.data)
        except :
            return Response({'status':'ko'})
        
