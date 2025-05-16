from django.db import models

# Create your models here.

# La imagini - ne cuplam in settings.py


class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    slug = models.SlugField()

    def __str__(self):
        return self.name

    # Pentru pluralul din Admin (categories in loc de categorys)
    class Meta:
        verbose_name = "categorie"


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    slug = models.SlugField(blank=True)
    image = models.ImageField(upload_to="product_images")
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)

    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name





