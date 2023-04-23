from django.shortcuts import render
from tools import luhn

BANK_LIST = [
    {"card_prefix": "622848", "card_name": "农行"},
    {"card_prefix": "622203", "card_name": "工行"},
    {"card_prefix": "621331", "card_name": "中行"},
    {"card_prefix": "622188", "card_name": "邮储"},
]


def my_view(request):
    card_prefix = '622848'
    if request.method == 'GET':
        card_prefix = request.GET.get('card_prefix', default=card_prefix)
    result = []
    for i in range(0, 10):
        result.append({'card_num': luhn.gen_card_num(card_prefix, 16), 'vin': luhn.random_vin()})
    return render(request, 'show.html', {'result': result, "bank_list": BANK_LIST, "card_prefix": card_prefix})
