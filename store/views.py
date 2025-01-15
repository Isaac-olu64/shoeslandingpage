from django.shortcuts import render
from rest_framework import status

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from . models import Category
from . serializers import CategorySerializer

# Create your views here.

class Category(APIView):
    def post(self, request):
        try:
             serializers = CategorySerializer(data=request.data)
             if serializers.is_valid():
                  serializers.save()
                  return Response(serializers.data,status=status.HTTP_201_CREATED)
             return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error":str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)