import base64
import sys
import hashlib
from rest_framework.decorators import api_view
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from django.db import connection
import bcrypt
from django.http import JsonResponse, HttpResponse, HttpResponseNotFound, Http404
from .models import Admins, Buyers, Sellers, ShippingAddresses
from .serializers import *
from shopping.models import *
from shopping.serializers import *
import base64
from django.contrib.auth.hashers import *
# Create your views here.


@api_view(['POST'])
def login(request):

    return Response({'message': "Register First!!"}, status=500)


@api_view(['POST'])
def register(request):

    return Response({'message': "seller under verification"}, status=500)


@api_view(['GET'])
def getUserDetails(request, Id, role):

    return Response()


@api_view(['POST'])
def updateProfile(request):

    return Response()


# Admin related apis


@api_view(['GET'])
def verifiedSellers(request):

    return Response()


@api_view(['GET'])
def unverifiedSellers(request):

    return Response()


@api_view(['GET'])
def verifySeller(request, sid):

    return Response()


@api_view(['GET'])
def removeSeller(request, sid):

    return Response()


@api_view(['GET'])
def adminsList(request):

    return Response()


@api_view(['GET'])
def removeAdmin(request, aid):

    return Response()


@api_view(['POST'])
def addAdmin(request):

    return Response()


@api_view(['GET'])
def deliverProducts(request):

    return Response()


@api_view(['GET'])
def deliverParticularProduct(request, oid):

    return Response()


@api_view(['GET'])
def returnProducts(request):

    return Response()


@api_view(['GET'])
def returnParticularProduct(request, oid):

    return Response()


@api_view(['GET'])
def addOldStocks(request, sid):

    return Response()


@api_view(['GET'])
def addOldParticularStock(request, sid, skid, quantity):

    return Response()


@api_view(['POST'])
def addNewParticularStock(request, sid):

    return Response([])
# Admin related apis
