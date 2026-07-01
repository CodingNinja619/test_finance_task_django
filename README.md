# Приложение дял управления движением денежных средств (ДДС) 

Django-приложение для управления финансовыми справочниками и карточками

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

---

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
- /api/types/
- /api/statuses/
- /api/categories/
- /api/subcategories/

---

## Скриншоты интерфейса

### Главная - отображение всех карточек (транзакций)
![Главная](/main_page.png)

### Фильтры на главной - фильтрация карточек (транзакций)
![Фильтры на главной](/filtered_transactions.png)

### Создание карточки (транзакции)
![Создание транзацкии](/create_transaction.png)

### Изменение карточки (транзакции)
![Измение карточки (транзакции)](/edit_transaction.png)

### Управление справочниками
![Управление справочниками](/directories_example.png)

### Пример REST API (все типы)
![Типы REST](/types_api.png)

### Пример REST API (один тип)
![Тип REST](/type_api.png)

### Пример REST API (все категории)
![Тип REST](/type_api.png)