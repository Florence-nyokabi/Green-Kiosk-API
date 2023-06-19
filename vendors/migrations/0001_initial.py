# Generated by Django 4.2.3 on 2023-07-07 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vendors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vendor_id', models.IntegerField()),
                ('vendor_name', models.CharField(max_length=32)),
                ('vendor_email', models.CharField(max_length=32)),
                ('vendor_address', models.CharField(max_length=32)),
                ('vendor_ratings', models.CharField(max_length=32)),
            ],
        ),
    ]
