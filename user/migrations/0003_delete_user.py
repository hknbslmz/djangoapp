# Generated by Django 3.1.4 on 2021-01-06 17:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]