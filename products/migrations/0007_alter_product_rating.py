# Generated by Django 3.2 on 2021-08-28 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_alter_product_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='rating',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
