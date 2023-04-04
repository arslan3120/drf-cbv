from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from django.http import Http404
from .models import Course
from .serializers import CourseSerializer

# Create your views here.

class CourseListView(APIView):
    def get(self, request):
        course = Course.objects.all()
        serializer = CourseSerializer(course, many=True)
        return Response(serializer.data)
    
    
    
    def post(self ,request):
        serializer = CourseSerializer(data= request.data)
        if serializer.is_valid():
           serializer.save()
           return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors)
    
    
    
    
class CourseDetailView(APIView):
    def get_course(self, pk):
        try:
            return Course.objects.get(pk=pk)
        except:
            raise Http404
            
    
    def get(self, request, pk):
        courses = self.get_course(pk)
        serializer = CourseSerializer(courses)
        return Response(serializer.data)
    
    
    def put(self, request, pk):
        courses = self.get_course(pk)
        serializer = CourseSerializer(courses, data= request.data)
        if serializer.is_valid():
           serializer.save()
           return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors)
    
    
    def get(self, request, pk):
        self.get_course(pk).delete()
        return Response(status = status.HTTP_204_NO_CONTENT)