from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение', )

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title


class ScopeArticle(models.Model):
    is_main = models.BooleanField(verbose_name="Основной",)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    scope = models.ForeignKey('Scope', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Тематика статьи'
        verbose_name_plural = 'Тематики статей'

    # def __str__(self):
    #     return


class Scope(models.Model):
    topic = models.CharField(max_length=100, verbose_name="Раздел")
    article = models.ManyToManyField(Article, through=ScopeArticle, related_name="scopes")

    class Meta:
        verbose_name = 'Тема'
        verbose_name_plural = 'Темы'

    def __str__(self):
        return self.topic
