# Generated by Django 3.1.4 on 2021-01-07 15:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_message'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Message',
        ),
    ]
