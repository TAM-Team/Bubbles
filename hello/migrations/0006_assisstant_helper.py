# Generated by Django 3.1.1 on 2020-10-18 04:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0005_helper_helper'),
    ]

    operations = [
        migrations.AddField(
            model_name='assisstant',
            name='helper',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
