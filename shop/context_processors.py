from appearance.models import Social_Media_Link, Header
from shop.models import Product, Banner, Category
from orders.models import Review

def social_processor(request):
    social_links = Social_Media_Link.objects.all()            
    return {'social_links': social_links}

def header_processor(request):
    head=Header.objects.all()
    return {'head': head}

def product_processor(request):
    product=Product.objects.all()
    return {'products':product}

def banner_front_processor(request):
    banner=Banner.objects.filter(set_front=True,on=True)
    return {'banner_front':banner}

def banner_other_processor(request):
    banner=Banner.objects.filter(on=True).exclude(set_front=True)
    return {'banner_other':banner}

def review_processor(request):
    review=Review.objects.all()
    return {'review':review}

def category_processor(request):
    categories=Category.objects.all()
    return {'categories':categories}
