from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.text import slugify
from .choices import cities



class Product(models.Model):
    CONDITION_TYPE =(
        ('New','New'),
        ('Used','Used'),
    )


    def get_image_path(instance,filename):
        name, ext = filename.split('.')
        image_path = 'product_photos/{prod_name}/{photo_name}.{ext}'.format(prod_name=instance.name,photo_name=name,ext=ext)
        return image_path

    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    condition = models.CharField(max_length=100,choices=CONDITION_TYPE)
    price = models.IntegerField()
    city_name = models.CharField(max_length=150,choices=cities,blank=True,null=True)
    owner = models.ForeignKey(User,on_delete=models.CASCADE)
    created = models.DateTimeField(default = timezone.now)
    category = models.ForeignKey('Category',on_delete=models.SET_NULL,null=True)
    brand = models.ForeignKey('Brand',on_delete=models.SET_NULL,null=True)
    photo_main = models.ImageField(upload_to=get_image_path)
    photo_1 = models.ImageField(upload_to=get_image_path,blank=True)
    photo_2 = models.ImageField(upload_to=get_image_path,blank=True)
    photo_3 = models.ImageField(upload_to=get_image_path,blank=True)
    photo_4 = models.ImageField(upload_to=get_image_path,blank=True)
    photo_5 = models.ImageField(upload_to=get_image_path,blank=True)
    photo_6 = models.ImageField(upload_to=get_image_path,blank=True)
    slug = models.SlugField(blank=True,null=True)
    isTrending = models.BooleanField(default=False)

    def save(self,*args,**kwargs):
        self.slug =slugify(self.name)
        super(Product,self).save(*args,**kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'



#########################################################

class Category(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='category_images/',blank=True,null=True)
    slug = models.SlugField(blank=True,null=True)

    def save(self,*args,**kwargs):
        self.slug =slugify(self.name)
        super(Category,self).save(*args,**kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

#########################################################

class Brand(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Brand'
        verbose_name_plural = 'Brands'
