# Generated by Django 3.1.6 on 2021-02-04 17:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='user',
            new_name='customer',
        ),
    ]
