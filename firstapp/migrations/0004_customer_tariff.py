# Generated by Django 3.1.1 on 2020-12-04 09:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0003_customer_balance'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='tariff',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='firstapp.tariff'),
        ),
    ]