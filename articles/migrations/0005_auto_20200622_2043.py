# Generated by Django 2.2.10 on 2020-06-22 17:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_auto_20200622_2036'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='scope',
            options={'ordering': ['-topic'], 'verbose_name': 'Тема', 'verbose_name_plural': 'Темы'},
        ),
        migrations.AlterModelOptions(
            name='scopearticle',
            options={'ordering': ['-is_main'], 'verbose_name': 'Тематика статьи', 'verbose_name_plural': 'Тематики статей'},
        ),
    ]