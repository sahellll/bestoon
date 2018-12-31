import datetime
from json import JSONEncoder

from django.http import JsonResponse
from web.models import User, Token, Income, Expense
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def submit_expense(request):
    """user submis anexpense"""
    # TODO; validate data ,amount might be fake , user might be fake , token might be fake ...
    this_token = request.POST['token']
    this_user = User.objects.filter(token__token=this_token).get()
    if 'date' not in request.POST:
        now = datetime.datetime.now()
    Expense.objects.create(User=this_user, amount=request.POST['amount'], text=request.POST['text'], date=now)
   
    return JsonResponse({
        'status': 'ok',

    }, encoder=JSONEncoder)


@csrf_exempt
def submit_income(request):
    """ submis an income"""
    # TODO; validate data ,amount might be fake , user might be fake , token might be fake ...
    this_token = request.POST['token']
    this_user = User.objects.filter(token__token=this_token).get()
    if 'date' not in request.POST:
        date = datetime.datetime.now()
    Income.objects.create(User=this_user, amount=request.POST['amount'], text=request.POST['text'], date=date)

    return JsonResponse({
        'status': 'ok',

    }, encoder=JSONEncoder)

