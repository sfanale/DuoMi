# Generated by Django 2.0.7 on 2018-07-13 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0004_auto_20180713_1120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='total_shares',
            field=models.DecimalField(decimal_places=2, default=10000, max_digits=6),
        ),
    ]