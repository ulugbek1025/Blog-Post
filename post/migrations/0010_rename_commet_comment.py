# Generated by Django 3.2.5 on 2021-07-28 19:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0009_commet'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Commet',
            new_name='Comment',
        ),
    ]