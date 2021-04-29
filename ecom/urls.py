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
from django.urls import path
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
    path('admin/products/add', AddProducts.as_view(),name='add_products'),
    path('address', ViewAddress.as_view(),name='view_address'),
    
]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)