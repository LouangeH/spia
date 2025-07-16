# tenders/models.py
from django.db import models

class Tender(models.Model):
    CATEGORY_CHOICES = [
        ('STAFF', 'Staff Recruitment'),
        ('SUPPLIES', 'School Supplies'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    document = models.FileField(upload_to='tenders/')
    published_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateField()

    def __str__(self):
        return self.title
