# Generated by Django 5.1.6 on 2025-03-14 17:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rec_app', '0003_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='labresult',
            name='doctor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rec_app.staffusers'),
        ),
        migrations.CreateModel(
            name='Imaging',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('record_type', models.CharField(choices=[('vitals', 'Vitals'), ('lab_results', 'Lab Results'), ('imaging', 'Imaging'), ('prescription', 'Prescription'), ('services_procedures', 'Services & Procedures')], max_length=50)),
                ('summary', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('scan_type', models.CharField(max_length=100)),
                ('scan_result', models.FileField(upload_to='imaging_reports/')),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='imaging', to='rec_app.staffusers')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rec_app.patient')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Prescription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('record_type', models.CharField(choices=[('vitals', 'Vitals'), ('lab_results', 'Lab Results'), ('imaging', 'Imaging'), ('prescription', 'Prescription'), ('services_procedures', 'Services & Procedures')], max_length=50)),
                ('summary', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('medication_name', models.CharField(max_length=100)),
                ('dosage', models.CharField(max_length=50)),
                ('frequency', models.CharField(max_length=50)),
                ('duration', models.CharField(max_length=50)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prescriptions', to='rec_app.staffusers')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rec_app.patient')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ServiceProcedure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('record_type', models.CharField(choices=[('vitals', 'Vitals'), ('lab_results', 'Lab Results'), ('imaging', 'Imaging'), ('prescription', 'Prescription'), ('services_procedures', 'Services & Procedures')], max_length=50)),
                ('summary', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('procedure_name', models.CharField(max_length=100)),
                ('procedure_notes', models.TextField()),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='procedures', to='rec_app.staffusers')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rec_app.patient')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
