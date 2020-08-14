# Generated by Django 3.0.5 on 2020-05-05 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0003_post'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('Email', models.EmailField(max_length=254)),
                ('Message', models.TextField(max_length=2048)),
                ('PhoneNo', models.CharField(max_length=10)),
            ],
        ),
    ]
