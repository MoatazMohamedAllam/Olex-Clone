# Generated by Django 3.0.4 on 2020-03-25 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0012_auto_20200325_1419'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='city_name',
            field=models.CharField(blank=True, choices=[('Alexandria', 'Alexandria'), ('Aswan', 'Aswan'), ('Asyut', 'Asyut'), ('Beheira', 'Beheira'), ('Beni Suef', 'Beni Suef'), ('Cairo', 'Cairo'), ('Dakahlia', 'Dakahlia'), ('Damietta', 'Damietta'), ('Faiyum', 'Faiyum'), ('Gharbia', 'Gharbia'), ('Giza', 'Giza'), ('Ismailia', 'Ismailia'), ('Kafr El Sheikh', 'Kafr El Sheikh'), ('Luxor', 'Luxor'), ('Matruh', 'Matruh'), ('Minya', 'Minya')], max_length=150, null=True),
        ),
    ]