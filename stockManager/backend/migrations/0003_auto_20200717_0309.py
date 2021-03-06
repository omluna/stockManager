# Generated by Django 3.0.8 on 2020-07-17 03:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_auto_20200716_1302'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Dividents',
        ),
        migrations.AddField(
            model_name='operation',
            name='cash',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='operation',
            name='reserve',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='operation',
            name='stock',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='operation',
            name='operationType',
            field=models.CharField(choices=[('BUY', 'Buy'), ('SELL', 'Sell'), ('DV', 'Divident')], default='BUY', max_length=4),
        ),
    ]
