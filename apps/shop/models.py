from django.db import models

class Plant(models.Model):
    img = models.ImageField(upload_to='plants/%Y/%m/%d/')
    name = models.CharField(max_length=35)
    price = models.DecimalField(decimal_places=2, max_digits=7)

    def __str__(self):
        return str(self.name) + ": $" + str(self.price)