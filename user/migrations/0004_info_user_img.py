# Generated by Django 3.1.4 on 2021-01-06 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_delete_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='info',
            name='user_img',
            field=models.FileField(blank=True, null=True, upload_to='', verbose_name='profil fotoğrafı ekleyin'),
        ),
    ]
