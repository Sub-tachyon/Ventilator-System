from django.db import models

class Ventilator(models.Model):
    STATUS_CHOICES = (
        ('allocated', 'Allocated'),
        ('Not allocated', 'Not Allocated'),
    ) 
    battery_no=models.IntegerField(null=True,unique=True)
    battery_mfg_date=models.DateField(null=True,blank=True)
    serial_number = models.CharField(max_length=50, unique=True) 
    model = models.CharField(max_length=100, null=True, blank=True) #device name
    model_no=models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Not allocated')
    lot_no=models.IntegerField(null=True,unique=True)
    mfg_date=models.DateField(null=True,blank=True)
    mac=models.CharField(max_length=100,null=True)
    

class device_logs(models.Model):
    log_id = models.AutoField(primary_key=True,unique=True)
    serial_number = models.CharField(max_length=50)
    device_log_in = models.DateTimeField(null=True, blank=True)
    device_log_out = models.DateTimeField(null=True, blank=True)
    assigned_by_doc_id = models.CharField(max_length=255) 
    assigned_to_patient_id = models.CharField(max_length=255)



class mydevices(models.Model):
    email = models.EmailField(max_length=255,null=True)
    serial_number = models.CharField(max_length=50, unique=False)
  
class Patient(models.Model):
    name = models.CharField(max_length=100)
    patient_id = models.AutoField(primary_key=True,unique=True)
    age = models.IntegerField(null= True)
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    
    STATUS_CHOICES = [
        ('PASSIVE', 'Passive'),
        ('EMERGENCY', 'Emergency'),
        ('DISCHARGED', 'Discharged'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PASSIVE')
    doc_id = models.CharField(max_length=255)  # Link to userdata model
    doc_name = models.CharField(max_length=255, null=True)
    device = models.ForeignKey('Ventilator', on_delete=models.SET_NULL, null=True, blank=True)
    height = models.IntegerField(null=False)
    weight = models.IntegerField(null=False)
    blood = models.CharField(max_length=255,null=False)
    ibw = models.IntegerField(null=False)
    itv = models.IntegerField(null=False)
    bmi = models.IntegerField(null=False)
    admitted_date = models.DateTimeField(null=True, blank=True)
    reason = models.CharField(max_length=255,null=False)
    potential = models.CharField(max_length=255,null=False)
    contact = models.IntegerField(null=False)
    room_no= models.CharField(max_length=255,null=False)

