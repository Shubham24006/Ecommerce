# Generated by Django 2.0.6 on 2018-07-12 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={},
        ),
        migrations.AddField(
            model_name='order',
            name='phone_no',
            field=models.CharField(default='no number', max_length=12),
        ),
    ]