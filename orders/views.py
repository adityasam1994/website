from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render, get_object_or_404, redirect,reverse,HttpResponse,HttpResponseRedirect
from .models import OrderItem, Order
from .forms import OrderCreateForm
from cart.cart import Cart
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from address.models import Address
from django.views.decorators.csrf import csrf_exempt
from paypal.standard.forms import PayPalPaymentsForm
from django.conf import settings
from shop.models import Product
from django.views.generic.base import TemplateView
from django.contrib.auth.models import User
from django.template.loader import render_to_string
import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY

 
@login_required
def order_create(request,total=None):
    cart = Cart(request)
    if request.method == 'POST':
        if request.POST.get('deliver_btn') is not None:
            addid=request.POST.get('optradio')
            addresses=Address.objects.filter(id=addid)

            for address in addresses:
                form = OrderCreateForm(request.POST)
                if form.is_valid():
                    form.save()
                    order = form.save()
                    order.user_id=request.user.id
                    order.fullname=address.fullname
                    order.mobile=address.mobile
                    order.town=address.town
                    order.pincode=address.pincode
                    order.state=address.state
                    order.house=address.house
                    order.area=address.area
                    order.landmark=address.landmark
                    order.save()
            tot=0
            for item in cart:
                if item['product'].stock != 0 :
                    OrderItem.objects.create(
                        order=order,
                        product=item['product'],
                        price=item['price'],
                        quantity=item['quantity'],
                        user_id=request.user.id,
                    )
                    tot=tot+item['price']
                    old_stock=Product.objects.filter(id=item['product'].id)
                    quantity=item['quantity']
                    for old in old_stock:
                        new_stock=int(old.stock)-int(quantity)
                        old.stock=new_stock
                        old.save()
            print(tot)
            cart.clear()
            request.session['order_id']=order.id
            request.session['total']=int(tot)*int(100)
            us=User.objects.filter(id=request.user.id)
            for u in us:
                request.session['mail']=u.email
            return redirect('orders:homeview')
           # return render(request, 'orders/order/created.html',{'order':order})
    else:
        
        form = OrderCreateForm()
        addresses=Address.objects.filter(user_id=request.user.id)
        context={
            'form': form,
            'addresses':addresses,
            'total':total
            }        
        return render(request, 'orders/order/create.html',context)


def del_address(request,addid):
    add=Address.objects.filter(id=addid).delete()
    return redirect('orders:order_create')

def addresssubmit(request):
    if request.method == "POST":
        if request.POST['address-submit']:
            user_id=request.user.id
            fullname=request.POST['fullname']
            mobile=request.POST['mobile']
            town=request.POST['town']
            pincode=request.POST['pincode']
            state=request.POST['state']
            house=request.POST['house']
            area=request.POST['area']
            landmark=request.POST['landmark']
            p=Address(user_id=user_id,fullname=fullname,mobile=mobile,pincode=pincode,town=town,state=state,house=house,area=area,landmark=landmark)
            p.save()
        return redirect('orders:order_create')


class HomePageView(TemplateView):
    template_name = 'orders/payment.html'

    def get_context_data(self, **kwargs,):
        context = super().get_context_data(**kwargs)
        context={
            'key': settings.STRIPE_PUBLIC_KEY,
                }
        return context

homeview = HomePageView.as_view()

def charge(request): # new
    if request.method == 'POST':
        total=request.session['total']
        print(total)
        charge = stripe.Charge.create(
            amount=total,
            currency='GBP',
            description='A Django charge',
            source=request.POST['stripeToken']
        )
        order_id=request.session['order_id']
        ord=Order.objects.filter(id=order_id)
        for o in ord:
            o.paid=True
            o.charge_id=charge.id
            o.save()
        subject="Thank's for shopping from Cyfoes Electronics"
        message=render_to_string('order_mail.html',{
            'order_id':order_id,
        })
        from_email=settings.EMAIL_HOST_USER
        to_list=[request.session['mail']]
        send_mail(subject,message,from_email,to_list,fail_silently=False)
        return render(request, 'orders/charge.html')

