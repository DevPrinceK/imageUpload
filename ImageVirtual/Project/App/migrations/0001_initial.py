# Generated by Django 3.2.7 on 2021-09-19 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='img', max_length=50)),
                ('image', models.ImageField(upload_to='uploaded_images')),
            ],
        ),
    ]
