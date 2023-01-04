# Generated by Django 4.1.2 on 2022-11-06 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('author', models.CharField(max_length=100)),
                ('rating', models.FloatField()),
                ('learners', models.IntegerField()),
                ('description', models.CharField(max_length=250)),
                ('published_on', models.DateField()),
                ('fees', models.IntegerField()),
                ('imagePath', models.CharField(max_length=500)),
            ],
        ),
    ]
