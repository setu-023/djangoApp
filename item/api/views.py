from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from django_filters import rest_framework as filters
from rest_framework import generics
import datetime
from django.contrib.auth.decorators import permission_required



#from django.db.models import Q
from item.serializers import ItemSerializer,ItemStatusSerializer,ItemListSerializer
from item.models import Item


@api_view(['POST'])
def post_post(request):
    error_val = {}
    error_data= {}
    result_data={}

#checking request length
    request_len    = len(request.data)
    count_valid_data   = 0

    for info in range(request_len):

        serializer          =   ItemSerializer(data = request.data[info])

        if serializer.is_valid():
            serializer.save()
            count_valid_data =  count_valid_data + 1
        else:
            result_data[info+1]           = {"errors":serializer.errors,"data":serializer.data}


    result  =  { "success":count_valid_data, "failed": request_len - count_valid_data }
    return Response({'response_code': '200', 'response': status.HTTP_201_CREATED, 'message': 'Successfully','data': [result,result_data] })

#@permission_required('is_role')
def store(request):

    serializer          =   ItemSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'response_code': '201', 'response': status.HTTP_201_CREATED, 'message': 'Created successfully', 'data': serializer.data})

    return Response({'response_code': '500', 'response': status.HTTP_500_INTERNAL_SERVER_ERROR
, 'message': 'Something went wrong', 'data': request.data, 'errors': serializer.errors})


@api_view(['POST'])
def bulk_insert(request):

    serializer          =   ItemSerializer(data = request.data, many=True)

    if serializer.is_valid():
        serializer.save()
        return Response({'response_code': '201', 'response': status.HTTP_201_CREATED, 'message': 'Created successfully', 'data': serializer.data})

    return Response({'response_code': '500', 'response': status.HTTP_500_INTERNAL_SERVER_ERROR
, 'message': 'Something went wrong', 'data': request.data, 'errors': serializer.errors})


#@permission_required('is_check')
def index(request):

    try:
        get_all_items   =   Item.objects.all()
        serializer      =   ItemSerializer(get_all_items, many = True)

        return Response({'response_code': '200', 'response': status.HTTP_200_OK, 'message': 'Ok', 'data': serializer.data})

    except:
        return Response({'response_code': '500', 'response': status.HTTP_500_INTERNAL_SERVER_ERROR
, 'message': 'Something went wrong'})



def show(request,pk):

    try:
        get_item_detail =    Item.objects.get(pk = pk)

    except Item.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)

    if request.method   ==  'GET':
        serializer      =    ItemSerializer(get_item_detail)
        return Response({'response_code': '200', 'response': status.HTTP_200_OK, 'message': 'Ok', 'data': serializer.data})

    return Response({'response_code': '500', 'response': status.HTTP_500_INTERNAL_SERVER_ERROR
, 'message': 'Something went wrong', 'data': request.data})


def update(request,pk):

    try:
        get_item        =   Item.objects.get(pk = pk)
    except Item.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)


    if request.method == 'PATCH':
        serializer = ItemSerializer(get_item, data = request.data, partial = True)

        if serializer.is_valid():
            serializer.save()
            return Response({'response_code': '200', 'response': status.HTTP_200_OK, 'message': 'Updated successfully', 'data': serializer.data})

    return Response({'response_code': '500', 'response': status.HTTP_500_INTERNAL_SERVER_ERROR
    , 'message': 'Something went wrong', 'data': request.data, 'errors': serializer.errors})


#@api_view(['PUT'])
def item_delete(request, pk):

    if request.method   ==   'PUT':
        get_item_detail =     Item.objects.get(pk = pk)
        get_item_detail.status = 0
        get_item_detail.save()
        #return Response(get_item_detail.status)
        return Response({'response_code': '200', 'response': status.HTTP_200_OK, 'message': 'Deleted successful'})

    else:
        return Response({'response_code': '500', 'response': status.HTTP_500_INTERNAL_SERVER_ERROR
, 'message': 'Something went wrong', 'data': request.data, "errors": error})


@api_view(['PATCH'])
def status_update(request,pk):

    try:
        get_item       =   Item.objects.get(pk=pk)
    except Item.DoesNotExist:
        return Response({'response': status.HTTP_404_NOT_FOUND, 'message': 'Something went wrong'})


    if request.method == 'PATCH':
        serializer = ItemStatusSerializer(get_item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'response_code': '200', 'response': status.HTTP_200_OK, 'message': 'Status changed successfully', 'data': serializer.data})

    return Response({'response_code': '500', 'response': status.HTTP_500_INTERNAL_SERVER_ERROR
    , 'message': 'Something went wrong', 'data': request.data, 'errors': serializer.errors})


@api_view(['POST'])
def get_query_by_date(request):

    start_date        =  request.data.get('start_date', None)
    end_date          =  request.data.get('end_date', None)

    if (start_date) is not None:
        if (end_date) is not None:
            samples = Item.objects.filter(created_at__gte=start_date, created_at__lte=end_date)
        else:
            samples = Item.objects.filter(created_at__gte=start_date)
    else:
        if (end_date) is not None:
            samples = Item.objects.filter(created_at__lte=end_date)
        else:
            samples = Item.objects.filter()

    if request.method == 'POST':
        try:
            serializer = ItemSerializer(samples, many = True, partial = True)
            #return Response('Found')
            if serializer.data:
                #return Response('Found')
                return Response({'response_code': '200', 'response': status.HTTP_200_OK, 'message': 'Ok', 'data': serializer.data})

            else:
                #return Response('Not Found')
                return Response({'response_code': '500', 'response': status.HTTP_500_INTERNAL_SERVER_ERROR, 'message': 'No data found'})

        except:
            return Response({'response_code': '500', 'response': status.HTTP_500_INTERNAL_SERVER_ERROR, 'message': 'Something went wrong', 'data': request.data})


@api_view(['POST'])
def query_status_update(request):

    item_status       =  request.data.get('status', None)
    item_type         =  request.data.get('type', None)

    get_item =  Item.objects.all()
#check
    try:

        if item_status is not None:
            get_item    =   get_item.filter(status=item_status)
        if item_type is not None:
            get_item    =   get_item.filter(type=item_type)


    except Item.DoesNotExist:
        return Response({'response': status.HTTP_404_NOT_FOUND, 'message': 'Something went wrong'})

    if request.method == 'POST':
        try:
            serializer = ItemSerializer(get_item, many = True, partial = True)
            quer       = serializer
            if  serializer.data:
                #return Response('Found')
                return Response({'response_code': '200', 'response': status.HTTP_200_OK, 'message': 'Ok', 'data': serializer.data})

            else:
                #return Response('Not Found')
                return Response({'response_code': '500', 'response': status.HTTP_500_INTERNAL_SERVER_ERROR, 'message': 'No data found'})

        except:
            return Response({'response_code': '500', 'response': status.HTTP_500_INTERNAL_SERVER_ERROR, 'message': 'Something went wrong', 'data': request.data})


@api_view(['POST'])
def search_item(request):

    name        =   request.data.get('name',None)
    get_item    =   Item.objects.all()

    try:
        if name is not None:
            get_item    =   get_item.filter(name__icontains=name)

    except Item.DoesNotExist:
        return Response({'response': status.HTTP_404_NOT_FOUND, 'message': 'Something went wrong'})

    try:
        serializer = ItemSerializer(get_item, many = True, partial = True)
        if  serializer.data:
            return Response({'response_code': '200', 'response': status.HTTP_200_OK, 'message': 'Ok', 'data': serializer.data})
        else:
            return Response({'response_code': '500', 'response': status.HTTP_500_INTERNAL_SERVER_ERROR, 'message': 'No data found'})
    except:
        return Response({'response_code': '500', 'response': status.HTTP_500_INTERNAL_SERVER_ERROR, 'message': 'Something went wrong', 'data': request.data})
