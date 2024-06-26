# Generated by Django 4.0.10 on 2023-03-29 10:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='GeneralSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adress', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='PhoneGeneral',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=20)),
                ('general', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.generalsettings')),
            ],
        ),
    ]
