# Generated by Django 3.2.19 on 2024-03-25 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testdb', '0002_post_image2'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='file3',
            field=models.FileField(blank=True, upload_to='data2'),
        ),
    ]
