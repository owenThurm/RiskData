from django.shortcuts import render
from rest_framework import views, status
from rest_framework.response import Response
from rest_framework.request import Request
from .utils import parse_price_data

# Create your views here.

class DataAPIView(views.APIView):

    def get(self, req: Request) -> Response:
        # parse bitcoin price data
        parsed_data = parse_price_data()
        return Response(parsed_data, status=status.HTTP_200_OK)
