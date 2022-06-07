from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from answer.serializers import AnswerSerializer

from answer.models import Answer


# Create your views here.
@api_view(['GET'])
def answer_list(request):
    if request.method == 'GET':
        answers = Answer.objects.all()
        serializer = AnswerSerializer(answers, many=True)
        if serializer.is_valid():
            return Response(serializer.data)
    return Response({'response': f'No answer to display'})


@api_view(['POST'])
def create_answer(request):
    if request.method == 'POST':
        if request.user:
            # get the user profile
            p = request.user.profile
            data = request.data
            serializer = AnswerSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                a = p.answer_set.create(serializer.data)
                return Response(a, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def answer_detail(request, pk):

    try:
        answer = Answer.objects.get(pk=pk)
    except Answer.DoesNotExist:
        return Response({'error': f'The tag with id {pk} doesn\'t exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.user:
        p = request.user.profile

        if request.method == 'GET':
            serializer = AnswerSerializer(request.data)
            if serializer.is_valid():
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)

        if request.method == 'PUT':
            data = request.data
            serializer = AnswerSerializer(answer, data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        if request.method == 'DELETE':
            serializer = AnswerSerializer(request.data)
            a = p.answer_set.remove(serializer.data)
            answer.delete()
            return Response(a, status=status.HTTP_204_NO_CONTENT)
