# Generated by Django 3.1.4 on 2021-01-06 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ali', models.CharField(max_length=50)),
                ('birthday', models.DateTimeField()),
            ],
        ),
    ]
