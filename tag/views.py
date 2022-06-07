from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from question.models import Question
from tag.models import Tag
from tag.serializers import TagSerializer


def tag_index(request):
    pass


@api_view(['GET'])
def tag_list(request):
    if request.method == 'GET':
        tags = Tag.objects.all()
        serializer = TagSerializer(tags, many=True)
        if serializer.is_valid():
            return Response(serializer.data)


@api_view(['POST'])
def create_tag(request):
    if request.method == 'POST':
        serializer = TagSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def tag_detail(request, pk):
    try:
        tag = Tag.objects.get(pk=pk)
    except Tag.DoesNotExist:
        return Response({'error': f'The tag with id {pk} doesn\'t exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TagSerializer(request.data)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)

    if request.method == 'PUT':
        serializer = TagSerializer(tag, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        serializer = TagSerializer(request.data)
        if serializer.is_valid():
            tag.delete()
            return Response({'response': f'The tag with id {pk} has been deleted'}, status=status.HTTP_204)


def question_list_by_tag(request, pk):

    if request.method == 'GET':
        questions = Question.objects.filter(tag__pk=pk)
        serializer = TagSerializer(questions, many=True)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == 'POST':
        data = request.data
        serializer = TagSerializer(data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)