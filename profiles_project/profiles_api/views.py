from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from . import serializers

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
	def list(self,request):
		"""return a hello message """
		a_viewset=[
			'uses action(list,create,retrieve,update,partial_update and destroy',
			'automatically maps the urls using routers',
			'provides more functionality with less code'
		]

		return Response({"message":"hello","a_viewset":a_viewset})