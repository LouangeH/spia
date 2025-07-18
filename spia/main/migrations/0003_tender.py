# Generated by Django 5.1.7 on 2025-05-15 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_admission_birth_certificate_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tender',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('category', models.CharField(choices=[('STAFF', 'Staff Recruitment'), ('SUPPLIES', 'School Supplies')], max_length=20)),
                ('document', models.FileField(upload_to='tenders/')),
                ('published_at', models.DateTimeField(auto_now_add=True)),
                ('deadline', models.DateField()),
            ],
        ),
    ]
