# Generated by Django 3.1.4 on 2021-01-03 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0007_auto_20210103_2313'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='user',
            field=models.CharField(max_length=200),
        ),
    ]
