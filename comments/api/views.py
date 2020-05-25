from rest_framework.generics import RetrieveUpdateDestroyAPIView,CreateAPIView
from comments.models import Comment
from .serializers import CommentSerializer
from posts.permissions import IsAuthourOrReadOnly

class CommentDetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthourOrReadOnly,]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class CommentCreateView(CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
