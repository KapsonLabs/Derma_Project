from rest_framework import generics
from django.http import QueryDict
import datetime

from django.http import Http404
from rest_framework.views import APIView

from rest_framework.response import Response
from rest_framework import serializers
from .serializers import PredictSerializer
from rest_framework import status


class PredictData(APIView):

    def post(self, request):
        predict_data = PredictSerializer(data=request.data)
        if predict_data.is_valid():
            print(predict_data)
            return Response(status=status.HTTP_201_CREATED)
        return Response(predict_data.errors, status=status.HTTP_400_BAD_REQUEST)
