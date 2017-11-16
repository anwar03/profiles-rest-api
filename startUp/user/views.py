from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response

from . import serializers

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
            print('bang bang ', serializer.data.get('csrfmiddlewaretoken'))
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

    def list(self, request):
        """Return a hello message."""

        a_viewset = [
            'Uses actions (list, create, retrieve, update, partial_update)',
            'Automatically maps to Urls using routers',
            'provides more functionality with less code',
        ]

        return Response({'message': 'Hello', 'a_viewset': a_viewset })
