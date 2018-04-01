from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

from django.db.models.signals import post_save
from django.dispatch import receiver
class Loai(models.Model):
    type_name=models.CharField(max_length=50)
    added_date=models.DateField(default=timezone.now)
    def __str__(self):
        return "%s" % (self.type_name)
class Product(models.Model):
    name=models.CharField(max_length=200)
    img=models.ImageField(upload_to='products/',default='products/noimg.png')
    loai=models.ForeignKey(Loai,on_delete=models.DO_NOTHING)
    description=models.TextField()
    added_date=models.DateField(default=timezone.now)
    price=models.DecimalField(decimal_places=0,max_digits=10,default=0)
    stock=models.IntegerField(default=0)
    def __str__(self):
        return "%s" % (self.name)

class Review(models.Model):
    product=models.ForeignKey(Product,on_delete=models.DO_NOTHING)
    user=models.ForeignKey(User,on_delete=models.DO_NOTHING)
    published_date=models.DateField(default=timezone.now)
    text=models.TextField()

class Cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.DO_NOTHING)
    active=models.BooleanField(default=True)
    order_date=models.DateField(default=timezone.now)
    def add_to_cart(self,product_id):
        product=Product.objects.get(pk=product_id)
        try:
            preexisting_order=ProductOrder.objects.get(product=product,cart=self)
            preexisting_order.quantity+=1
            preexisting_order.save()
        except ProductOrder.DoesNotExist:
            new_order=ProductOrder.objects.create(product=product,cart=self,quantity=1)
            new_order.save()


    def remove_from_cart(self,product_id):
        product=Product.objects.get(pk=product_id)
        try:
            preexisting_order=ProductOrder.objects.get(product=product,cart=self)
            if preexisting_order.quantity>1:
                preexisting_order.quantity-=1
                preexisting_order.save()
            else:
                preexisting_order.delete()
        except ProductOrder.DoesNotExist:
            pass
class ProductOrder(models.Model):
    product=models.ForeignKey(Product,on_delete=models.DO_NOTHING)
    cart=models.ForeignKey(Cart,on_delete=models.DO_NOTHING)
    quantity=models.IntegerField(default=1)

class Profile(models.Model):
    fullname=models.CharField(max_length=100)
    address=models.CharField(max_length=500)
    user=models.ForeignKey(User,on_delete=models.DO_NOTHING)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,13}$', message="Số điện thoại không thích hợp.(Chỉ gồm 9-13 ký tự số)")
    sdt = models.CharField(validators=[phone_regex], max_length=13, blank=False)
    added_date=models.DateField(default=timezone.now)
    def __str__(self):
        return "%s - %s - Tel: %s" % (self.fullname,self.address,self.sdt)

class Status(models.Model):
    name=models.CharField(max_length=100)
    def __str__(self):
        return "%s" % (self.name)

class ThanhToan(models.Model):
    profile=models.ForeignKey(Profile,on_delete=models.DO_NOTHING)
    total=models.DecimalField(decimal_places=0,max_digits=15,default=0)
    order_date=models.DateField(default=timezone.now)
    status=models.ForeignKey(Status,on_delete=models.DO_NOTHING,blank=True)
    chitiet=models.TextField(default='')
    code=models.CharField(max_length=100,blank=True)



class ChiTietThanhToan(models.Model):
    product=models.ForeignKey(Product,on_delete=models.DO_NOTHING)
    thanhtoan=models.ForeignKey(ThanhToan,on_delete=models.DO_NOTHING)
    quantity=models.IntegerField(default=1)

class About(models.Model):
    text=models.TextField(default='')
    active=models.BooleanField(default=False)

class Contact(models.Model):
    text=models.TextField(default='')
    active=models.BooleanField(default=False)
