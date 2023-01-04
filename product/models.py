from django.db import models

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=50)
    author = models.CharField(max_length=100)
    rating = models.FloatField()
    learners = models.IntegerField()
    description = models.CharField(max_length=250)
    published_on = models.DateField()
    fees = models.IntegerField()
    imagePath = models.CharField(max_length=500)
    topic = models.CharField(max_length=1000)

class Order(models.Model):
    course = models.ForeignKey("Course", on_delete= models.CASCADE)
    studentName = models.CharField(max_length=200)
    mobile = models.BigIntegerField()
    email = models.EmailField(max_length=100)
    address = models.CharField(max_length=200)


# class Author(models.Model):
#     name = models.CharField(max_length=50)
