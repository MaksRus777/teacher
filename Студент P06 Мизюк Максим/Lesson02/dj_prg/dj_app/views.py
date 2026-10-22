from django.shortcuts import render

# Методы для генерации ответа
from django.http import HttpResponse  # Способ №1 (Явно можем записать внутрь HTML код)
from django.http import HttpResponseRedirect  # Способ №2 (Указываем маршрут по которому будет взята HTML)
from django.shortcuts import render  # Способ №3 (Используем файлы шаблонов с HTML кодом)


# Главная (1 способ)
def index(request):
    return HttpResponse("<h2>Привет</h2>")


# О себе (2 способ)
def about(request):
    return HttpResponseRedirect("/")


# Контакты (3 способ)
def contact(request):
    name = "Вася"
    number = "+375(29)7776655"
    context = {"NUMBER": number, "NAME": name}  # Способ для передачи данных из Python в HTML
    return render(request, "contact.html", context=context)
