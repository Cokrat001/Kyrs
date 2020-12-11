from django.db import models

# Create your models here.


class Card(models.Model):
    name = models.CharField(max_length=50)
    number_card = models.CharField(max_length=19)
    date_of_create = models.CharField(max_length=15)
    pay_limit = models.BigIntegerField('pay limit')
    ccv = models.CharField(max_length=50)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Customer(models.Model):
    name = models.CharField(max_length=50, default='')
    address = models.CharField(max_length=100, default='')
    phone_number = models.CharField(max_length=20)
    balance = models.DecimalField(max_digits=4, decimal_places=2, default=0)
    card = models.ForeignKey(Card, on_delete=models.DO_NOTHING, null=True)

    def __str__(self):
        return self.name + ' - ' + str(self.balance)


# !!! после обновления модели БД нам надо мигрировать на неё.
# Сначала создаём миграцию: py manage.py makemigrations firstapp
# Потом вызываем: py manage.py migrate
