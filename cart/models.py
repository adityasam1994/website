from django.db import models

# Create your models here.
class Cart_Record(models.Model):
    user_id=models.IntegerField()
    product_id=models.IntegerField()
    quantity=models.IntegerField(default=1)

    class Meta:
        ordering=("user_id",)
