from rest_framework.generics import ListAPIView,RetrieveUpdateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from .permissions import IsAllowedToUpdate
from .serializers import UserSerializer
from ..models import Contact
from actions.utils import create_action


class UsersList(ListAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

class UserDetailView(RetrieveUpdateAPIView):
    permission_classes = [IsAllowedToUpdate,]
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


class FollowUserView(APIView):
    
    def post(self,request,format=None):
        id = request.POST['id']
        action = request.POST['action']

        try:
            if id and action:
                user_to = get_user_model().objects.get(id=id)

                if request.user == user_to:
                    return JsonResponse({'status':'ko'})
                elif action == "follow":
                    Contact.objects.get_or_create(user_from=request.user,user_to=user_to)
                    create_action(request.user,'is following ',target=user_to)
                else:
                    Contact.objects.filter(user_from=request.user,user_to=user_to).delete()
                return Response({'status':'ok'})
        except:
            return Response({'status':'ko'})

        return Response({'status':'ko'})

class CurrentUserView(APIView):
    def get(self,request,format=None):
        serializer = UserSerializer(instance=request.user)
        return Response(serializer.data)
        
    def post(self,request,format=None):
        user_detail = UserSerializer(instance=request.user)
        return Response(user_detail.data)

