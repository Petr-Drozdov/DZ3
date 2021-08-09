from django.http import Http404
from django.shortcuts import render, HttpResponse
from MainApp.models import Item
from django.core.exceptions import ObjectDoesNotExist


def index(request):
    return render(request, "index.html")


def about(request):
    name = 'Petr'
    second_name = 'Dr'
    surname = 'D'
    tel = '0-900-90-00-00'
    email = '_______________.com'
    return HttpResponse(f'Имя: <b>{name}</b><br>Отчество: <b>{second_name}</b><br>'
                        f'Фамилия: <b>{surname}</b><br>Телефон: <b>{tel}</b><br>'
                        f'e-mail: <b>{email}<b>')


def items(request):
    items = Item.objects.all()
    context = {"items": items}
    return render(request, "items_list.html", context)


def item_details(request, id):
    try:
        item = Item.objects.get(pk=id)
    except ObjectDoesNotExist:
        raise Http404
    context = {
        "item": item
    }
    return render(request, "item_page.html", context)
