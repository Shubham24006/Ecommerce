# Generated by Django 2.1.4 on 2018-12-08 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_auto_20180712_1121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='paid',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]
