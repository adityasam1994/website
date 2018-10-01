from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from shop.models import Product
from .cart import Cart
from .forms import CartAddProductForm
from shop.models import Category
from shop.views import login
from django.contrib import messages
from .models import Cart_Record
 
 
@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        user_id=request.user.id
        tt=Cart_Record.objects.filter(user_id=user_id,product_id=product_id)
        if tt:
            for t in tt:
                t.quantity = form.cleaned_data['quantity']
                t.save()

        else:    
            c=Cart_Record(user_id=user_id,product_id=product_id,quantity=form.cleaned_data['quantity'])
            c.save()

        cd = form.cleaned_data
        cart.add(product=product, quantity=cd['quantity'], update_quantity=cd['update'])
    return redirect('cart:cart_detail')
 
 
def cart_remove(request, product_id):
    user_id=request.user.id
    Cart_Record.objects.filter(user_id=user_id,product_id=product_id).delete()
    c=Cart_Record(user_id=user_id,product_id=product_id)
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')
 
 
def cart_detail(request):
    categories=Category.objects.all()
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(initial={'quantity': item['quantity'], 'update': True})
    return render(request, 'cart/myorders.html', {'cart': cart,'categories':categories})

def please_login(request):
    messages.error(request,"Please login before checkout!")
    return redirect('cart:cart_detail')
    
def total(request,total):
    return redirect('orders:order_create', total=total)

def please_login_cart(request):
    messages.error(request,"Please login before add item to cart!")
    return redirect('shop:login')