# Generated by Django 3.2.18 on 2023-02-23 08:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('poster', '0002_delete_customer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('phone', models.CharField(max_length=15)),
                ('message', models.TextField(blank=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('post_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='poster.post')),
            ],
            options={
                'ordering': ['created_on'],
            },
        ),
    ]