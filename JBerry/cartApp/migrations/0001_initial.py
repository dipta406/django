# Generated by Django 4.0.6 on 2022-08-03 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='cartItem',
            fields=[
                ('cid', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('pid', models.IntegerField()),
                ('qty', models.SmallIntegerField()),
                ('uid', models.IntegerField()),
                ('in_cart', models.IntegerField()),
            ],
        ),
    ]
