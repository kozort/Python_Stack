# Generated by Django 2.2 on 2021-07-18 23:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books_authors_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='author',
            old_name='description',
            new_name='notes',
        ),
    ]
