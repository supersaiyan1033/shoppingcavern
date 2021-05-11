from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import *
from .models import *
from authentication.models import *
from django.db.models import Avg
import datetime
# Create your views here.


@api_view(['GET'])
def getAllProducts(request):
    query = request.query_params.get('keyword')
    if query == None:
        query = ''
    stocks = Stocks.objects.filter(
        productId__name__icontains=query,
        availableQuantity__gt=0
    )
    serializer = StocksSerializer(stocks, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getProductDetails(request, Id):
    stocks = Stocks.objects.get(stockId=Id)
    serializer = StocksSerializer(stocks, many=False)
    print(serializer.data['productId']['productId'])
    try:
        ratings = Ratings.objects.filter(
            productId=serializer.data['productId']['productId'])
        serial = RatingsSerializer(ratings, many=True)
    except Ratings.DoesNotExist:
        serial = None
    if serial != None:
        data = {"reviews": serial.data}
        data.update(serializer.data)
    else:

        data = serializer.data
    return Response(data)


@api_view(['POST'])
def reviewProduct(request, Id):

    return Response(status=200)


@api_view(['PUT'])
def addToCart(request, Id):

    return Response(status=200)


@api_view(['GET'])
def getCart(request, Id):

    return Response(status=200)


@api_view(['DELETE'])
def deleteCartItem(request, Id):
    cart = Carts.objects.get(stockId=Id)
    cart.delete()
    return Response(status=200)


@api_view(['GET'])
def getOrderById(request, Id):

    return Response(status=200)


@api_view(['GET'])
def myOrders(request, Id):

    return Response(status=200)


@api_view(['POST'])
def placeOrder(request):

    return Response(status=200)


@api_view(['POST'])
def cancelOrder(request):

    return Response(status=200)


def returnOrder(request):

    return Response(status=200)
