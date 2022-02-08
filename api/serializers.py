# -*- coding: utf-8 -*-
#from rest_framework.pagination import PageNumberPagination
#, mixins.ListModelMixin, PageNumberPagination

from shop.models import Item
from rest_framework import serializers, mixins


class PostSerializer(serializers.ModelSerializer):
    class Meta:

        model = Item
        fields = ('brand_name', 'model', 'price', 'category', 'id')
        ordering = ('-publish_date',)
        # paginate_by = 5
        page_size = 10
        # done = serializers.BooleanField(required=False, default=False)
        done = serializers.BooleanField(required=True)