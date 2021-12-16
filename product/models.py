from django.db import models
from django.urls import reverse_lazy


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, primary_key=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category,
                                 on_delete=models.RESTRICT,
                                 related_name='products')
    image = models.ImageField(upload_to='products', null=True, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse_lazy('product-details', args=(self.id,))


# TODO: реализовать возможность хранить несколько изображений
class ProductImage(models.Model):
    product = models.ForeignKey(Product,
                                on_delete=models.CASCADE,
                                related_name='images')
    image = models.ImageField(upload_to='products')

# варианты on_delete
# CASCADE - при удалении категории, удаляются соответсвующие ей продукты
# RESTRICT -
# PROTECT - запрещает удалении категории, если есть связанные с ней продукты
# SET_NULL - при удалении категории, у продуктов категории становится NULL
# SET_DEFAULT - при удалении категории продуктов присваивается дефолтная категория
