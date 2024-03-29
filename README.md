# tree-menu-django

--- 

### Описание
Приложение Django, в котором с помощью tamplate tag 
реализовано древовидное меню, редактируемое в админинстрационной панели Django. Меню по названию можно отрисовать на любой странице Приложения, 
используя следующие теги:
```
{% load draw_menu %}
{% draw_menu 'main_menu' %}
```

### Технологии
* Python
* Django

### Запуск проекта

```shell
git clone git@github.com:danjoklion/django-tree-templatetag.git
cd django-tree-templatetag
python -m venv venv
venv/Scripts/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
python manage.py migrate
```
Для корректной работы приложения необходимо:
 * создать суперпользователя
```shell
python manage.py createsuperuser
```
 * создать меню и его элементы через административную панель.

Запустить сервер разработки
```shell
python manage.py runserver
```
