# Generated by Django 2.2.4 on 2019-11-03 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('informesContables', '0005_auto_20191103_1253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cuenta',
            name='debe',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6),
        ),
        migrations.AlterField(
            model_name='cuenta',
            name='haber',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6),
        ),
    ]
