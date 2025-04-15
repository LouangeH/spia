from django import forms
from main.models import Admission

class AdmissionForm(forms.ModelForm):
    class Meta:
        model = Admission
        fields = [
            'academic_year', 'grade', 'full_name', 'date_of_birth', 'age', 'gender', 'nationality', 'place_of_birth', 'home_address',
            'guardian_name', 'guardian_relationship', 'guardian_phone', 'guardian_email', 'guardian_occupation', 'guardian_employer',
            'previous_school', 'school_location', 'last_grade_completed', 'languages_spoken',
            'allergies', 'medical_conditions', 'doctor_name', 'doctor_contact',
            'emergency_contact_name', 'emergency_relationship', 'emergency_phone',
            'hobbies_interests', 'special_skills', 'reason_for_applying',
            'birth_certificate', 'passport_photo', 'last_report_card', 'transfer_letter', 'immunization_records'
        ]
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
            'birth_certificate': forms.FileInput(),
            'passport_photo': forms.FileInput(),
            'last_report_card': forms.FileInput(),
            'transfer_letter': forms.FileInput(),
            'immunization_records': forms.FileInput()
        }