# Generated by Django 3.0.6 on 2020-05-18 23:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eshop', '0012_monthlyvolume_discount_percent'),
    ]

    operations = [
        migrations.CreateModel(
            name='CalculateSection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=255)),
                ('description', models.TextField(default='')),
            ],
        ),
    ]
