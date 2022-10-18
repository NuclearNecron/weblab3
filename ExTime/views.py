from django.shortcuts import render
from rest_framework import viewsets

from ExTime.serialisers  import *
from ExTime.models import *


class GameViewSet(viewsets.ModelViewSet):
    queryset = Games.objects.all().order_by('pk')
    serializer_class = GameSerializer
# Create your views here.

class DevViewSet(viewsets.ModelViewSet):
    queryset = Developer.objects.all().order_by('pk')
    serializer_class = DevSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('pk')
    serializer_class = UserSerializer

class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all().order_by('pk')
    serializer_class = ServiceSerializer

class ReviewsViewSet(viewsets.ModelViewSet):
    queryset = Reviews.objects.all().order_by('pk')
    serializer_class = ReviewSerializer

class RScreenViewSet(viewsets.ModelViewSet):
    queryset = Reviewscreenshot.objects.all().order_by('pk')
    serializer_class = RScreenSerializer

class SScreenViewSet(viewsets.ModelViewSet):
    queryset = Servicescreenshot.objects.all().order_by('pk')
    serializer_class = SScreenSerializer

class STypeViewSet(viewsets.ModelViewSet):
    queryset = Servicetype.objects.all().order_by('pk')
    serializer_class = STypeSerializer