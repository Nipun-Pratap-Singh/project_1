# Generated by Django 5.0.4 on 2024-05-05 21:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerceapp', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Orders',
        ),
        migrations.DeleteModel(
            name='OrderUpdate',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
    ]
