# Generated by Django 3.0.6 on 2020-05-17 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eshop', '0008_app_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='app',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
