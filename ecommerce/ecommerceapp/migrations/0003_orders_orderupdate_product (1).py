# Generated by Django 5.0.4 on 2024-05-05 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerceapp', '0002_delete_orders_delete_orderupdate_delete_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('items_json', models.CharField(max_length=5000)),
                ('amount', models.IntegerField(default=0)),
                ('name', models.CharField(max_length=90)),
                ('email', models.CharField(max_length=90)),
                ('address1', models.CharField(max_length=200)),
                ('address2', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('zip_code', models.CharField(max_length=100)),
                ('oid', models.CharField(blank=True, max_length=150)),
                ('amountpaid', models.CharField(blank=True, max_length=500, null=True)),
                ('paymentstatus', models.CharField(blank=True, max_length=20)),
                ('phone', models.CharField(default='', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='OrderUpdate',
            fields=[
                ('update_id', models.AutoField(primary_key=True, serialize=False)),
                ('order_id', models.IntegerField(default='')),
                ('update_desc', models.CharField(max_length=5000)),
                ('delivered', models.BooleanField(default=False)),
                ('timestamp', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=100)),
                ('category', models.CharField(default='', max_length=100)),
                ('subcategory', models.CharField(default='', max_length=50)),
                ('price', models.IntegerField(default=0)),
                ('desc', models.CharField(max_length=300)),
                ('image', models.ImageField(upload_to='images/images')),
            ],
        ),
    ]
