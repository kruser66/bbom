# Тестовое задание

* Создать веб-приложение на Django, которое будет отображать список пользователей и их посты,  
а также позволять добавлять и удалять посты.

* Создание API: Создайте несколько API-конечных пунктов. Первый должен возвращать список всех пользователей, второй - список всех постов конкретного пользователя, третий - добавление нового поста, четвертый - удаление существующего поста

## Как установить

Python 3 должен быть установлен.

- Скачать проект.
- Создать виртуальное окружение.

```bash
python -m venv venv
```

- Установить зависимости.

```bash
pip install -r requirements.txt
```

- Накатить миграции.

```bash
python manage.py migrate
```

- Создать суперпользователя.

```bash
python manage.py createsuperuser
```

## Запуск проекта

### Установить переменные окружения

- для развертывания Django Вам понадобятся перемнные окружения (для тестирования они приписаны по-умолчанию)

```python
SECRET_KEY=YOUR_SECRET_KEY
ALLOWED_HOSTS=YOUR_HOST_NAME_OR_ADDRESS
```

### Старт проекта

```bash
python manage.py runserver
```

Сайт будет доступен по адресу: `http://127.0.0.1:8000/`

API (ипользуется стандартный интефейс DRF):

* Получить всех пользователей `GET /api/users`
* Получить посты пользователя `GET /api/posts`
* Просмотр поста `GET /api/posts/<id>`
* Изменить пост `PUT /api/posts/<id>`
* Удалить пост `DELETE /api/posts/<id>`

## Цель проекта

Тестовое задание на вакансию "Python разработчик (Django)"
