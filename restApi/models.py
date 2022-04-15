from django.db import models

# Create your models here.
class Products(models.Model):
  id = models.AutoField(
    primary_key = True
  )

  name = models.TextField(
    max_length=500,
    null=False,
    blank=False
  )

  price = models.IntegerField(
    null=False,
    blank=False
  )

  mfd_dt = models.DateField(
    null= False,
    blank=False
  )

  prod_img = models.ImageField(
    upload_to='products'
  )

  class Meta:
    db_table = 'Products'


