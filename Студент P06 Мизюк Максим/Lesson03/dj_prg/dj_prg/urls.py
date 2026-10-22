from django.contrib import admin
from django.urls import path
from dj_app import views  # Подключили urls файл views


# -- 1. Объяснение создания маршрута --
# EN - path('admin/', admin.site.urls),
# RU - ФункцияСозданияМаршрута(URL, МетодОбработкиURL, ИмяМаршрута)

# -- 2. Объяснение динамической части --
# PATH: Динамическое место в URL - <int:product_id> <ТипДанных:ИмяПеременной>
# Возможные типы: str, int, slug, uuid, path
# Пример: path('product/<int:product_id>/<str:name>')

# RE_PATH: Динамическое место в URL - (?P<name>\D+) (?P<ИмяПеременной>ТипДанных)
# Возможные типы: str - "\D+", int - "\d+"
# Пример: re_path(r'^product/(?P<product_id>\d+)/(?P<name>\D+)$')

# --- 3. Передача данных может быть 2-умя способами: ---
# 1. Передача ДАННЫХ через [интернет-адрес] - http://127.0.0.1:8000/products/10/Nokia
#    Данные будут находиться: В аргументах метода обработки URL
# 2. Передача ДАННЫХ [по строке запроса] - http://127.0.0.1:8000/products?product_id=8&name=Samsung
#    Данные будут находиться: В первом аргументе "request" метода обработки URL - request.GET.get()

urlpatterns = [

    # --- СТАТИЧНЫЕ МАРШРУТЫ ---

    path('admin/', admin.site.urls),  # Админа
    path('', views.index, name="index"),  # Главная
    path('about', views.about, name="about"),  # О себе
    path('contact', views.contact, name="contact"),  # Контакты

    # --- ДИНАМИЧЕСКИЕ МАРШРУТЫ ---

    # [Способ 1. Передача ДАННЫХ через [интернет-адрес]
    # Пример URL: http://127.0.0.1:8000/products/10/Nokia
    path('products/<int:product_id>/<str:name>', views.product_1, name="product_1"),  # Одно и тоже (#1)
    # re_path(r"^products/(?P<product_id>\d+)/(?P<name>\D+)$", views.product_1, name="product_1")  # Одно и тоже (#2)

    # [Способ 2. Передача ДАННЫХ [по строке запроса]
    # Пример URL: http://127.0.0.1:8000/products?product_id=8&name=Samsung
    path('products', views.product_2, name="product_2"),

]
