from django.forms import modelformset_factory
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, ListView, UpdateView, DeleteView
from django.views import View

from django.shortcuts import render, redirect

from .forms import ProductForm, ProductImageForm
from .models import Product, ProductImage


def products_list(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'product/products_list.html', context)

# class ProductListView(View):
#     def get(self, request):
#         products = Product.objects.all()
#         context = {'products': products}
#         return render(request, 'product/products_list.html', context)


class ProductsListView(ListView):
    queryset = Product.objects.all()
    template_name = 'product/products_list.html'
    context_object_name = 'products'


class ProductDetailsView(DetailView):
    queryset = Product.objects.all()
    template_name = 'product/product_details.html'
    context_object_name = 'product'


ImagesFormSet = modelformset_factory(ProductImage, form=ProductImageForm, extra=3, max_num=5, can_delete=True)


class CreateProductView(CreateView):
    queryset = Product.objects.all()
    template_name = 'product/create_product.html'
    form_class = ProductForm
    success_url = reverse_lazy('products-list')

    def post(self, request, *args, **kwargs):
        self.object = None
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save()
            for image in request.FILES.getlist('product_image'):
                ProductImage.objects.create(product=product, image=image)
            return redirect(product.get_absolute_url())
        return self.form_invalid(form)


class UpdateProductView(UpdateView):
    queryset = Product.objects.all()
    form_class = ProductForm
    template_name = 'product/update_product.html'
    context_object_name = 'product'


class DeleteProductView(DeleteView):
    queryset = Product.objects.all()
    template_name = 'product/delete_product.html'
    success_url = reverse_lazy('product-list')



# CRUD(create, retrieve, update, delete)

# MVC(Model-View-Controller)

# Model        (models)
# View         (template)
# Controler    (view)
