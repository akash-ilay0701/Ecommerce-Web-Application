# Generated by Django 4.1.2 on 2022-11-09 12:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_course_topic'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('studentName', models.CharField(max_length=200)),
                ('mobile', models.IntegerField()),
                ('email', models.EmailField(max_length=100)),
                ('address', models.CharField(max_length=200)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.course')),
            ],
        ),
    ]
