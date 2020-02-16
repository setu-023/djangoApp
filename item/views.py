from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth.decorators import permission_required

from django_filters import rest_framework as filters
from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter

from item.serializers import ItemSerializer
from item.models import Item
from  item.api import views




@api_view(['GET', 'POST'])
@permission_required('is_check')
def items(request):

    if request.method   ==  'POST':
        return (views.store(request))

    if request.method   ==  'GET':
        return (views.index())


# route function for show_details,update
@api_view(['PATCH', 'GET'])
def item(request, pk):

    if request.method   ==  'PATCH':
        return (views.update(request,pk))


    if request.method   ==  'GET':
        return (views.show(request,pk))
