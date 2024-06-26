# Generated by Django 4.0.10 on 2023-03-29 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_service_blog_service'),
    ]

    operations = [
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('service', models.ManyToManyField(related_name='portfolio', to='blog.service')),
            ],
        ),
    ]
