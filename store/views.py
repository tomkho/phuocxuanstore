from .models import Product,Cart,ProductOrder,Profile,Review,ChiTietThanhToan,ThanhToan,About,Contact,Status

from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from store.forms import ProfileForm,ReviewForm

def index(request):
    return render(request,'template.html')

def store(request):
    products=Product.objects.filter(stock__gt=0)
    context={
        'products':products,

    }
    return render(request,'base.html',context)

def about(request):
    about=About.objects.get(active=True)
    context={
        'about':about,
    }
    return render(request,'store/about.html',context)

def contact(request):
    contact=Contact.objects.get(active=True)
    context={
        'contact':contact,
    }
    return render(request,'store/lienhe.html',context)

def product_details(request,product_id):
    product=Product.objects.get(pk=product_id);
    context={
        'product': product,
    }
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = ReviewForm(request.POST)
            if form.is_valid():
                new_review=Review.objects.create(
                    user=request.user,
                    product=context['product'],
                    text=form.cleaned_data.get('text')
                )
                new_review.save()
        else:
            if Review.objects.filter(user=request.user,product=context['product']).count()==0:
                form = ReviewForm()
                context['form']=form
    context['reviews']=product.review_set.all()
    return render(request,'store/chitiet.html',context)

def add_to_cart(request,product_id):
    if request.user.is_authenticated:
        try:
            product=Product.objects.get(pk=product_id)
        except ObjectDoesNotExist:
            pass
        else:
            try:
                cart=Cart.objects.get(user=request.user,active=True)
            except ObjectDoesNotExist:
                cart=Cart.objects.create(user=request.user)
                cart.save()
            cart.add_to_cart(product_id)
        return redirect('cart')
    else:
        return redirect('auth_login')

def remove_from_cart(request,product_id):
    if request.user.is_authenticated:
        try:
            product=Product.objects.get(pk=product_id)
        except ObjectDoesNotExist:
            pass
        else:
            cart=Cart.objects.get(user=request.user,active=True)
            cart.remove_from_cart(product_id)
            return redirect('cart')
    else:
        return redirect('auth_login')

def cart(request):
    if request.user.is_authenticated:
        cart=Cart.objects.filter(user=request.user.id,active=True)
        orders=ProductOrder.objects.filter(cart=cart[0])
        total=0
        count=0
        po=''
        for order in orders:
            total +=(order.product.price * order.quantity)
            count += order.quantity
        context={
            'cart' : orders,
            'total' : total,
            'count' : count,
            'cart_id' :cart[0].id,
        }
        return render(request,'store/giohang.html',context)
    else:
        return redirect('auth_login')


def profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if request.user.is_authenticated:
            if form.is_valid():

                    if Profile.objects.filter(user=request.user.id).count()==0:

                        profile=Profile.objects.create(
                            user=request.user,
                            fullname=form.cleaned_data.get('fullname'),
                            address=form.cleaned_data.get('address'),
                            sdt=form.cleaned_data.get('sdt')
                        )
                        profile.save()
                    else:
                        if Profile.objects.filter(user=request.user.id).count()==1:
                            profiles=Profile.objects.get(user=request.user.id)
                            profiles.fullname=form.cleaned_data.get('fullname')
                            profiles.address=form.cleaned_data.get('address')
                            profiles.sdt=form.cleaned_data.get('sdt')
                            profiles.save()
                    return redirect('thanhtoan')
            else: return render(request,'store/profile.html', {'form': form})
        else:
            return redirect('auth_login')


    if request.user.is_authenticated:
            if Profile.objects.filter(user=request.user.id).count()==1:
                profile=Profile.objects.get(user=request.user.id)
                form = ProfileForm(None, initial={'fullname':profile.fullname, 'address':profile.address,'sdt':profile.sdt})
                return render(request,'store/profile.html', {'form': form})

    return render(request,'store/profile.html', {'form': ProfileForm()})
def thanhtoan(request):
    if request.user.is_authenticated:
        profile=Profile.objects.filter(user=request.user.id)[0]
        cart=Cart.objects.filter(user=request.user.id,active=True)
        orders=ProductOrder.objects.filter(cart=cart[0])
        total=0
        count=0
        for order in orders:
            total +=(order.product.price * order.quantity)
            count += order.quantity

        context={
                'cart' : orders,
                'total' : total,
                'count':count,
                'profile' :Profile.objects.filter(user=request.user.id)[0],
            }
    else:
        return redirect('auth_login')

    return render(request,'store/thanhtoan.html',context)
import string
import random
def code_random(size=10, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def requesttt(request):

    if request.user.is_authenticated:
        tt=save_order(request.user)
        return redirect('https://www.nganluong.vn/button_payment.php?receiver=tiananarissa@gmail&product_name='+str(tt.profile)+'&price='+str(tt.total)+'&return_url=complete_order&comments='+tt.chitiet)

    else:
        return redirect('auth_login')

    return render(request,'store/thanhtoan.html')

def save_order(user):
        profile=Profile.objects.filter(user=user.id)[0]
        cart=Cart.objects.filter(user=user.id,active=True)
        orders=ProductOrder.objects.filter(cart=cart[0])
        total=0
        count=0
        status=Status.objects.get(pk=1)
        po=''
        code=code_random()
        for order in orders:
            total +=(order.product.price * order.quantity)
            count += order.quantity
            po += order.product.name +' ( '+str(order.quantity)+' x '+order.product.loai.type_name+' )***'

        tt=ThanhToan.objects.create(profile=profile,total=total,status=status,chitiet=po,code=code)
        tt.save()
        for order in orders:

            ctdh=ChiTietThanhToan.objects.create(
                            product=order.product,
                            thanhtoan=tt,
                            quantity=order.quantity
                        )
            ctdh.save()
            order.delete()
        return tt
def completeorder(request):
    if request.user.is_authenticated:
        save_order(request.user)
        return render(request,'store/complete_order.html')

    else:
        return redirect('auth_login')
    return render(request,'store/complete_order.html')

def cancel_order(request,thanhtoan_id):
    if request.user.is_authenticated:
        thanhtoan=ThanhToan.objects.get(pk=thanhtoan_id)
        chitiet=ChiTietThanhToan.objects.filter(thanhtoan=thanhtoan)
        for order in chitiet:
            order.delete()
        thanhtoan.status=Status.objects.get(pk=6)
        thanhtoan.save()
        return redirect('history')

    else:
        return redirect('auth_login')
    return render(request,'store/lichsu.html')

def encrypt(key):
    num=(key*1457) + 2018 - 31
    return num

def decrypt(num):
    key=(num + 31-2018)/1457
    return key

def history(request):
    if request.user.is_authenticated:
        profile=Profile.objects.get(user=request.user.id)
        thanhtoan=ThanhToan.objects.filter(profile=profile).order_by('-order_date').exclude(status=6)
        context={'thanhtoan':thanhtoan,'profile': profile}
        return render(request,'store/lichsu.html',context)
    return redirect('auth_login')
