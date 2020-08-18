from django.db import models

class Comment(models.Model):
    text = models.TextField(verbose_name="Комментарии")
    author = models.CharField(max_length=255, verbose_name="Автор")

    def __str__(self):
        return self.author


class News(models.Model):
    name = models.CharField(max_length=255, verbose_name="Имя")
    create_date = models.DateField(verbose_name="Дата")
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, null=True)
    image = models.ImageField(verbose_name="Картинка", upload_to='media/image/')
    file = models.FileField(upload_to='media/file/')

    class Meta:
        verbose_name = "News"
        verbose_name_plural = "News"

    def __str__(self):
        return self.name



# Create your models here.
