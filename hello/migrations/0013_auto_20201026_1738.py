# Generated by Django 3.1.2 on 2020-10-26 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0012_auto_20201025_1338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='event_title',
            field=models.CharField(max_length=255, verbose_name='Event Title'),
        ),
    ]
