# Generated by Django 5.1.7 on 2025-04-03 07:06

import main.models.admission
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admission',
            name='birth_certificate',
            field=models.FileField(blank=True, null=True, upload_to='admissions/', validators=[main.models.admission.validate_file_extension]),
        ),
        migrations.AlterField(
            model_name='admission',
            name='immunization_records',
            field=models.FileField(blank=True, null=True, upload_to='admissions/', validators=[main.models.admission.validate_file_extension]),
        ),
        migrations.AlterField(
            model_name='admission',
            name='last_report_card',
            field=models.FileField(blank=True, null=True, upload_to='admissions/', validators=[main.models.admission.validate_file_extension]),
        ),
        migrations.AlterField(
            model_name='admission',
            name='passport_photo',
            field=models.FileField(blank=True, null=True, upload_to='admissions/', validators=[main.models.admission.validate_file_extension]),
        ),
        migrations.AlterField(
            model_name='admission',
            name='transfer_letter',
            field=models.FileField(blank=True, null=True, upload_to='admissions/', validators=[main.models.admission.validate_file_extension]),
        ),
    ]
