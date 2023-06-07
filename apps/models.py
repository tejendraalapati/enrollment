from django.db import models

# Create your models here.
class profile(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    username=models.CharField(max_length=100)
    email=models.EmailField(max_length=254)
    phone_number=models.CharField(max_length=10)
    address=models.CharField(max_length=100)
    COURSE_CHOICES=(
        ('PHP','PHP'),
        ('Front-end web development','Front-end web development'),
        ('Django','Django'),
        ('Node js','Node js'),
        ('java','java'),
        ('Python','Python')
    )
    Course=models.CharField(max_length= 25, choices=COURSE_CHOICES, default='1')
    Photo=models.ImageField(upload_to='images/')
    Percentage=models.CharField(max_length=100)

class contact(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    phone_number=models.CharField(max_length=100)
    message=models.CharField(max_length=100)
    

