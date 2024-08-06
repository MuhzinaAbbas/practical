from django.shortcuts import render
from rest_framework.response import Response
from rest_framework. decorators import api_view

from reactapp.models import customers
from reactapp.serializers import CustomerSerializer
from rest_framework import status

# Create your views here.
@api_view(['POST'])
def register(request):
    if request.method=='POST':
        serializer=CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'saved successfully','data':serializer.data})
@api_view(['GET'])
def display(request):
    if request.method=='GET':
        data=customers.objects.all()
        serializer=CustomerSerializer(data,many=True,context={'request':request})
        return Response(serializer.data)
@api_view(['DELETE'])
def delete(request,id):
    try:
        instance=customers.objects.get(id=id)
    except customers.DoseNotExist:
        return Response({"error":"Not found"},status=status.HTTP_404_NOT_FOUND)
    if request.method=='DELETE':
        instance.delete()
        return Response({"data":"delete"})
@api_view(['PUT'])
def update(request,id):
    try:
        instance=customers.objects.get(id=id)
    except customers.DoesNotExist:
        return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method=='PUT':
        serializer = CustomerSerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    

