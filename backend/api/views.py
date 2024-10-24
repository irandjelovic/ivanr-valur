from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response

from .serializers import MulSerializer


@api_view(['GET'])
def multiply_numbers(request: Request) -> Response:
    """ API endpoint to calculate product of two numbers """
    serializer = MulSerializer(data=request.query_params)

    if serializer.is_valid():
        multiplicand: float = serializer.validated_data['multiplicand']
        multiplicator: float = serializer.validated_data['multiplicator']
        return Response({'res': multiplicand * multiplicator})

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
