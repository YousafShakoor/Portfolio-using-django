from django.db import models

# Create your models here.
class Header(models.Model):
    name=models.CharField(max_length=255)
    designation=models.CharField(max_length=255)
    title_line=models.CharField(max_length=255)

    def __str__(self):
        return self.name


class education(models.Model):
    school=models.CharField(max_length=255)
    course=models.CharField(max_length=255)
    year=models.PositiveIntegerField()

    def __str__(self):
        return self.school
    
class experience(models.Model):
    role=models.CharField(max_length=255)
    company=models.CharField(max_length=255)
    description=models.TextField()

    def __str__(self):
        return self.role
    
class skills(models.Model):
    skill=models.CharField(max_length=255)

    def __str__(self):
        return self.skill

class portfolio(models.Model):
    project=models.CharField(max_length=255)
    image=models.ImageField(upload_to='Images/')

    def __str__(self):
        return self.project

class contact(models.Model):
    username=models.CharField(max_length=255)
    email=models.CharField(max_length=255)
    message=models.TextField()

    def __str__(self):
        return self.username

class detail(models.Model):
    email=models.CharField(max_length=255)
    degree=models.CharField(max_length=255)
    birthday=models.DateField(auto_now=False, auto_now_add=False)
    phone=models.IntegerField()
    city=models.CharField(max_length=255)
    age=models.IntegerField()

    def __str__(self):
        return self.email
