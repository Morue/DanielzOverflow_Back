from django.shortcuts import render

# Create your views here.
from rest_framework import status, permissions
from rest_framework.decorators import permission_classes, api_view
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from jwtauth.serializers import UserCreateSerializer


@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def registration(request):
    serializer = UserCreateSerializer(data=request.data)
    if not serializer.is_valid():
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    user = serializer.save()
    refresh = RefreshToken.for_user(user)
    # TODO : erase print
    print(refresh.access_token),

    res = {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

    return Response(res, status=status.HTTP_201_CREATED)
