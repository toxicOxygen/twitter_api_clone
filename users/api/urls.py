from django.urls import path
from .views import UsersList,UserDetailView,FollowUserView,CurrentUserView

urlpatterns = [
    path('',UsersList.as_view()),
    path('current_user/',CurrentUserView.as_view()),
    path('<int:pk>/',UserDetailView.as_view()),
    path('follow/',FollowUserView.as_view()),
]