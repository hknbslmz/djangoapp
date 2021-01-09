from django.db import models

# Create your models here.

class Info(models.Model):
    username=models.ForeignKey("auth.User",on_delete=models.CASCADE,verbose_name="bilgi",related_name="info")
    birthday=models.DateTimeField()
    user_img=models.FileField(blank=True,null=True,verbose_name="profil fotoğrafı ekleyin")

