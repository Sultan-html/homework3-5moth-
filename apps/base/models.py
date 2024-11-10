from django.db import models

# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    author = models.CharField(max_length=255, verbose_name="Автор")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    pages = models.PositiveIntegerField(verbose_name="Количество страниц")
    logo = models.ImageField(upload_to='logo/', blank=True, null=True, verbose_name="Логотип")

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книгы'