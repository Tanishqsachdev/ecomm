from typing import get_origin
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import AddressForm, AddProductForm,SignupForm
from .models import Address,Product,OrderItem,Order
from django.utils import timezone

from django.views.generic import ListView, DetailView,View
from django.contrib.auth.mixins import UserPassesTestMixin
from django.views.generic.base import TemplateView
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit  import CreateView

# Create your views here.
class Home(ListView):
    template_name='main/index.html'
    context_object_name='products'
    model=Product

class UserLogin(LoginView):
    template_name='main/login.html'
    redirect_authenticated_user =True
    
    def get_success_url(self):
        return reverse_lazy('home')

class UserSignUp(UserPassesTestMixin,CreateView):
    template_name='main/signup.html'
    form_class = SignupForm
    success_url = reverse_lazy('home')
    
    def test_func(self):
        if self.request.user.is_authenticated:
            return False
        return reverse_lazy('signup')

class UserLogout(LogoutView):
    next_page='home'

class AddAddress(CreateView):
    template_name='main/add_address.html'
    form_class = AddressForm
    success_url = reverse_lazy('view_address')

class ViewAddress(ListView):
    template_name='main/view_address.html'
    context_object_name='address'
    model=Address

    
    def get_queryset(self):
        queryset = Address.objects.filter(user=self.request.user)
        return queryset

class AddProducts(CreateView):
    template_name='main/add_products.html'
    form_class= AddProductForm
    success_url = reverse_lazy('home')

class ViewDetails(DetailView):
    model= Product
    template_name='main/detail.html'
    context_object_name = 'product'

class AddToCart(View):

    def get(self, *args, **kwargs):
        item = get_object_or_404(Product,pk=self.kwargs['pk'])
        order_item,is_new = OrderItem.objects.get_or_create(item=item,user=self.request.user,ordered=False)

        pending_order = Order.objects.filter(user=self.request.user,ordered=False)
        
        if pending_order.exists():
            order = pending_order[0]

            if order.items.filter(item__pk=self.kwargs['pk']).exists():
                order_item.quantity+=1
                order_item.save()
                # messages.info(self.request,'item added to the cart')
                return redirect('view_cart')
            else:
                order.items.add(order_item)
                # messages.info(self.request,'item added to the cart')
                return redirect('view_cart')
        else:
            order = Order.objects.create(user=self.request.user)
            # messages.info(self.request,'item added to the cart')
            return redirect('view_cart')

class ReduceFromCart(View):
    def get(self,*args,**kwargs):
        item = get_object_or_404(Product,pk=self.kwargs['pk'])
        pending_order = Order.objects.filter(user=self.request.user,ordered=False)

        if pending_order.exists():
            order = pending_order[0]
            item_exist  = order.items.filter(item__pk=self.kwargs['pk'])
            if item_exist.exists():
                order_item = OrderItem.objects.get(item =item,user=self.request.user,ordered=False)
                quant = order_item.quantity
                if quant==1:
                    order_item.delete()
                    return redirect('home')
                elif quant>0:
                    order_item.quantity -=1
                    order_item.save()
                    return redirect('view_cart')
                else:
                    return redirect('home')

class DeleteFromCart(View):
    def get(self,*args,**kwargs):
        item = get_object_or_404(Product,pk=self.kwargs['pk'])
        pending_order = Order.objects.filter(user=self.request.user,ordered=False)

        if pending_order.exists():
            order = pending_order[0]
            item_exist  = order.items.filter(item__pk=self.kwargs['pk'])
            if item_exist.exists():
                order_item = OrderItem.objects.get(item =item,user=self.request.user,ordered=False)
                order_item.delete()
                return redirect('view_cart')
            else:
                return redirect('home')
        else:
            return redirect('home')

class ViewCart(ListView):
    model=OrderItem
    template_name='main/cart.html'
    context_object_name='items'

