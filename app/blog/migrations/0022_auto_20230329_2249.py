# Generated by Django 3.2.18 on 2023-03-29 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0021_auto_20230329_2235'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolio',
            name='date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='portfolio',
            name='live_demo_link',
            field=models.CharField(max_length=2000, null=True),
        ),
        migrations.AddField(
            model_name='portfolio',
            name='text',
            field=models.TextField(null=True),
        ),
    ]
