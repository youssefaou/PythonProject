from django.shortcuts import render
from django.template import RequestContext

from django.http import HttpResponse
from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
#Create your views here.

from . models import products
from . serializers import productsSerializer

class productList(APIView):
    def get(self,resquest):
        productsl = products.objects.all()
        serializer = productsSerializer(productsl,many=True)

        return Response(serializer.data)

    def post(self):
        pass
