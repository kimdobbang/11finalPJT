from django.shortcuts import render
from django.contrib.auth import get_user_model
from .serializers import UserInfoSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

# permission Decorators
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser

# Create your views here.
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getuser(request ,username):
    usermodel = get_user_model().objects.get(username=username)
    serializer = UserInfoSerializer(usermodel)
    return Response(serializer.data, status=status.HTTP_200_OK)