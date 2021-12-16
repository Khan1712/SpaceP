from django import forms

from product.models import Category, Product, ProductImage


class ProductForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__()
    name = forms.CharField(max_length=50)
    description = forms.CharField()
    price = forms.DecimalField(max_digits=10, decimal_places=2)
    category = forms.ModelChoiceField(queryset=Category.objects.all())

    def save(self):
        data = self.cleanned_data
        product = Product.objects.create(**data)
        return product


class ProductForm(forms.ModelForm):
    # TODO: загрузка изображений
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'category']

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price <= 0:
            raise forms.ValidationError('Цена должна быть положительной')
        return price


class ProductImageForm(forms.ModelForm):
    class Meta:
        model = ProductImage
        fields = ['image']




