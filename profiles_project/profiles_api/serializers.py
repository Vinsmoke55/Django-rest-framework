from rest_framework import serializers

class HelloSerializer(serializers.Serializer):
	"""serializer a name fiels for testing our APIView"""
	name=serializers.CharField(max_length=10)