from django.db import models

# Create your models here.

GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female'),
)

STATUS_CHOICES = (
    ('P', 'Pending'),
    ('C', 'Completed'),
    ('D', 'Delivered'),
)

class Patient(models.Model):
    name = models.CharField(max_length=100, help_text="Full name of the patient")
    age = models.IntegerField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Test(models.Model):
    test_name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.test_name


class LabReport(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='P')
    result_value = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    result_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.patient, self.test
