# Generated by Django 5.1.3 on 2024-11-10 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок')),
                ('author', models.CharField(max_length=255, verbose_name='Автор')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('pages', models.PositiveIntegerField(verbose_name='Количество страниц')),
                ('logo', models.ImageField(blank=True, null=True, upload_to='logo/', verbose_name='Логотип')),
            ],
            options={
                'verbose_name': 'Книга',
                'verbose_name_plural': 'Книгы',
            },
        ),
    ]