# Generated by Django 2.0.6 on 2018-06-26 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='quantities',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]