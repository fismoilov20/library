# Generated by Django 4.1.4 on 2023-01-08 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_author_about'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='publication_date',
            field=models.DateField(null=True),
        ),
    ]
