# from .forms import UserForm
from .models import Customer, Card
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import CustomerForm, CardForm, DeactivateCardForm


def index(request):
    customer_form = CustomerForm()
    card_form = CardForm()
    deactivate_card_form = DeactivateCardForm()
    customers = Customer.objects.all()

    return render(request, 'firstapp/index.html', {
        'customer_form': customer_form,
        'card_form': card_form,
        'deactivate_card_form': deactivate_card_form,
        'customers': customers})


def create_customer(request):
    customer_form = CustomerForm(request.POST)
    if not customer_form.is_valid():  # это если кто-то считерил и отправил неверные данные
        return HttpResponse(status=400)

    customer_form.save()

    return HttpResponseRedirect('/')


def create_card(request):
    card_form = CardForm(request.POST)
    if not card_form.is_valid():  # это если кто-то считерил и отправил неверные данные
        return HttpResponse(status=400)

    card_form.save()  # тут мы сохраняем данные из формы в БД

    return HttpResponse('success')


def deactivate_card(request):
    form = DeactivateCardForm(request.POST)
    if not form.is_valid():
        return HttpResponse(status=400)
    Card.objects.filter(
        id=form.cleaned_data['card'].id).update(active=False)
    return HttpResponseRedirect('/')
