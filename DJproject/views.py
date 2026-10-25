from django.http import HttpResponse


def user_view(request):
    user_id = request.GET.get('id')
    fio = request.GET.get('fio')
    age = request.GET.get('age')
    address = request.GET.get('address')
    email = request.GET.get('email')
    phone = request.GET.get('phone')
    name = request.GET.get('name')

    if user_id is not None:
        return HttpResponse(f"<h1> {user_id}</h1>")
    elif fio is not None:
        return HttpResponse(f"<h1> {fio}</h1>")
    elif name is not None:
        return HttpResponse(f"<h1>{name}</h1>")
    elif age is not None:
        return HttpResponse(f"<h1>{age}</h1>")
    elif address is not None:
        return HttpResponse(f"<h1> {address}</h1>")
    elif email is not None:
        return HttpResponse(f"<h1> {email}</h1>")
    elif phone is not None:
        return HttpResponse(f"<h1> {phone}</h1>")

    return HttpResponse("<h1>Ничего не передано. Введите параметры в адресную строку!</h1>")