# Generated by Django 4.1.4 on 2023-01-09 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_book_description_alter_author_name_alter_book_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='grade',
            field=models.CharField(choices=[('freshman', 'Freshman'), ('sophomore', 'Sophomore'), ('junior', 'Junior'), ('senior', 'Senior')], max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='author',
            name='alive',
            field=models.BooleanField(default=1),
        ),
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.ManyToManyField(related_name='books', to='core.author', verbose_name='Authors'),
        ),
    ]
