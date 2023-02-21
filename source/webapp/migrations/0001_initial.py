# Generated by Django 4.1.6 on 2023-02-21 05:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Наименование категории')),
                ('description', models.TextField(max_length=500, null=True, verbose_name='Описание')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Наименование')),
                ('description', models.TextField(max_length=500, null=True, verbose_name='Описание')),
                ('added_at', models.DateTimeField(auto_now_add=True, verbose_name='Время добавления')),
                ('price', models.DecimalField(decimal_places=2, max_digits=20, verbose_name='Стоимость')),
                ('image', models.TextField(max_length=3000, verbose_name='URL картинки')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products',
                                               to='webapp.category', verbose_name='Категория')),
            ],
        ),
    ]