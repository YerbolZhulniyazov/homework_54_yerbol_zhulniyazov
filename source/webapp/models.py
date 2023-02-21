from django.db import models


# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=50, null=False, blank=False, verbose_name='Наименование категории')
    description = models.TextField(max_length=500, null=True, blank=False, verbose_name="Описание")

    def __str__(self):
        return f'{self.title}'


class Product(models.Model):
    category = models.ForeignKey(
        to='webapp.Category',
        verbose_name='Категория',
        null=False,
        blank=False,
        related_name='products',
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=50, null=False, blank=False, verbose_name='Наименование')
    description = models.TextField(max_length=500, null=True, blank=False, verbose_name="Описание")
    added_at = models.DateTimeField(auto_now_add=True, verbose_name="Время добавления")
    price = models.DecimalField(max_digits=20, decimal_places=2, null=False, verbose_name='Стоимость')
    image = models.TextField(max_length=3000, null=False, blank=False, verbose_name="URL картинки")

    def __str__(self):
        return f'{self.name} - {self.added_at}'
