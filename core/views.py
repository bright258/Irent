#  in built django dependencies
from django.shortcuts import render
from jsonschema import ValidationError

#  rest framework dependencies
from rest_framework.views import APIView
from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    DestroyAPIView,
    RetrieveAPIView,
    UpdateAPIView
)
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated
)
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import (
    MultiPartParser,
    FormParser
)

# serializers
from .serializers import (
    HouseSerializer
)

# models
from .models import (
    House
)

# others

# views

class CreateHouse(CreateAPIView):
    serializer_class = HouseSerializer
    permission_classes = [ 
        AllowAny
    ]
    queryset = House.objects.all()
    

    def post(self, request, *args, **kwargs):
       
        serializer = self.get_serializer(
            data = request.data, context = {'request':request}
        )
       
        serializer.is_valid(raise_exception = True)
        print(serializer.is_valid(raise_exception = True))
        
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)
    

class HouseList(ListAPIView):
    serializer_class = HouseSerializer
    permission_classes = [ 
        AllowAny
    ]
    queryset = House.objects.all()

    def get(self, request, *args, **kwargs):
        houses = House.objects.all()
        serializer = self.serializer_class(houses, many = True)
        return Response(serializer.data) 

   

class RetrieveHouse(RetrieveAPIView):
    serializer_class = HouseSerializer
    permission_classes = [ 
        AllowAny
    ]
    queryset = House.objects.all()

    def get(self, request, pk,*args, **kwargs):
        try:
            house = House.objects.get(pk = pk)
            serializer = self.serializer_class(house)
        except(House.DoesNotExist, ValueError):
            return Response(
                {'details': 'Item does not exist'}, status = status.HTTP_404_NOT_FOUND)
        return Response(serializer.data, status = status.HTTP_200_OK)


class UpdateHouse(UpdateAPIView):
    serializer_class = HouseSerializer
    permission_classes = [ 
        # IsAuthenticated
        AllowAny
    ]
    queryset = House.objects.all()

    def put(self, request, *args, **kwargs):
        
        instance = self.get_object()
        serializer = self.get_serializer(
            instance,
            data = request.data, context = {'request':request} )
        serializer.is_valid(raise_exception = True)
        serializer.save()
       
        return Response(
            {'detail': 'House Details updated successfully'},
            status = status.HTTP_200_OK 

        )

class DeleteHouse(DestroyAPIView):
    serializer_class = HouseSerializer
    permission_classes = [ 
        AllowAny
    ]
    queryset = House.objects.all()

    



    def delete(self, request, pk ,*args, **kwargs):
        
        house = House.objects.filter(pk = pk)
        house.delete()
       

        return Response({'details':'Item successfully deleted'})
    
