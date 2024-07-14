# Generated by Django 5.0.6 on 2024-07-01 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0004_alter_listing_state'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listing',
            name='year',
        ),
        migrations.AlterField(
            model_name='listing',
            name='category',
            field=models.CharField(choices=[('cars', 'Cars'), ('bikes', 'Bikes'), ('mobiles', 'Mobiles'), ('pets', 'Pets'), ('fashion', 'Fashion'), ('book', 'Books'), ('furniture', 'Furniture'), ('electronics', 'Electronics & Appliances'), ('properties', 'Properties'), ('sports', 'Sports'), ('commercial_vehicle', 'Commercial Vehicle Spares')], max_length=50),
        ),
    ]
