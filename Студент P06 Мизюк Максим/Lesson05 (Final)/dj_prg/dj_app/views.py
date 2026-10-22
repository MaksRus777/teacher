from django.shortcuts import render

# Методы для генерации ответа
from django.http import HttpResponse  # Способ №1 (Явно можем записать внутрь HTML код)
from django.http import HttpResponseRedirect  # Способ №2 (Указываем маршрут по которому будет взята HTML)
from django.shortcuts import render  # Способ №3 (Используем файлы шаблонов с HTML кодом)

from datetime import datetime  # Модуль для работы с датой и временем


# Главная (1 способ)
def index(request):
    html = ""
    menu1 = "<a href='/about'>О себе</a>"
    menu2 = "<a href='/contact'>Контакты</a>"
    btn1 = "<a href='/product/10/Nokia'>Продукты (1 способ)</a>"
    btn2 = "<a href='/products?product_id=8&name=Samsung'>Продукты (2 способ)</a>"
    btn3 = "<a href='/products/6?name=LG'>Продукты (3 способ)</a>"
    html = "<h2>{}</h2><br>{} {}<br><br>{}<br>{}<br>{}".format("Главная страница", menu1, menu2, btn1, btn2, btn3)
    return HttpResponse(html)


# О себе (2 способ)
def about(request):
    return HttpResponseRedirect("/contact")


# Контакты (3 способ)
def contact(request):

    # --- ВАЖНЫЕ МОМЕНТЫ ---
    # context - Переменная для передачи данных [Python] в [HTML шаблон]
    # Тип данных переменной "context" - это всегда словарь "dict"
    # Название [Ключей словаря] это будущие названия [Переменных в HTML]

    # Jinja2 - Шаблонизатор. Описание синтаксиса Python в HTML
    # static - Папка содержащая в основном "ФАЙЛЫ СТАТИЧЕСКИЕ" и "СSS ТАБЛИЦЫ СТИЛЕЙ"
    # media - Папка содержащая в основном "ФАЙЛЫ МЕДИА ДИНАМИЧЕСКИЕ"
    # templates - Папка содержит в основном ФАЙЛЫ ШАБЛОНОВ

    # Входные данные для шаблона
    name = "Вася"
    time = datetime.now()
    number = "+375(29)7776655"
    names = ["Осипов Егор", "Воробьева Рената"]

    # Способ для передачи данных из Python в HTML (через context)
    context = {"NUMBER": number, "NAME": name, "TIME": time, "NAMES": names, "AGE": 18}
    return render(request, "contact.html", context=context)


# Метод обработки "Страницы продуктов №1"
# [Способ 1. Передача ДАННЫХ через [интернет-адрес]
# Пример URL: http://127.0.0.1:8000/products/10/Nokia
def product_1(request, product_id, name):
    return HttpResponse("<h2>Продукт №{}. Название: {}</h2>".format(product_id, name))


# Метод обработки "Страницы продуктов №2"
# [Способ 2. Передача ДАННЫХ [по строке запроса]
# Пример URL: http://127.0.0.1:8000/products?product_id=8
def product_2(request):
    product_id = request.GET.get("product_id", "-")
    name = request.GET.get("name", "-")
    return HttpResponse("<h2>Продукт №{}. Название: {}</h2>".format(product_id, name))


# Метод обработки "Страницы продуктов №3"
# [Способ 3. Способ 1 + Способ 2]
# Пример URL: http://127.0.0.1:8000/products/6?name=LG
def product_3(request, product_id):
    name = request.GET.get("name", "-")
    return HttpResponse("<h2>Продукт №{}. Название: {}</h2>".format(product_id, name))