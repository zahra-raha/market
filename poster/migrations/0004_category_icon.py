# Generated by Django 3.2.18 on 2023-02-24 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poster', '0003_customer'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='icon',
            field=models.CharField(default='ri-seedling-line', max_length=30),
        ),
    ]
