# Generated by Django 3.1.1 on 2020-10-29 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_register', '0002_auto_20201027_1729'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='DOB',
            field=models.DateField(auto_now=True),
        ),
    ]
