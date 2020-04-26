from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
# from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.request import Request
from django.shortcuts import get_object_or_404
from api.serializers import CategorySerailizer,ProductSerializer,FeedbackSerializer,CartSerializer,UserSerializer
from rest_framework import generics
from rest_framework import viewsets
from rest_framework import mixins
from rest_framework.exceptions import APIException
# from django.http.response import HttpResponse, JsonResponse
# from django.http.request import HttpRequest
from api.models import*
# Create your views here.
@api_view(['GET','POST'])
def products_list(request):
    if request.method == 'GET':
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = request.data
        serializer = ProductSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({'error': wrong})
@api_view(['GET','PUT','DELETE'])
def product_detail(request, product_id):
    product = get_object_or_404(Product,id=product_id)
    if request.method == 'GET':
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ProductSerializer(instance=product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({'errors':serializer.errors})
    elif request.method == 'DELETE':
        product.delete()
        return Response({'deleted':True})
    
class CategoryAPIView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerailizer

class CategoryDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerailizer
    lookup_url_kwarg = 'category_id'

def products_by_category(request,fk):
    try:
        category = Category.objects.get(id = fk)
    except Category.DoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False)
    products = category.product_set.all()
    response = [product.to_json() for product in products]
    return JsonResponse(response, safe=False)

# class CartViewSet(viewsets.ModelViewSet):
#     queryset = Cart.objects.all()
#     serializer_class = CartSerializer

class FeedbackAPIView(generics.CreateAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer

@api_view(['GET', 'POST', 'DELETE'])
# @permission_classes([IsAuthenticated])
def cart_list(request, pk=None):
    if request.method == 'GET':
        cart_list = Cart.objects.all()
        serializer = CartSerializer(cart_list, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = CartSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    if request.method == 'DELETE':
        if pk is None:
            return Response('error no pk matched')
        cart_item=Cart.objects.get(id=pk)
        cart_item.delete()
        return Response('DELETED')


@api_view(['GET', 'POST'])
def category_product(request, pk):
    if request.method == 'GET':
        products = Product.objects.filter(category_id=pk)
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error, status=status.HTTP_500_INTERNAL_SERVER_ERROR)