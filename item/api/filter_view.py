from item.models import Item
from item.serializers import ItemSerializer
from rest_framework import viewsets
from rest_framework.decorators import action,api_view
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from django_filters  import rest_framework as filters
from rest_framework.filters import SearchFilter, OrderingFilter
from django.views import generic
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.exceptions import APIException
from rest_framework.serializers import ValidationError
from rest_framework import status
from django.http import JsonResponse


class ItemFilter(filters.FilterSet):

    class Meta:
        model = Item
        fields = ['status','name','type','unit_price']


class ItemListView(ListAPIView):

    serializer_class = ItemSerializer




    queryset = Item.objects.all()
    filter_backends = [ DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ['status', 'name', 'type', 'unit_price']

    ordering_fields = ('status', 'unit_price')
    ordering = ('status')
    filter_class = ItemFilter

class ItemList(ListAPIView):


    def __init__(self, status_code=None):
        if status_code is not None:
            self.status_code = status_code


    serializer_class = ItemSerializer
    def get_queryset(self):

        queryset = Item.objects.all()
        status = self.request.query_params.get('status', None)
        type   = self.request.query_params.get('type', None)
        if status is not None:
            queryset = queryset.filter(status=status)
        if type is not None:
            queryset = queryset.filter(type=type)


        if not queryset:
            raise ValidationError()
        else:
            FailList.test_api()
            return queryset


class ValidationSuccess(APIException):

    def check():
        status_code = status.HTTP_200_OK
        default_detail = ({ 'response_code': '200', 'response': status.HTTP_200_OK
, 'message': ' available', })
        default_code = 'invalid'
        return default_detail


class ValidationError(APIException):
    status_code = status.HTTP_404_NOT_FOUND
    default_detail = ({ 'response_code': '404', 'response': status.HTTP_404_NOT_FOUND
, 'message': 'No data is available', })
    default_code = 'invalid'

class FailList():
    def test_api():
        return Response({'response_code': '500', 'response': status.HTTP_500_INTERNAL_SERVER_ERROR, 'message': 'Something went wrong'})




def query_success(a):

    return a
    try:
        return abc
    except:
        return Response('jshjfskh')

    finally:
        return Response('huhuahuaa')
    #return  Response('a')


'''
def retrieve(request, *args, **kwargs):

    status = kwargs.get('Status')
    userExist = Item.objects.filter(status=status)
    if userExist.exists():
        # call the original 'list' to get the original response
        queryset =  Item.objects.filter(status=status)
        lastSourceId = queryset[0]['status']
        response = {"collection": {"data": status,"version":"1.0"}}
        # customize the response data
        if response is not None:
            return Response(response)
    else:
        # return response with this custom representation
        response = {"collection"}
        return response
'''


'''
    status_code  = status.HTTP_400_BAD_REQUEST
    default_code = 'error'
    detail       = ['status_code','default_code']
    def __init__(self, detail, status_code=None):
        self.detail = detail
        if status_code is not None:
            self.status_code = status_code



class CustomFilter(ListAPIView):

    def __init__(self, detail, status_code=None):
        self.detail = detail
        if status_code is not None:
            self.status_code = status_code

    def get_queryset(request):

        status = self.request.query_params.get('status', None)
        type   = self.request.query_params.get('type', None)

        items = Item.objects.filter(status=status, type=type)

        if not items:
            return Response({'response_code': 404})

        return queryset


class FailList():

    def test_api():
        return Response({'response_code': '500', 'response': status.HTTP_500_INTERNAL_SERVER_ERROR
, 'message': 'Something went wrong', 'data': request.data, "errors": error})
'''
