# Generated by Django 4.0.4 on 2022-05-11 17:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0013_rename_firs_name_user_first_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('phone_number', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=80)),
                ('skills', models.JSONField(verbose_name=[])),
            ],
        ),
        migrations.CreateModel(
            name='Recruiter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='Vacancy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(max_length=20)),
                ('project_description', models.CharField(max_length=100)),
                ('company', models.CharField(max_length=20)),
                ('requirements', models.JSONField()),
                ('applied_candidates', models.ManyToManyField(related_name='applied_vacancies', to='service.candidate')),
                ('recruiter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service.recruiter')),
            ],
        ),
        migrations.RemoveField(
            model_name='insurancedata',
            name='reserved_by_user',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='user',
        ),
        migrations.DeleteModel(
            name='Document',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
