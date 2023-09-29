from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken

from . import serializers
from . import models
from . import permission

# Create your views here.
class HelloApiView(APIView):
	"""Test api view"""

	serializer_class=serializers.HelloSerializer

	def get(self,request,format=None):
		"""returns the list of APIView features"""
		an_apiview=[
			"uses HTTP methods as functions(get,post,patch,put,delete)",
			"it is similar to an traditional django view",
			"gives you the most control over your logic",
			"it mapped manually to urls"
		]
		return Response({"message":"hello","an_apiview":an_apiview})


	def post(self,request):
		"""creates hello message with  our name"""

		serializer =serializers.HelloSerializer(data=request.data)
		if serializer.is_valid():
			name=serializer.data.get('name')
			message="hello {0}".format(name)
			return Response({"message":message})
		else:
			return Response(
				serializer.errors,status=status.HTTP_400_BAD_REQUEST)


	def put(self,request,pk=None):
		"""handles updating the object"""

		return Response({'method':'put'})

	def patch(self,request,pk=None):
		"""patch request only updates fields provided in the request"""

		return Response({'method':'patch'})

	def delete(self,request,pk=None):
		"""deletes and object"""

		return Response({'method':'delete'})


class HelloViewset(viewsets.ViewSet):
	"""test api viewset"""
	serializer_class=serializers.HelloSerializer
	def list(self,request):
		"""return a hello message """
		a_viewset=[
			'uses action(list,create,retrieve,update,partial_update and destroy',
			'automatically maps the urls using routers',
			'provides more functionality with less code'
		]

		return Response({"message":"hello","a_viewset":a_viewset})

	def create(self,request):
		"""creates a new hello message"""
		serializer=serializers.HelloSerializer(data=request.data)
		if serializer.is_valid():
			name=serializer.data.get('name')
			message="hello {0]".format(name)
			return Response({"message":message})
		else:
			return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


	def retrieve(self,request,pk=None):
		"""handles getting an object by its id"""
		return Response({"http_method":"GET"})

	def update(self,request,pk=None):
		"""handles updating an object"""

		return Response({"http_method":"put"})

	def partial_update(self,request,pk=None):
		"""handles updating part of an object"""

		return Response({"http_method":"patch"})

	def destroy(self,request,pk=None):
		"""handles removing an object"""

		return Response({"http_method":"delete"})

class UserProfileViewset(viewsets.ModelViewSet):
	"""handles creating ,treating and uupdating profiles"""
	serializer_class=serializers.UserProfileSerializer
	queryset=models.UserProfile.objects.all()
	authentication_classes=(TokenAuthentication,)
	permission_classes=(permission.UpdateOwnProfile,)
	filter_backends=(filters.SearchFilter,)
	search_fields=('name','email',)

class LoginViewSet(viewsets.ViewSet):
	"""checks emial and pssword nd returns an auth token"""
	serializer_class=AuthTokenSerializer

	def create(self,request):
		"""use the ObtainAuthToken apiview to validate and create a token """
		return ObtainAuthToken().as_view()(request=request._request)