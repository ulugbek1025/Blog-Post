# Generated by Django 3.2.5 on 2021-07-27 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_alter_post_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_image',
            field=models.FileField(blank=True, null=True, upload_to='', verbose_name='Rasm'),
        ),
    ]
