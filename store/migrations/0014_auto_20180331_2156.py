# Generated by Django 2.0.3 on 2018-03-31 12:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0013_auto_20180331_2044'),
    ]

    operations = [
        migrations.AddField(
            model_name='thanhtoan',
            name='code',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='thanhtoan',
            name='status',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.DO_NOTHING, to='store.Status'),
        ),
    ]
