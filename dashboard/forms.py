from django import forms
from products.models import *


class Addcat_Form(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'


class Sub_CategoryForm(forms.ModelForm):
    class Meta:
        model = Sub_Category
        fields = '__all__'


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ['name', 'image', 'category', 'sub_category',
                  'product_id', 'description', 'tags', 'brand',
                  'price', 'discount_price', 'featured_post', 'video'
                  ]
