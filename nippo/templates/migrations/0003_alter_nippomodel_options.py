# Generated by Django 4.2.4 on 2023-11-25 06:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nippo', '0002_alter_nippomodel_content_alter_nippomodel_title'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='nippomodel',
            options={'verbose_name': '日報', 'verbose_name_plural': '日報一覧'},
        ),
    ]