from django.shortcuts import render
from dj_app.forms import *  # Импорт всех ФОРМ
from dj_app.models import *  # Импорт всех МОДЕЛЕЙ

# Главная страница
def index(request):

    # ЛОГИКА 1. [Клиент Обновил Страницу] - Когда клиент хочет посмотреть
    if request.method == "GET":
        form1 = UserForm()
        form2 = AuthorizationForm()
        context = {"form1": form1, "form2": form2}
        return render(request, "index.html", context=context)

    # ЛОГИКА 2. [Клиент Нажал Кнопку Войти] - Когда клиент что-то хочет отправить
    if request.method == "POST":

        data = []  # Список с правильными данными из формы

        # Автоматически берем нужные поля
        for key, value in request.POST.items():
            if key != "csrfmiddlewaretoken" and key != "country" and key != "flag":
                data.append([key, value])

        # Вручную добавляем Поле множественного выбора (Страна)
        list_country = request.POST.getlist("country")
        data.insert(4, ["country", list_country])

        # Вручную добавляем Поле флага
        flag = True if request.POST.get("flag") == "on" else False
        data.insert(2, ["flag", flag])

        form1 = UserForm()
        form2 = AuthorizationForm()
        context = {"form1": form1, "form2": form2}
        return render(request, "index.html", context=context)

    return None  # Заглушка чтобы PEP 8 не ругался


# Метод для работы с операциями БД
def operation(request):

    #  Прочитать какая кнопка была нажата для чтения (all / one / filter / update / delete)
    button = request.GET.get("button")
    print("Нажата была кнопка:", button)

    # ЛОГИКА 1. [Клиент Обновил Страницу] - Когда клиент хочет посмотреть
    if request.method == "GET":

        # ОПЕРАЦИЯ - ЧТЕНИЕ ВСЕХ
        if button == "all" or button is None:
            form = OperationsForm()
            person = Person.objects.all()
            context = {"FORM": form, "TABLE": person}
            return render(request, "operation.html", context=context)
        # ОПЕРАЦИЯ - ЧТЕНИЕ ОДНОГО
        if button == "one":
            form = OperationsForm()
            person = [Person.objects.get(pk=5)]
            context = {"FORM": form, "TABLE": person}
            return render(request, "operation.html", context=context)
        # ОПЕРАЦИЯ - ЧТЕНИЕ ФИЛЬТР
        if button == "filter":
            form = OperationsForm()
            person = Person.objects.filter(age=30)
            context = {"FORM": form, "TABLE": person}
            return render(request, "operation.html", context=context)
        # ОПЕРАЦИЯ - ЧТЕНИЕ ИСКЛЮЧЕНИЕ
        if button == "exclude":
            form = OperationsForm()
            person = Person.objects.exclude(age=30)
            context = {"FORM": form, "TABLE": person}
            return render(request, "operation.html", context=context)
        # ОПЕРАЦИЯ - УДАЛЕНИЕ
        if button == "delete":
            pk = request.GET.get("id")  # Получили ID элемента (для удаления)
            Person.objects.filter(pk=pk).delete()  # Удалили элемент по ID
            form = OperationsForm()
            person = Person.objects.all()
            context = {"FORM": form, "TABLE": person}
            return render(request, "operation.html", context=context)
        # ОПЕРАЦИЯ - ОБНОВЛЕНИЕ (1. Показ формы)
        if button == "update":
            pk = request.GET.get("id")  # Получили ID элемента (для обновления)
            form = OperationsForm()
            person = Person.objects.all()
            context = {"FORM": form, "TABLE": person, "PK": int(pk)}
            return render(request, "operation.html", context=context)


    # ЛОГИКА 2. [Клиент Нажал Кнопку Войти] - Когда клиент что-то хочет отправить
    if request.method == "POST":

        # ОПЕРАЦИЯ - ЗАПИСЬ
        if button == "write" or button is None or button == "all":
            name = request.POST.get("name")
            age = request.POST.get("age")
            Person.objects.create(name=name, age=age)
            form = OperationsForm()
            person = Person.objects.all()
            context = {"FORM": form, "TABLE": person}
            return render(request, "operation.html", context=context)
        # ОПЕРАЦИЯ - ОБНОВЛЕНИЕ (2. Изменение данных в БД)
            if button == "update":
                pass

    return None  # Заглушка чтобы PEP 8 не ругался