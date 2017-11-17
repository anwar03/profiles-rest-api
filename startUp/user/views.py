from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response

from . import serializers
from . import models

# Create your views here.

class HelloApiView(APIView):
    """Test API View"""

    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Returns a list of APIView feature."""

        an_apiview = [
            'Uses HTTP methods as function (get, post, put, patch, delete).',
            'It is similar to a traditional django view',
            'Gives you the most control over your logic',
            'Is mapped manually to URLs',
        ]

        return Response({'message': 'Hello world', 'an_apiview': an_apiview })


    def post(self, request):
        """Create a hello message with our name."""

        serializer = serializers.HelloSerializer(data=request.data)

        if serializer.is_valid():
            print('bang bang ', serializer.data.get('name'))
            name = serializer.data.get('name')
            message = 'Hello {0}'.format(name)
            return Response({ 'message': message })
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )


    def put(self, request, pk=None):
        """Handles Updating an object."""

        return Response({'message': 'put serializer is work.'})


    def patch(self, request, pk=None):
        """Patch request , only updates fields provides in the request."""

        return Response({'message': 'patch serializer is work.'})


    def delete(self, request, pk=None):
        """Deletes and object."""

        return Response({'message': 'delete serializer is work'})



class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet"""

    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """Return a hello message."""

        a_viewset = [
            'Uses actions (list, create, retrieve, update, partial_update)',
            'Automatically maps to Urls using routers',
            'provides more functionality with less code',
        ]

        return Response({'message': 'Hello', 'a_viewset': a_viewset })

    def create(self, request):
        """Create a new hello message."""

        serializer = serializers.HelloSerializer(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'ViewSet Hello {0}'.format(name)

            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status = status.HTTP_400_BAD_REQUEST
            )


    def retrieve(self, request, pk=None):
        """Handles getting an object by its id."""
        return Response({'http_method': 'GET'})


    def update(self, request, pk=None):
        """update an item its id"""
        return Response({'http_method': 'PUT'})


    def partial_update(self, request, pk=None):
        """Handles updating part of an object its id"""
        return Response({'http_method': 'PATCH'})


    def destroy(self, request, pk=None):
        """Handles removing an object id"""
        return Response({'http_method': 'DELETE'})

class UserProfileViewSet(viewsets.ModelViewSet):
    """Handles creates, creating and updating profile."""

    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
