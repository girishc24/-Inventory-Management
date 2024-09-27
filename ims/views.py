from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from django.core.cache import cache
from rest_framework.permissions import IsAuthenticated
from . models import Item
from . serializers import *


def home(request):
    return HttpResponse('Welcome')

@api_view(['POST'])
def adduser(request):
    if request.method == 'POST':
        user_serializer = UserCreateSerializer(data=request.data)
        employee_serializers = EmployeeSerializers(data=request.data)
        

        if user_serializer.is_valid(raise_exception=True) and employee_serializers.is_valid(raise_exception=True):
            user = user_serializer.save()
            employee = employee_serializers.save(user=user)
            response_data = {
                'user': user_serializer.data,
                'profile': employee_serializers.data
            }
            return Response(response_data, status=status.HTTP_201_CREATED)
        
        return Response({'error': user_serializer.errors, 'error': employee_serializers.errors}, status=status.HTTP_400_BAD_REQUEST)
    
    else:
        return Response({'error': 'GET Method not allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


class ItemDetailView(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request):
        data = request.data
        item_name = data.get('name')
        
        if Item.objects.filter(name=item_name).exists():
            return Response({'error': 'Item already exists'}, status=status.HTTP_400_BAD_REQUEST)
        
        serializer = ItemSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request, item_id=None):
        if item_id is None:
            
            cache_key = 'all_items'
            items = cache.get(cache_key)

            if items is None:
                
                items = Item.objects.all()
                cache.set(cache_key, items, timeout=60*15)  # Cache for 15 minutes

            serializer = ItemSerializer(items, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        else:
            
            cache_key = f'item_{item_id}'
            item = cache.get(cache_key)

            if item is None:
                try:
                    item = Item.objects.get(id=item_id)
                    cache.set(cache_key, item, timeout=60*15)  
                except Item.DoesNotExist:
                    return Response({'error': 'Item not found'}, status=status.HTTP_404_NOT_FOUND)

            serializer = ItemSerializer(item)
            return Response(serializer.data, status=status.HTTP_200_OK)

    
    def put(self, request, item_id):
        try:
            item = Item.objects.get(id=item_id)
        except Item.DoesNotExist:
            return Response({'error': 'Item not found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = ItemSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, item_id):
        try:
            item = Item.objects.get(id=item_id)
        except Item.DoesNotExist:
            return Response({'error': 'Item not found'}, status=status.HTTP_404_NOT_FOUND)
        
        item.delete()
        return Response({'message': 'Item deleted successfully'}, status=status.HTTP_204_NO_CONTENT)