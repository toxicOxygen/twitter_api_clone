from django.urls import path
from .views import PostListCreateView,PostDetailView,LikePostView

urlpatterns = [
    path('',PostListCreateView.as_view()),
    path('<int:pk>/',PostDetailView.as_view()),
    path('like_post/',LikePostView.as_view()),
]