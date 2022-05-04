from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.http import Http404
from rest_framework import mixins, generics
from rest_framework.viewsets import ViewSet

'''Function based views'''

# @api_view(['GET','POST'])
# def course_view(request):
#     if request.method == 'GET':
#         course = Course.objects.all()
#         serializer = CourseSerializer(course, many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = CourseSerializer(data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)
#
# @api_view(['GET','PUT','DELETE'])
# def course_detail_view(request,pk):
#     try:
#         course = Course.objects.get(pk=pk)
#     except:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#     if request.method == 'GET':
#         serilizer = CourseSerializer(course)
#         return Response(serilizer.data)
#     elif request.method == 'PUT':
#         serializer = CourseSerializer(course,data=request.data) #Importantstep
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)
#
#     elif request.method == 'DELETE':
#         course.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


'''class based views'''

# class Course_View(APIView):
#     def get(self, request):
#         course = Course.objects.all()
#         serializer = CourseSerializer(course, many=True)
#         return Response(serializer.data)
#
#     def post(self, request):
#         pass
#         serializer = CourseSerializer(data=request.data, many=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)
#
#
# class Course_Detail_View(APIView):
#     def get_course(self, pk):
#         try:
#             course = Course.objects.get(pk=pk)
#             return course
#         except Course.DoesNotExist:
#             raise Http404
#
#     def get(self, request, pk):
#         serilizer = CourseSerializer(self.get_course(pk))
#         return Response(serilizer.data)
#
#     def put(self, request, pk):
#
#         serializer = CourseSerializer(self.get_course(pk), data=request.data)  # Importantstep
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)
#
#     def delete(self, request, pk):
#         course = self.get_course(pk)
#         course.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


'''Using Mixins'''

#
# class Course_View(mixins.ListModelMixin,mixins.CreateModelMixin, generics.GenericAPIView):
#     queryset = Course.objects.all()
#     serializer_class = CourseSerializer
#
#     def get(self, request):
#         return self.list(request)
#
#     def post(self,request):
#         return self.create(request)
#
# class Course_Detail_View(generics.GenericAPIView,mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin):
#     queryset = Course.objects.all()
#     serializer_class = CourseSerializer
#
#     def get(self,request,pk):
#         return self.retrieve(request,pk)
#
#     def put(self,request,pk):
#         return self.update(request,pk)
#
#     def delete(self,request,pk):
#         return self.destroy(request,pk)


''' Using mixins and generics'''

class Course_View(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class Course_Detail_View(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer




'''Using Viewsets'''


# class CourseViewSet(ViewSet):
#     def list(self,request):
#         course = Course.objects.all()
#         serializer = CourseSerializer(course,many=True)
#         return Response(serializer.data)
#
#     def retrieve(self,request,pk):
#         try:
#             course = Course.objects.get(pk=pk)
#             serializer = CourseSerializer(course)
#             return Response(serializer.data)
#         except Course.DoesNotExist:
#             return Response(status = status.HTTP_404_NOT_FOUND)