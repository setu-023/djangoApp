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


@api_view(['POST', 'GET'])
#@permission_required('is_check')
def items(request):
    if request.method   ==  'POST':
        if request.user.is_check:
            return (views.store(request))
        else:
            return Response ('HomePage')

    if request.method   ==  'GET':
        if request.user.is_role:
            return (views.index(request))
        else:
            return Response ('HomePage')


# route function for show_details,update
@api_view(['PATCH', 'GET'])
#@permission_required('is_check')
def item(request, pk):

    if request.method   ==  'PATCH':
        if request.user.is_manager:
            return (views.update(request,pk))
        else:
            return Response ('HomePage')

    if request.method   ==  'GET':
        if request.user.is_ceo:
            return (views.show(request,pk))
        else:
            return Response ('HomePage')
