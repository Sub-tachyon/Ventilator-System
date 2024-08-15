from django.db import models
from django.utils import timezone

class userdata(models.Model):
    username=models.CharField(max_length=255,null=True)
    email = models.CharField(max_length=255,null=True)
    password = models.CharField(max_length=255,null=True)
    doctor_id = models.AutoField(primary_key=True,unique=True)

class logs(models.Model):
    serial_number = models.CharField(max_length=50, unique=False)
    email= models.CharField(max_length=255,null=True)
    log_in = models.DateTimeField(null=True,blank=True)
    log_out= models.DateTimeField(null=True,blank=True)
    
    
class PasswordResetToken(models.Model):
    email = models.EmailField(max_length=255,null=True)
    token = models.CharField(max_length=100, editable=False) 
    

    def __str__(self):
        return f"Password Reset Token for {self.email}"
 