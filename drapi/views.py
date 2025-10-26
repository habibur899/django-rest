from django.shortcuts import render
from .models import Aiquest
from .serializers import AiquestSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status



class AiquestCreate(APIView):
    def get(self, request, pk=None):
        id = pk
        if id is not None:
            # complex data
            ai = Aiquest.objects.get(id=id)
            # python dictionary
            serializer = AiquestSerializer(ai)
            return Response(serializer.data)
        else:
            # complex data
            ai = Aiquest.objects.all()
            # python dictionary
            serializer = AiquestSerializer(ai, many=True)
            return Response(serializer.data)
    # Post Method
    def post(self, request):
        serializer = AiquestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Put Method
    def put(self, request, pk):
        id = pk
        ai = Aiquest.objects.get(pk=id)
        serializer = AiquestSerializer(ai, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Patch Method
    def patch(self, request, pk):
        id = pk
        ai = Aiquest.objects.get(pk=id)
        serializer = AiquestSerializer(ai, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Delete Method
    def delete(self, request, pk):
        id = pk
        ai = Aiquest.objects.get(pk=id)
        ai.delete()
        return Response({'msg': 'Data Deleted'})
