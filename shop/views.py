from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth import login as auth_login, authenticate, logout
from django.shortcuts import render, get_object_or_404, redirect,reverse,HttpResponse,HttpResponseRedirect
from django.db.models import Q
from .models import Category,Product, Banner,Offer,Front_Page_Section,Highlights
from cart.forms import CartAddProductForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm, ResetForm
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.views.generic import CreateView
from django import forms
from django.core.mail import EmailMessage
from django.contrib import messages
from django.db.models import Model
from django import template
from django.template.defaultfilters import stringfilter
from orders.models import Review, Order, OrderItem
import random
import stripe

register = template.Library()





def product_list(request, category_slug=None):
    
    section=Front_Page_Section.objects.filter(activate=True)
    offer=Offer.objects.filter(available=True,)
    category=None
    categories=Category.objects.all()
    products=Product.objects.filter(available=True)
    username=request.session.get('username')
    count=1
    
    
    
    if category_slug:
        category=get_object_or_404(Category, slug=category_slug)
        products=Product.objects.filter(Category=category)

        context={
        'category':category,
        # 'categories':categories,
        'products':products,
        'username':username,
        
        }

        return render(request,'shop/product/query.html',context)

    query=request.GET.get("query")
    if query:
        products=Product.objects.filter(
            Q(name__icontains=query) |
            Q(description__icontains=query) |
            Q(specifications__contains=query) |
            Q(Category__name__icontains=query)
            
            ).distinct()

        context={
        'category':category,
        # 'categories':categories,
        'products':products,
        'username':username,
        }

        return render(request,'shop/product/query.html',context)
        
    context={
        'category':category,
        # 'categories':categories,
        'products':products,
        'username':username,
        'offer':offer,
        'section':section,
        'count':count,
    }
    
    return render(request,'shop/product/list.html', context)

# @login_required
def product_detail(request,id,slug):
    specific=""
    product=get_object_or_404(Product, id=id, slug=slug, available=True)
    cat=product.Category
    similar=Product.objects.filter(Category=cat,available=True)
    cart_product_form=CartAddProductForm()
    specification=product.specifications
    highlight=Highlights.objects.filter(product=product)
    reviews=Review.objects.filter(product_id=id)
    orders=Order.objects.all()
    if specification is not None:
        for specific in specification:
            specific = specification.split("\n")
            # name,value=highligh.split("-")
                    
            
        
    context={
        'product':product,
        'cart_product_form': cart_product_form,
        'similar':similar,
        'specification':specific,
        'highlight':highlight,
        'reviews': reviews,
        'orders':orders,
    }
    return render(request,'shop/product/detail.html', context)

def signup(request):
    if request.method == "POST":
        ue=User.objects.all()
        for u in ue:
            if u.email == request.POST['email']:
                print(u.email)
                messages.error(request,"Email address already exists")
                form = SignUpForm()
                return render(request,'registration/signup.html',{'form':form})
                
        form = SignUpForm(data=request.POST)
        if form.is_valid():    
            form.save()
            nu=User.objects.filter(username=request.POST['username'])
            for n in nu:
                n.is_active=False
                n.save()
            reciever=request.POST['email']
            sender=settings.EMAIL_HOST_USER
            for x in range(1):
                rannum=random.randint(10000,99999)
                request.session['otp']=str(rannum)
                request.session['user_id']=request.POST['username']
                send_mail(
                'Activate your Quality account',
                str(rannum),
                sender,
                [reciever],
                fail_silently=False,
                )

            return render(request, 'registration/otp_enter.html')

        # else:
        #     #raise forms.ValidationError("Can't validate")
        #     messages.error(request,"error")

    else:
        form = SignUpForm()
    return render(request,'registration/signup.html',{'form':form})


def login(request):
    if request.method =="POST":
        form=AuthenticationForm(data=request.POST)
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username,password=password)
        if user is not None:
            if user.is_active:
                auth_login(request,user)
                if  request.POST.get('remember_me'):
                    request.session.set_expiry(60*20*24*30)
                return redirect('shop:product_list')
                #return HttpResponse("logged in")
                request.session['username']=username

        else:
            messages.error(request,"Username or Password is wrong, Please try again!")
        
            
        

    else:
        form=AuthenticationForm()
        #return HttpResponse("wrong")
    return render(request, 'registration/login.html',{'form':form})

def logouts(request):
    #if request.method=="POST":
    logout(request)
    return redirect('shop:product_list')


# def test_mail(request):
#     for x in range(1):
#         rannum=random.randint(1000,9999)
#         send_mail(
#         'Subject here',
#         str(rannum),
#         'adityanathtiwari25@gmail.com',
#         ['adityanathtiwari62@gmail.com'],
#         fail_silently=False,
#         )
#     return redirect('shop:product_list')

def otp_test(request):
    if request.method == 'POST':
        if request.POST['otp'] == request.session['otp']:
            nu=User.objects.filter(username=request.session['user_id'])
            for n in nu:
                n.is_active=True
                n.save()
            return redirect('shop:product_list')
        else:
            user_id=request.session['user_id']
            print(user_id)
            idst=str(id)
            User.objects.filter(username=user_id).delete()
        return redirect('shop:product_list')

def otp_render(request):
    return render(request, 'registration/otp_enter.html')


def offer(request,id):
    offer=Offer.objects.filter(id=id)
    for off in offer:
        title=off.title
        products=Product.objects.filter(offer=off)
    return render(request,'shop/product/query.html',{'products':products,'title':title})


def section(request, id):
    section=Front_Page_Section.objects.filter(id=id)
    for sec in section:
        cat=sec.category
        title=sec.title
    products=Product.objects.filter(Category=cat)
    return render(request,'shop/product/query.html',{'products':products,'title':title})
    #return HttpResponse("section")

@login_required
def review(request, pid, slug):
    if request.method == "POST":
        u_id = request.user.id
        u_name = request.user.username
        next = request.POST.get('next')
        print(next)
        product_name = Product.objects.filter(id=pid)
        review=request.POST['review']
        for product in product_name:
            pn=product.name
        r=Review.objects.all()
        r=Review(user_id=u_id,user_name=u_name,product_id=pid,product_name=pn,review=review)
        r.save()
    return HttpResponseRedirect(next)


def reset_p(request):
    return render(request, 'registration/enter_email.html')


def pass_reset_check(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        # return redirect('home')
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('Activation link is invalid!')

def my_orders(request):
    price=0
    length=0
    orderitem=OrderItem.objects.all()
    for ord in orderitem:
        if ord.order is not None:
            if ord.order.user_id == request.user.id:        
                price=price+ord.price
                length=length+1

    return render(request, 'shop/product/my_orders.html',{'orderitem':orderitem,'price':price,'length':length})


def delete_order(request,cid,oid,orid,price):
    refund = stripe.Refund.create(
    charge=cid,
    amount=price,
    )
    uid=request.user.id 
    if OrderItem.objects.filter(user_id=uid).count() == 1:
        Order.objects.filter(id=orid,user_id=uid).delete()
    else:
        OrderItem.objects.filter(id=oid,user_id=uid).delete()
    return redirect('shop:my_orders')


