from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Article(models.Model):
    author=models.ForeignKey("auth.User",on_delete=models.CASCADE,verbose_name="Yazar")
    title=models.CharField(max_length=50,verbose_name="Başlık")
    content=RichTextField(verbose_name="içerik")
    created_date=models.DateTimeField(auto_now_add=True,verbose_name="Oluşturulma tarihi")
    article_img=models.FileField(blank=True,null=True,verbose_name="makaleye fotoğraf ekleyin")
    def __str__(self):
        return self.title
    class Meta:
        ordering = ['-created_date']


class Comment(models.Model):
    article=models.ForeignKey(Article,on_delete=models.CASCADE,verbose_name="makale",related_name="comments")
    user=models.CharField(max_length=200)    
    comment=models.CharField(max_length=200)
    date=models.DateTimeField(auto_now_add=True,verbose_name="Oluşturulma tarihi")
    class Meta:
        ordering = ['-date']



    

