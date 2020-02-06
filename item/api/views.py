from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from django_filters import rest_framework as filters
from rest_framework import generics
import datetime


from django.db.models import Q
from item.serializers import ItemSerializer,ItemStatusSerializer,ItemListSerializer
from item.models import Item


@api_view(['POST'])
def post_post(request):
    error_val = {}
    error_data= {}

    val    = len(request.data)
    count_valid_data   = 0
    count_invalid_data = 0
#     Response(val)

    for info in range(val):

        serializer          =   ItemSerializer(data = request.data[info])

        if serializer.is_valid():
            serializer.save()
            error_val  = serializer.errors
            count_valid_data =  count_valid_data + 1
        else:
            # count_invalid_data    = count_invalid_data + 1
            error_val[info]      = serializer.errors
            error_data[info]     = serializer.data


    result  =  { "success":count_valid_data, "failed": val - count_valid_data }

#return Response(result)
    #return Response({'response_code': '201', 'response': status.HTTP_201_CREATED, 'message': 'Created successfully', 'data': serializer.data})
    #return Response(error_data)
    return Response({'response_code': '200', 'response': status.HTTP_201_CREATED, 'message': 'Successfully','data': result,'errors': error_data})


    # serializer = ItemSerializer(data=request.data, many=isinstance(request.data, list))
    # serializer.is_valid(raise_exception=True)
    # todo_created = []
    # for list_elt in request.data:
    #     todo_obj = Item.objects.create(**list_elt)
    #     item_created.append(item_obj.id)
    #
    # return Response(status=status.HTTP_400_BAD_REQUEST)


# , 'message': 'Something went wrong', 'data': request.data, 'errors': serializer.errors})
    #
    # return Response(serializer.data, status=status.HTTP_201_CREATED)
    # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    #
    #
    #return Response ({'data': serializer.data,'errors': serializer.errors})

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


# @api_view(['POST'])
# def create(request, *args, **kwargs):
#     many = isinstance(request.data, list)
#     serializer = ItemSerializer(data=request.data, many=many)
#     serializer.is_valid(raise_exception=True)
#     self.perform_create(serializer)
#     headers = self.get_success_headers(serializer.data)
#     return Response(serializer.data, headers=headers)


def index():

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
    except Items.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)


    if request.method == 'PATCH':
        serializer = ItemSerializer(get_item, data = request.data, partial = True)

        if serializer.is_valid():
            serializer.save()
            return Response({'response_code': '200', 'response': status.HTTP_200_OK, 'message': 'Updated successfully', 'data': serializer.data})

    return Response({'response_code': '500', 'response': status.HTTP_500_INTERNAL_SERVER_ERROR
    , 'message': 'Something went wrong', 'data': request.data, 'errors': serializer.errors})


@api_view(['PUT'])
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
