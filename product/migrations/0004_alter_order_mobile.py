# Generated by Django 4.1.2 on 2022-11-21 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='mobile',
            field=models.BigIntegerField(),
        ),
    ]
