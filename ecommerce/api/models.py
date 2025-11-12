from django.db import models

# Create your models here.
class Ecommerce(models.Model):
    id = models.AutoField(primary_key=True)
    name=models.CharField(max_length=255)
    price=models.DecimalField(max_digits=15, decimal_places=2)
    rating=models.DecimalField(max_digits=15 , decimal_places=2)
    image=models.ImageField(upload_to='products/',null=True,blank=True)

    def __str__(self):
        return self.name