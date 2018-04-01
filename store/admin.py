from django.contrib import admin
from .models import Product,Loai,Review,ThanhToan,About,Contact,ChiTietThanhToan,Status
# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display=('name','img','price','stock')
class LoaiAdmin(admin.ModelAdmin):
    list_display=('type_name','added_date')
class ReviewAdmin(admin.ModelAdmin):
    list_display=('product','user','published_date')
class ThanhToanAdmin(admin.ModelAdmin):
    list_display=('id','profile','total','order_date','status')
class ChiTietThanhToanAdmin(admin.ModelAdmin):
    list_display=('product','quantity','id')
class ProfileAdmin(admin.ModelAdmin):
    list_display=('fullname','address')
class CartAdmin(admin.ModelAdmin):
    list_display=('id','order_date')
class ProfileAdmin(admin.ModelAdmin):
    list_display=('fullname','address')
class AboutAdmin(admin.ModelAdmin):
    list_display=('id','text')
class ContactAdmin(admin.ModelAdmin):
    list_display=('id','text')
class StatusAdmin(admin.ModelAdmin):
    list_display=('id','name')
admin.site.register(Product,ProductAdmin)
admin.site.register(Loai,LoaiAdmin)
admin.site.register(Review,ReviewAdmin)
admin.site.register(ThanhToan,ThanhToanAdmin)
admin.site.register(ChiTietThanhToan,ChiTietThanhToanAdmin)
admin.site.register(About,AboutAdmin)
admin.site.register(Contact,ContactAdmin)
admin.site.register(Status,StatusAdmin)
