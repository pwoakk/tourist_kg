# Generated by Django 3.2 on 2022-04-14 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0002_auto_20220407_2105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tourbooking',
            name='is_paid',
            field=models.BooleanField(default=False, verbose_name='Оплачено'),
        ),
    ]