from django.http import JsonResponse
from .models import Hostel
from .models import Database
from .models import users
from .models import tempdata
from .serializers import HostelSerializer
from .serializers import DatabaseSerializer
from .serializers import usersSerializer
from .serializers import tempdataSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET', 'POST'])
def hostel_list(request, format=None):

    if request.method == 'GET':
        hostels = Hostel.objects.all()
        serializer = HostelSerializer(hostels, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = HostelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def hostel_detail(request, username, format=None):
    try:
        hostel = Hostel.objects.get(pk=username)
    except Hostel.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = HostelSerializer(hostel)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = HostelSerializer(hostel, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        hostel.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
@api_view(['GET', 'POST'])
def database_list(request, format=None):

    if request.method == 'GET':
        db = Database.objects.all()
        serializer = DatabaseSerializer(db, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = DatabaseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

    
@api_view(['GET', 'PUT', 'DELETE'])
def database_detail(request, id, format=None):
    try:
        db = Database.objects.get(pk=id)
    except Database.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        db = DatabaseSerializer(db)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = DatabaseSerializer(db, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        db.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
@api_view(['GET', 'POST'])
def users_list(request, format=None):

    if request.method == 'GET':
        u = users.objects.all()
        serializer = usersSerializer(u, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = usersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
@api_view(['GET'])
def users_detail(request, roll_no, format=None):
    try:
        u = users.objects.get(pk=roll_no)
    except users.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        u = usersSerializer(u)
        return Response(u.data)
    
@api_view(['GET', 'POST'])
def tempdata_list(request, format=None):

    if request.method == 'GET':
        tdb = tempdata.objects.all()
        serializer = DatabaseSerializer(tdb, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = tempdataSerializer(data=request.data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response('Errrr')
        
@api_view(['GET', 'DELETE'])
def tempdata_detail(request, rollnum_1, format=None):
    try:
        tdb = tempdata.objects.get(pk=rollnum_1)
    except tempdata.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        tdb = tempdataSerializer(tdb)
        return Response(tdb.data)
    
    elif request.method == 'DELETE':
        tdb.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
  
        