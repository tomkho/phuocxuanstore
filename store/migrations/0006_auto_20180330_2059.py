# Generated by Django 2.0.3 on 2018-03-30 11:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_auto_20180330_2043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='loai',
            field=models.ForeignKey(default='null', on_delete=django.db.models.deletion.DO_NOTHING, to='store.Loai'),
        ),
    ]
