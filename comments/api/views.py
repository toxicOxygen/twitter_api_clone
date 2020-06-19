from rest_framework.generics import RetrieveUpdateDestroyAPIView,CreateAPIView,ListAPIView
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


class CommentListView(ListAPIView):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
