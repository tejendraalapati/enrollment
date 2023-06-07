# Generated by Django 4.1.2 on 2023-06-06 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=10)),
                ('address', models.CharField(max_length=100)),
                ('Course', models.CharField(choices=[('PHP', 'PHP'), ('Front-end web development', 'Front-end web development'), ('Django', 'Django'), ('Node js', 'Node js'), ('java', 'java'), ('Python', 'Python')], default='1', max_length=25)),
                ('Percentage', models.CharField(max_length=100)),
                ('Photo', models.ImageField(upload_to='uploads/')),
            ],
        ),
    ]
