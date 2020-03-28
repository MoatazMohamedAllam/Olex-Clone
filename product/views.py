from django.shortcuts import render
from .models import Product,Category
from django.core.paginator import EmptyPage,PageNotAnInteger,Paginator
from django.db.models import Count
from .choices import cities_choices


def index(request):
    category_list = Category.objects.all()
    trending_products = Product.objects.filter(isTrending=True)

    context = {
        'category_list':category_list,
        'trending_products': trending_products
    }
    return render(request,'product/index.html',context)


def product_list(request,category_slug=None):
    productList = Product.objects.order_by('-created')
    categoryList = Category.objects.annotate(total_products=Count('product'))
    trending_products = Product.objects.filter(isTrending=True)[:3]

    category = None
    if category_slug:
        category = Category.objects.get(slug=category_slug)
        productList = productList.filter(category=category)

    paginator = Paginator(productList,1)
    page = request.GET.get('page')
    paged_products = paginator.get_page(page)

    categories = Category.objects.all()


    context ={
        'product_list':paged_products,
        'category_list':categoryList,
        'categories': categories,
        'category':category,
        'trending_products':trending_products,
        'cities_choices':cities_choices
    }

    return render(request,'product/product_list.html',context)


def product_detail(request,product_slug):
    try:
        product = Product.objects.get(slug=product_slug)
    except Product.DoesNotExist:
        raise Http404('product does not exist')

    return render(request,'product/detail.html',{'product':product})

def search(request):
    queryset_list = Product.objects.order_by('-created')
    categories = Category.objects.all()

    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            queryset_list =queryset_list.filter(city_name__icontains=city)

    if 'category' in request.GET:
        category = request.GET['category']
        if category:
            queryset_list=queryset_list.filter(category__name__icontains=category)

    if 'name' in request.GET:
        name = request.GET['name']
        if name:
            queryset_list=queryset_list.filter(name__icontains=name)

    context={
        'product_list':queryset_list,
        'categories': categories,
        'cities_choices':cities_choices,
        'values':request.GET
    }
    return render(request,'product/product_list.html',context)
