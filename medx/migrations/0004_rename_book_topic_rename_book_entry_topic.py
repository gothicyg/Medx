# Generated by Django 4.0.5 on 2022-06-10 17:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medx', '0003_entry'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Book',
            new_name='Topic',
        ),
        migrations.RenameField(
            model_name='entry',
            old_name='book',
            new_name='topic',
        ),
    ]
