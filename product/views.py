from django.shortcuts import render,redirect
from .models import Product,Category,Brand
from django.core.paginator import EmptyPage,PageNotAnInteger,Paginator
from django.db.models import Count
from .choices import cities_choices
from django.contrib import messages,auth
from django.contrib.auth.decorators import login_required



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


    if 'name' in request.GET:
        name = request.GET['name']
        if name:
            queryset_list=queryset_list.filter(name__icontains=name)

    context={
        'product_list':queryset_list,
        'cities_choices':cities_choices,
        'values':request.GET
    }
    return render(request,'product/product_list.html',context)



@login_required
def add_advertise(request):
    if request.method == 'POST':
        name = request.POST['name']
        category = request.POST['category']
        description = request.POST['description']
        brand = request.POST.get('brand','')
        price = request.POST['price']
        city_name = request.POST['city_name']
        photo_main = request.FILES['photo_main']
        photo_1 = request.FILES.get('photo_1','')
        photo_2 = request.FILES.get('photo_2','')
        photo_3 = request.FILES.get('photo_3','')
        photo_4 = request.FILES.get('photo_4','')
        photo_5 = request.FILES.get('photo_5','')
        photo_6 = request.FILES.get('photo_5','')

        cat = Category.objects.get(name=category)
        if brand:
            brand = Brand.objects.get(name=brand)
        else:
            brand = None
        

        product = Product(name=name,
                            description=description,
                            category=cat,
                            owner=request.user,
                            brand=brand,
                            price=price,
                            city_name=city_name,
                            photo_main=photo_main,
                            photo_1=photo_1,
                            photo_2=photo_2,
                            photo_3=photo_3,
                            photo_4=photo_4,
                            photo_5=photo_5,
                            )
        print(product)
        product.save()
        messages.success(request,'you have been post your advertise successfully!')

        return redirect('products:product_list')
        
       






    categories = Category.objects.all()


    context={
        'categories':categories,
        'cities_choices':cities_choices,
    }
    return render(request,'product/post-ad.html',context)