# Generated by Django 2.0.3 on 2018-03-31 03:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_auto_20180331_0847'),
    ]

    operations = [
        migrations.AddField(
            model_name='thanhtoan',
            name='chitiet',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
