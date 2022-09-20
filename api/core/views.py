from rest_framework import viewsets
from .serializers import UserSerializer, VideoSerializer
from .models import User, Video


# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
 serializer_class = UserSerializer
 queryset = User.objects.all()

class VideoViewSet(viewsets.ModelViewSet):
 serializer_class = VideoSerializer
 queryset = Video.objects.all()
