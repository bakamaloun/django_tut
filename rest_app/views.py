from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_app.serializers import RestSerializer
from rest_app.models import RestElements
from rest_framework import status

# Create your views here.

class restListView(APIView):
    def get(self, request):
        requests = RestElements.objects.all()
        serializer = RestSerializer(requests, many=True)
        return Response(serializer.data)

    def put(self, request):
        serializer = RestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class restDetailView(APIView):
    def get(self, request, pk):
        requests = get_object_or_404(RestElements, pk=pk)
        serializer = RestSerializer(requests)
        return Response(serializer.data)

    def delete(self, request, pk):
        requests = get_object_or_404(RestElements, pk=pk)
        requests.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
