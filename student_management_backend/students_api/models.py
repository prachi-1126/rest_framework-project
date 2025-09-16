from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    student_id = models.CharField(max_length=50, unique=True)
    date_of_birth = models.DateField(null=True, blank=True)
    contact_email = models.EmailField(unique=True)
    phone_contact = models.CharField(max_length=20, blank=True, null=True)
    parent_contact_phone = models.CharField(max_length=20, blank=True, null=True)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
