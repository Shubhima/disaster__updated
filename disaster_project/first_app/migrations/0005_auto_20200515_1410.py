# Generated by Django 3.0.5 on 2020-05-15 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0004_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organization',
            name='Contact_Info',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='organization',
            name='Name',
            field=models.CharField(max_length=50),
        ),
    ]
