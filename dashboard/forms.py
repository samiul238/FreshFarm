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
        fields = ['category', 'sub_category', 'name', 'unit', 'image',
                  'product_id', 'description', 'tags', 'brand',
                  'price', 'discount_price', 'count_in_stock', 'include', 'video'
                  ]
