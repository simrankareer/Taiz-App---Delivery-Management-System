# Generated by Django 4.2.6 on 2023-10-21 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_remove_customer_alternatenumber'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='alternatenumber',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
