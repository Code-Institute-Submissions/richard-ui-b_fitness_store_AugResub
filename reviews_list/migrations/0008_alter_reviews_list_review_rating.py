# Generated by Django 3.2 on 2021-08-28 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews_list', '0007_alter_reviews_list_review_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviews_list',
            name='review_rating',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True),
        ),
    ]
