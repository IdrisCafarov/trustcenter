# Generated by Django 4.0.10 on 2023-03-28 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_blog_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='click',
            field=models.PositiveIntegerField(default=0, editable=False),
        ),
    ]
