# Generated by Django 4.0.10 on 2023-03-28 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_author_blog_main_image_alter_blog_text_blog_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='title',
        ),
        migrations.AddField(
            model_name='blog',
            name='name',
            field=models.CharField(max_length=150, null=True),
        ),
    ]
