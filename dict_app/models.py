from django.db import models
from django.contrib.auth.models import AbstractUser




# Create your models here.

class Login(AbstractUser):
    is_importer = models.BooleanField(default=False)
    


class Teacher(models.Model):
    FirstName = models.CharField(max_length=100)
    LastName = models.CharField(max_length=100)
    Profile_picture =models.FileField(upload_to='documents/')
    Email =models.EmailField()
    Address= models.TextField(max_length=200)
    Phone=models.CharField(max_length=100)
    NumberRoom=models.IntegerField()
    CHOICES =(
    ("computer science", "computer science"),
    ("mathematics", "mathematics"),
    ("history", "history"),
    ("geography", "geography"),
    ("physics", "physics"),
     ("chemistry", "chemistry"),
    ("biology", "biology"),
    ("english", "english"),
    ("arabic", "arabic"),
    ("computer science", "computer science"),
)
    Subjects=models.CharField(choices = CHOICES , max_length=100)
    
    def __str__(self):
        return self.name



class csv(models.Model):
    file_name=models.FileField(upload_to = 'csv')
    uploaded = models.DateTimeField(auto_now = True)
    activate = models.BooleanField(default = False)

    def __str__(self):
        return f"File id:{self.id}"