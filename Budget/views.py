from django.shortcuts import render
from django.http import HttpResponse
from .models import Budget


Budgets = [{'Creator': 'Roma Ostrovskiy', 'UAH_amount': 2056, 'USD_amount': 235, },
         {'Creator': 'Sergiy Sergienko', 'UAH_amount': 103232, 'USD_amount': 23255, },
         ]


def home(request):

    context = {
        'posts': Budget.objects.all()
    }
    return render(request, 'budget/home.html', context=context)


def check_budget(request):
    return HttpResponse("Your budget is 2092")


def about(request):
    return render(request, 'budget/about.html')

# Create your views here.
