# Приложение дял управления движением денежных средств (ДДС) 

Django-приложение для управления финансовыми справочниками с

---

## Возможности

- Отображение всех транзакций и фильтрация по ним
- Управление транзакциями (CRUD)
- Управление справочниками (CRUD):
  - Типы
  - Категории
  - Подкатегории
  - Статусы
- Динамическое обновление интерфейса через JavaScript (fetch/AJAX)
- Интерфейс на вкладках (tabs)
- REST API на Django REST Framework (для справочников)

---

## Технологии

- Python 3.13
- Django 6.x
- Django REST Framework
- PostgreSQL
- JavaScript 
- Bootstrap 5

## Структура app
finance/
├── models.py
├── forms.py
├── views.py
├── views_api.py
├── serializers.py
├── urls.py
├── api_urls.py

## Установка 

git clone https://github.com/CodingNinja619/test_finance_task_django.git
cd test_finance_task_django
python -m venv .venv

### Linux / Mac
source venv/bin/activate

### Windows
venv\Scripts\activate

### Установить зависимости
pip install -r requirements.txt

### Миграции
python manage.py migrate
python manage.py createsuperuser

### Запуск
python manage.py runserver

## API
Доступные endpoints:
/api/types/
/api/statuses/
/api/categories/
/api/subcategories/