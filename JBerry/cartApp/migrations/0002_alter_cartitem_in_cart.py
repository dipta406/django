# Generated by Django 4.0.6 on 2022-08-03 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cartApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitem',
            name='in_cart',
            field=models.IntegerField(default=True),
        ),
    ]
