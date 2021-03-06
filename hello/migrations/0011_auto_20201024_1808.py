# Generated by Django 3.1.2 on 2020-10-24 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0010_auto_20201024_1343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='address',
            field=models.TextField(default='Mount Albert, Auckland, New Zealand', max_length=1025),
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='user',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to='i/'),
        ),
    ]
