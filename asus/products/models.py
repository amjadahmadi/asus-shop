from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)

    @property
    def children(self):
        return Category.objects.filter(parent=self)

    def __str__(self):
        return self.name


class Features(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class ProductFeatures(models.Model):
    product = models.ForeignKey('Products', on_delete=models.CASCADE)
    feature = models.ForeignKey(Features, on_delete=models.CASCADE)
    describe = models.TextField()

    def __str__(self):
        return f'{self.product.name}({self.feature.name})'


class Products(models.Model):
    name = models.CharField(max_length=255)
    category = models.ManyToManyField(Category)

    def __str__(self):
        return self.name

    @property
    def features(self):
        return ProductFeatures.objects.filter(product=self)
