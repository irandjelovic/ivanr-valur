from rest_framework import serializers


class MulSerializer(serializers.Serializer):
    """ Serializer for multiplication of two numbers """
    multiplicand = serializers.FloatField()
    multiplicator = serializers.FloatField()
