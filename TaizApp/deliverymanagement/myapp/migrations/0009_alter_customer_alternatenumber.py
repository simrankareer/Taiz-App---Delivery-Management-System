# Generated by Django 4.2.6 on 2023-10-21 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_customer_alternatenumber'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='alternatenumber',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
