# Generated by Django 3.0.4 on 2020-03-25 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0011_product_city_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='city_name',
            field=models.CharField(blank=True, choices=[('Alexandria', 'Alexandria'), ('Aswan', 'Aswan'), ('Asyut', 'Asyut'), ('Beheira', 'Beheira'), ('Beni Suef', 'Beni Suef'), ('Cairo', 'Cairo'), ('Dakahlia', 'Dakahlia'), ('Damietta', 'Damietta'), ('Faiyum', 'Faiyum'), ('Gharbia', 'Gharbia')], max_length=150, null=True),
        ),
    ]