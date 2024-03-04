from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from app.models import *
from app.serializers import *
from rest_framework.decorators import APIView

class productcrud(APIView):
    def get(self,request):
        PDO=Product.objects.all()
        PJO=ProductModelSerializer(PDO,many=True)
        return Response(PJO.data)
    
    def post(self,request):
        JDO=request.data
        PDO=ProductModelSerializer(data=JDO)
        if PDO.is_valid():
            PDO.save()
            return Response({'insert':'Data is inserted successfully'})
        else:
            return Response({'Error':'Data is not inserted'})


    
