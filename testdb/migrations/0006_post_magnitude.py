# Generated by Django 5.0.3 on 2024-03-13 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testdb', '0005_remove_post_magnitude'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='Magnitude',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
