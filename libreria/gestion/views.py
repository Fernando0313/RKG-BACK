from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView

class PruebaController(APIView):
    def get(self, request, format=None):
        return {'message': 'Exito'}

