# serializers.py
from rest_framework import serializers

from .models import NikeCrawl


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = NikeCrawl
        fields = ('id',
                  'title',
                  'subtitle',
                  'status',
                  'stylecode',
                  'colorcode',
                  'stylecolor',
                  'colordescription',
                  'genders',
                  'sporttags',
                  'quantitylimit',
                  'styletype',
                  'producttype',
                  'country',
                  'currency',
                  'currentprice',
                  'available',
                  'imageurls')
