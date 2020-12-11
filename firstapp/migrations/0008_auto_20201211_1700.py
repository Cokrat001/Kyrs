# Generated by Django 3.1.1 on 2020-12-11 15:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0007_customer_additional_services'),
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('number_card', models.DecimalField(decimal_places=2, max_digits=5)),
                ('date_of_create', models.IntegerField(verbose_name='Date of create')),
                ('pay_limit', models.BigIntegerField(verbose_name='pay limit')),
                ('sms', models.IntegerField()),
                ('ccv', models.CharField(max_length=50)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Service',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='additional_services',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='tariff',
        ),
        migrations.DeleteModel(
            name='Tariff',
        ),
        migrations.AddField(
            model_name='customer',
            name='сard',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='firstapp.card'),
        ),
    ]
