# Generated by Django 3.1.6 on 2021-02-04 17:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20210204_2039'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='customer',
            new_name='user',
        ),
    ]
