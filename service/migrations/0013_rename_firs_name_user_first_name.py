# Generated by Django 4.0.4 on 2022-05-08 16:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0012_alter_insurancedata_country'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='firs_name',
            new_name='first_name',
        ),
    ]
