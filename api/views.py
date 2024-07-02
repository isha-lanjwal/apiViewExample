from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student
from .serializaers import StudentSerializer
from rest_framework import status
# used for function view
# from rest_framework.decorators import APIView
from rest_framework.views import APIView

# Create your views here.
# by default if anything not there api_view consider it as GET method
# @api_view()
# def hello_world(request):
#     return Response({'msg': 'Hello World'})

# @api_view(['GET'])
# def hello_world(request):
#     return Response({'msg': 'Hello World'})

# @api_view(['POST','GET'])
# def hello_world(request):
#     if request.method == 'GET':
#         return Response({'msg':'This is GET request'})
#     if request.method == 'POST':
#         return Response({'msg': 'This is POST request','data':request.data})


# @api_view(['GET','POST','PUT','DELETE'])
# def student_api(request):
#     if request.method == 'GET':
#         id = request.data.get('id')
#         if id is not None:
#           stu = Student.objects.get(id=id)
#           serializaer = StudentSerializer(stu)
#           return Response(serializaer.data)
#         stu = Student.objects.all()
#         serializaer = StudentSerializer(stu,many=True)
#         return Response(serializaer.data)

#     if request.method == 'POST':
#        serializaer = StudentSerializer(data=request.data)
#        if serializaer.is_valid():
#           serializaer.save()
#           return Response({'msg': 'Data Created'})
#        return Response(serializaer.errors)

#     if request.method == 'PUT':
#        id = request.data.get('id')
#        stu = Student.objects.get(id=id)
#        serializaer = StudentSerializer(stu,data=request.data,partial = True)
#        if serializaer.is_valid():
#          serializaer.save()
#          return Response({'msg': 'Data Updated'})
#        return Response(serializaer.errors)
       
#     if request.method == 'DELETE':
#        id = request.data.get('id')
#        stu = Student.objects.get(id=id)
#        stu.delete()
#        return Response({'msg': 'Data Deleted'})

# function view
# @api_view(['GET','POST','PUT','PATCH','DELETE'])
# def student_api(request,pk=None):
#     if request.method == 'GET':
#         id = pk
#         if id is not None:
#           stu = Student.objects.get(id=id)
#           serializaer = StudentSerializer(stu)
#           return Response(serializaer.data)
#         stu = Student.objects.all()
#         serializaer = StudentSerializer(stu,many=True)
#         return Response(serializaer.data)

#     if request.method == 'POST':
#        serializaer = StudentSerializer(data=request.data)
#        if serializaer.is_valid():
#           serializaer.save()
#           return Response({'msg': 'Data Created'},status=status.HTTP_201_CREATED)
#        return Response(serializaer.errors,status=status.HTTP_400_BAD_REQUEST)

#     if request.method == 'PUT':
#        id = pk
#        stu = Student.objects.get(pk=id)
#        serializaer = StudentSerializer(stu,data=request.data)
#        if serializaer.is_valid():
#          serializaer.save()
#          return Response({'msg': 'Complete Data Updated'})
#        return Response(serializaer.errors,status=status.HTTP_400_BAD_REQUEST)
       
#     if request.method == 'PATCH':
#        id = pk
#        stu = Student.objects.get(pk=id)
#        serializaer = StudentSerializer(stu,data=request.data,partial=True)
#        if serializaer.is_valid():
#          serializaer.save()
#          return Response({'msg': 'Partial Data Updated'})
#        return Response(serializaer.errors,status=status.HTTP_400_BAD_REQUEST)
    
#     if request.method == 'DELETE':
#        id = pk
#        stu = Student.objects.get(pk=id)
#        stu.delete()
#        return Response({'msg': 'Data Deleted'})

# class view
# pk is a primary key
class StudentApi(APIView):
    def get(self,request,pk=None,format=None):
        id = pk
        if id is not None:
          stu = Student.objects.get(pk=id)
          serializaer = StudentSerializer(stu)
          return Response(serializaer.data)
        stu = Student.objects.all()
        serializaer = StudentSerializer(stu,many=True)
        return Response(serializaer.data)

    def post(self,request,format=None):
        serializaer = StudentSerializer(data=request.data)
        if serializaer.is_valid():
          serializaer.save()
          return Response({'msg': 'Data Created'},status=status.HTTP_201_CREATED)
        return Response(serializaer.errors,status=status.HTTP_400_BAD_REQUEST)


    def put(self,request,pk,format=None):
       id = pk
       stu = Student.objects.get(pk=id)
       serializaer = StudentSerializer(stu,data=request.data)
       if serializaer.is_valid():
         serializaer.save()
         return Response({'msg': 'Complete Data Updated'})
       return Response(serializaer.errors,status=status.HTTP_400_BAD_REQUEST)

    def patch(self,request,pk,format=None):
       id = pk
       stu = Student.objects.get(pk=id)
       serializaer = StudentSerializer(stu,data=request.data,partial=True)
       if serializaer.is_valid():
         serializaer.save()
         return Response({'msg': 'Partial Data Updated'})
       return Response(serializaer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk,format=None):
       id = pk
       stu = Student.objects.get(pk=id)
       stu.delete()
       return Response({'msg': 'Data Deleted'})

       
      
