# Generated by Django 4.1.2 on 2023-06-06 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0002_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='Photo',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/'),
        ),
    ]