from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from answer.models import Answer
from answer.serializers import AnswerSerializer
from .models import Question
from .serializers import QuestionSerializer


@api_view(['GET'])
def question_list(request):
    if request.method == 'GET':
        questions = Question.objects.all()
        serializer = QuestionSerializer(questions, many=True)
        return Response(serializer.data)
    return Response({'response': f'No question to display'})


@api_view(['POST'])
def create_question(request):
    if request.method == 'POST':
        if request.user:
            # get the user profile
            p = request.user.profile
            data = request.data
            serializer = QuestionSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                q = p.question_set.create(serializer.data)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def question_detail(request, pk):

    try:
        question = Question.objects.get(pk=pk)
    except Question.DoesNotExist:
        return Response({'error': f'the question with id {pk} doesn\'t exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.user:
        p = request.user.profile

        if request.method == 'GET':
            serializer = QuestionSerializer(request.data)
            if serializer.is_valid():
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)

        if request.method == 'PUT':
            data = request.data
            serializer = QuestionSerializer(question, data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        if request.method == 'DELETE':
            serializer = QuestionSerializer(request.data)
            if serializer.is_valid():
                p.question_set.remove(serializer.data)
                question.delete()
                return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)

    # return Response({'error': f'The user {request.user} doesn\'t exist'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET', 'POST'])
def answer_list_by_question(request, pk):
    # TODO : GET & POST - answers related to a question and answers related to their creator
    if request.user:
        p = request.user.profile
        if request.method == 'GET':
            answers = Answer.objects.filter(question__pk=pk)
            serializer = AnswerSerializer(answers, many=True)
            if serializer.is_valid():
                return Response(serializer.data, status=status.HTTP_200_OK)

        if request.method == 'POST':
            data = request.data
            serializer = AnswerSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                # a = p.answer_set.create(serializer.data)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
