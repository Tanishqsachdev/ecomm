"""ecom URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views as auth_views
from main.views import *
from django.conf.urls.static import static
from django.conf import settings

admin.site.site_header = "Admin"
admin.site.site_title = "Admin Portal"
admin.site.index_title = "Welcome to Admin Portal"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Home.as_view(),name='home'),
    path('login/', UserLogin.as_view(),name='login'),
    path('signup/', UserSignUp.as_view(),name='signup'),
    path('logout', UserLogout.as_view(),name='logout'),
    path('address/add', AddAddress.as_view(),name='add_address'),
    path('products/add', AddProducts.as_view(),name='add_products'),
    path('address', ViewAddress.as_view(),name='view_address'),
    path('details/<pk>', ViewDetails.as_view(),name='view_details'),
    path('cart', ViewCart.as_view(),name='view_cart'),
    path('cart/add/<pk>', AddToCart.as_view(),name='cart_add'),
    path('cart/red/<pk>', ReduceFromCart.as_view(),name='cart_red'),
    path('cart/del/<pk>', DeleteFromCart.as_view(),name='cart_del'),
    path('checkout/', Checkout.as_view(),name='checkout'),
    path('order/', OrderView.as_view(),name='order'),
    path('order/<pk>', OrderDetails.as_view(),name='order_details'),
    #password_reset
    path('password_reset/',auth_views.PasswordResetView.as_view(template_name="registration/password_reset.html"),name='password_reset'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name="registration/password_reset_confirm.html"),name='password_reset_confirm'),
    path('reset_password/done/',auth_views.PasswordResetDoneView.as_view(template_name="registration/password_reset_done.html"),name='password_reset_done'),
    path('reset/done/',auth_views.PasswordResetCompleteView.as_view(template_name="registration/password_reset_complete.html"),name='password_reset_complete'),
  
]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)