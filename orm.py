# SELECT

# SELECT * FROM products;
# Product.objects.all()

# SELECT * FROM products WHERE ...;
# Product.objects.filter(...)

# SELECT * FROM product WHERE price = 10000;
# Product.objects.filter(price=10000)

# SELECT * FROM products WHERE price != 10000;
# Product.objects.filter(~Q(price=10000))
# Product.objects.exclude(price=10000)

# SELECT * FROM products WHERE price > 10000;
# Product.objects.filter(price__gt)

# SELECT * FROM products WHERE price < 10000;
# Product.objects.filter(price__lte=10000)

# SELECT * FROM products WHERE price < 10000;
# Product.objects.filter(price__gte=10000)

# SELECT * FROM products WHERE category_id IN ('phones', 'tv');
# Product.objects.filter(category_id__in=['phones', 'tv'])


# SELECT * FROM products WHERE price BETWEEN 2000 AND 5000
# Product.objects.filter(price__range=[2000, 5000])


# LIKE
# SELECT * FROM products WHERE name LIKE 'test';
# Product.objects.filter(name__exact='test')

# SELECT * FROM products WHERE name ILIKE 'test';
# Product.objects.filter(name__iexact='test')

# SELECT * FROM products WHERE name LIKE '%test%';
# Product.objects.filter(name__contains='test')

# SELECT * FROM products WHERE name ILIKE '%test%';
# Product.objects.filter(name__icontains='test')


# SELECT * FROM products WHERE name LIKE '%test%';
# Product.objects.filter(name__startwith='test')

# SELECT * FROM products WHERE name ILIKE '%test%';
# Product.objects.filter(name__startwith='test')

# получение одной записи
# Product.objects.get(id=1)
# SELECT *  FROM products WHERE id=1;

# ограничение набора полей
# SELECT name, price FROM products;
# Product.objects.only('name', 'price')

# SELECT_id, description, category_id FROM products;
# Product.objects.only('id', 'description', 'category_id')
# Product.objects.defer('name', 'price')

# SELECT * FROM products ORDER BY price;
# Product.objects.order_by('price')

# SELECT * FROM products ORDER BY price DESC;
# Product.objects.order_by('-price')

# INSERT

# INSERT INTO products (name, description, price, category) VALUES ('MI 10', 'норм телефон', 40000, 'phones')

# Product.objects.create('MI 10', 'норм телефон', 40000, 'phones')

# Product.objects.bulk_create(
#     [
#         Product(...),
#         Product(...)
#     ]
# )

# product = Product(...)
# product.save()


# update
# UPDATE products SET price = 10000;
# Product.objects.update(price=10000)

# UPDATE products SET price=10000 WHERE category = 'phones'
# Product.objects.filter(category='phones').update(price=20000)

# обновляем 1 объект
# product = Product.objects.get(id=1)
# product.price = 20000
# product.save()

# DElETE
# DELETE FROM products;
# Product.objects.delete()

# DELETE FROM products WHERE category = 'tv';
# Product.objects.filter(category='tv').delete()

