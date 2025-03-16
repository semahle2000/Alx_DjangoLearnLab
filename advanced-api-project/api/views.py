from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class TestView(APIView):
    def get(self, request):
        return Response({"message": "Django REST Framework is working!"}, status=status.HTTP_200_OK)
