# Generated by Django 4.0.4 on 2022-05-12 14:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0022_remove_vacancy_recruiter_alter_vacancy_requirements'),
    ]

    operations = [
        migrations.AddField(
            model_name='vacancy',
            name='recruiter',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='vacancies', to='service.recruiter'),
            preserve_default=False,
        ),
    ]