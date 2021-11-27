from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        pass


class Plant(models.Model):
    name = models.CharField(max_length=150, db_index=True)
    img = models.ImageField(upload_to='plants/%Y/%m/%d/')
    price = models.DecimalField(decimal_places=2, max_digits=10)
    slug = models.SlugField(max_length=150, db_index=True)
    category = models.ForeignKey(Category, related_name='plants', on_delete=models.CASCADE)
    available = models.BooleanField(default=True)
    stock = models.PositiveIntegerField()

    class Meta:
        ordering = ('name',)
        index_together = (
            ('id', 'slug'),
        )

    def __str__(self):
        return str(self.name) + ": $" + str(self.price)

    def get_absolute_url(self):
        return reverse('shop:plant_detail', args=[self.id, self.slug])
