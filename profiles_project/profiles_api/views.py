from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class HelloApiView(APIView):
	"""Test api view"""
	def get(self,request,format=None):
		"""returns the list of APIView features"""
		an_apiview=[
			"uses HTTP methods as functions(get,post,patch,put,delete)",
			"it is similar to an traditional django view",
			"gives you the most control over your logic",
			"it mapped manually to urls"
		]
		return Response({"message":"hello","an_apiview":an_apiview})


