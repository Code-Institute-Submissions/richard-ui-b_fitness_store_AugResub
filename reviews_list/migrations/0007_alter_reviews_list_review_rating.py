# Generated by Django 3.2 on 2021-08-28 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews_list', '0006_rename_rating_reviews_list_review_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviews_list',
            name='review_rating',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], default='3', max_length=10),
        ),
    ]
