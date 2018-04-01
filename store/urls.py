
from django.urls import path
from store import views,tests

from django.contrib.auth import views as auth_views
urlpatterns = [
    path('', views.store, name='index'),
    path('product/<int:product_id>', views.product_details, name='product_details'),
    path('add/<int:product_id>', views.add_to_cart, name='add_to_cart'),
    path('remove/<int:product_id>', views.remove_from_cart, name='remove_from_cart'),
    path('cart', views.cart, name='cart'),
    path('profile/', views.profile, name='profile'),
    path('thanhtoan/', views.thanhtoan, name='thanhtoan'),
    path('about/', views.about, name='about'),
    path('lienhe/', views.contact, name='contact'),
    path('lichsu/', views.history, name='history'),
    path('requesttt/', views.requesttt, name='requesttt'),
    path('complete_order/', views.completeorder, name='complete_order'),
    path('change-password/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('cancel/<int:thanhtoan_id>', views.cancel_order, name='cancel_order'),
    ]
