from rest_framework import serializers
from item.models import Item


class ItemStatusSerializer(serializers.ModelSerializer):

    def validate_status(self, value):

         if (value) > 0:
             return value
         raise serializers.ValidationError("Enter possitive number.")

    class Meta:
        model   = Item
        fields  = ['status']


class ItemListSerializer(serializers.ListSerializer):

    def create(self, validated_data):
        items = [Item(**item) for item in validated_data]
        return Item.objects.create(items)

#bulk
    # def create(self, validated_data):
    #     return Response('blaaa')
    #     items = [Item(**item) for item in validated_data]
    #     return Item.objects.bulk_create(items)



class ItemSerializer(serializers.ModelSerializer):

    def validate_unit_price(self, value):
         if (value) > 0:
             return value
         raise serializers.ValidationError("Enter positive number.")

    class Meta:
        model  = Item
        fields = ['id','SKU', 'name', 'type','unit_type', 'unit_price', 'status','created_at','updated_at']
        list_serializer_class = ItemListSerializer




#
# class ItemSerializer(serializers.Serializer):
#     ...
#     class Meta:
#         list_serializer_class = ItemListSerializer
