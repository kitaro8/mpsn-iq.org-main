# Generated by Django 4.1.7 on 2023-07-04 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testdb', '0004_rename_date_paper_link_remove_paper_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paper',
            name='link',
            field=models.CharField(max_length=9999999),
        ),
        migrations.AlterField(
            model_name='paper',
            name='title',
            field=models.TextField(),
        ),
    ]
