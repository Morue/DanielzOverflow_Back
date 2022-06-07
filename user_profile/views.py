from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views import generic
from rest_framework.response import Response

from user_profile.models import UserProfile
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets, status
from rest_framework.decorators import api_view, action


# Create your views here.
from .serializers import UserProfileSerializer


@api_view(['GET'])
def current_profile(request):
    if request.user:
        current_user = request.user
        current_profile = current_user.profile
        serializer = UserProfileSerializer(current_profile)
        return HttpResponse(serializer.data)
    return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET', 'POST'])
def profile_list(request):

    if request.method == 'GET':
        profiles = UserProfile.objects.all()
        serializer = UserProfileSerializer(profiles, many=True, context={'request': request})
        data = serializer.data
        return Response(data)

    if request.method == 'POST':
        data = request.data
        serializer = UserProfileSerializer(data=data)

        if serializer.is_valid():
            profile = request.user.profile
            profile.user_set.create(**serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def update_profile(request, pk):

    try:
        prof = UserProfile.objects.get(pk=pk)
        profile = request.user.profile
    except UserProfile.DoesNotExist:
        return Response({'error': f'This profile doesn\'t exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        data = request.data
        serializer = UserProfileSerializer(profile, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # if request.method == 'DELETE':
    #    profile.delete()
    #    return Response({'response': f'The profile with the id {pk} has been deleted'}, status=status.HTTP_204_NO_CONTENT)




