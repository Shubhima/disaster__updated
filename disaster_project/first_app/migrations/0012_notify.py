# Generated by Django 3.0.5 on 2020-06-09 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0011_subscribe'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notify',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Subject', models.CharField(max_length=300, unique=True)),
                ('Message', models.TextField()),
            ],
        ),
    ]