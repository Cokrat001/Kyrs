# Generated by Django 3.1.1 on 2020-12-04 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0004_customer_tariff'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=50)),
                ('decsription', models.CharField(default='', max_length=100)),
            ],
        ),
    ]
