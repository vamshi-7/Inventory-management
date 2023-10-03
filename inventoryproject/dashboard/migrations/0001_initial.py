# Generated by Django 4.2.3 on 2023-09-21 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=255)),
                ('product_quantity', models.PositiveIntegerField()),
                ('dealer_name', models.CharField(max_length=255)),
            ],
        ),
    ]