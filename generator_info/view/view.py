from django.shortcuts import render
from tools import luhn

def my_view(request):
    result=[]
    for i in range(0,10):
        result.append({'card_num':luhn.gen_card_num('622848', 16),'vin':luhn.random_vin()})
    return render(request, 'show.html', {'result': result})