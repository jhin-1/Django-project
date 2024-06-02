# Generated by Django 5.0.6 on 2024-06-02 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_site', '0007_alter_product_discount_alter_product_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='discount',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=10, null=True, verbose_name='discount'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=10, null=True, verbose_name='price'),
        ),
    ]