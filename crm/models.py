from django.db import models

class Order(models.Model):
    order_dt = models.DateTimeField(auto_now=True)
    order_name = models.CharField(max_length=200, verbose_name="Имя")
    order_phone = models.CharField(max_length=200, verbose_name="Номер")

    def __str__(self):
        return self.order_name

    class Meta:
        verbose_name = "Zakaz"
        verbose_name_plural = "Zakazy"