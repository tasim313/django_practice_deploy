from django.shortcuts import render
from . import models
from . import customer_froms


def customer_home(request):
    new_from = customer_froms.CustomerForm()
    if request.method == "POST":
        new_from = customer_froms.CustomerForm(request.POST)
        if new_from.is_valid():
            new_from.save(commit=True)
            return index(request)
    dictionary ={
        'new_from': new_from
    }
    return render(request, 'customer_home.html', context=dictionary)


def index(request):
    customer_list = models.Customer.objects.order_by('name')
    dictionary = {'customer_list': customer_list, 'sample_text': 'I am a sample text !! ', 'add': '8',
                  'customer': models.Customer.objects.get(pk=2)}
    return render(request, 'index.html', context=dictionary)