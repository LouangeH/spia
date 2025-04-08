from django.db import models
from django.utils.crypto import get_random_string
from django.core.exceptions import ValidationError   

def validate_file_extension(value):
    import os
    ext = os.path.splitext(value.name)[1]  # Récupère l'extension du fichier
    valid_extensions = ['.jpg', '.png', '.pdf']
    if ext.lower() not in valid_extensions:
        raise ValidationError(f"Format non autorisé. Formats acceptés : {valid_extensions}")

def generate_application_id():
    return get_random_string(10).upper()

class Admission(models.Model):
    application_id = models.CharField(max_length=12, unique=True, editable=False, default=generate_application_id)
    academic_year = models.CharField(max_length=9)
    grade = models.CharField(max_length=50)
    
    # Student Information
    full_name = models.CharField(max_length=200)
    date_of_birth = models.DateField()
    age = models.IntegerField()
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female')])
    nationality = models.CharField(max_length=100)
    place_of_birth = models.CharField(max_length=100)
    home_address = models.TextField()
    
    # Parent/Guardian Information
    guardian_name = models.CharField(max_length=200)
    guardian_relationship = models.CharField(max_length=100)
    guardian_phone = models.CharField(max_length=20)
    guardian_email = models.EmailField()
    guardian_occupation = models.CharField(max_length=100, blank=True, null=True)
    guardian_employer = models.CharField(max_length=100, blank=True, null=True)
    
    # Academic Background
    previous_school = models.CharField(max_length=200)
    school_location = models.CharField(max_length=200)
    last_grade_completed = models.CharField(max_length=50)
    languages_spoken = models.CharField(max_length=200)
    
    # Medical Information
    allergies = models.TextField(blank=True, null=True)
    medical_conditions = models.TextField(blank=True, null=True)
    doctor_name = models.CharField(max_length=200, blank=True, null=True)
    doctor_contact = models.CharField(max_length=20, blank=True, null=True)
    
    # Emergency Contact
    emergency_contact_name = models.CharField(max_length=200)
    emergency_relationship = models.CharField(max_length=100)
    emergency_phone = models.CharField(max_length=20)
    
    # Additional Information
    hobbies_interests = models.TextField(blank=True, null=True)
    special_skills = models.TextField(blank=True, null=True)
    reason_for_applying = models.TextField()
    
    # Supporting Documents
    birth_certificate = models.FileField(upload_to='admissions/', validators=[validate_file_extension], blank=True, null=True)
    passport_photo = models.FileField(upload_to='admissions/', validators=[validate_file_extension], blank=True, null=True)
    last_report_card = models.FileField(upload_to='admissions/',validators=[validate_file_extension], blank=True, null=True)
    transfer_letter = models.FileField(upload_to='admissions/',validators=[validate_file_extension], blank=True, null=True)
    immunization_records = models.FileField(upload_to='admissions/',validators=[validate_file_extension], blank=True, null=True)
    
    submitted_at = models.DateTimeField(auto_now_add=True)
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')

    def __str__(self):
        return f"{self.application_id} - {self.full_name}"
