# Generated by Django 3.2.19 on 2024-03-23 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testdb', '0012_remove_post_magnitudemw'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='MagnitudeMW',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
