# Generated by Django 3.2.18 on 2023-04-03 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0022_auto_20230329_2249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='main_image',
            field=models.FileField(null=True, upload_to='blog_image'),
        ),
    ]