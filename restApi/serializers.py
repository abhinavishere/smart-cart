from rest_framework import serializers
from .models import Products

class ProductsSerializer(serializers.ModelSerializers):
  class Meta:
    model = Products
    fields = (
      'id',
      'name',
      'price',
      'mfg_dt',
      'prod_img'
    )