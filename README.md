# automatika_test

## Быстрый старт
> для запуска проекта требуется локально поднятый сервер postgres
1. Перейдите в корневую папку проекта
2. Установите зависимости командой ```pipenv install```
3. Активируйте виртуальное окружение при помощи ```pipenv shell```
4. Перейдите в директорию ivisit/ivisit
5. Создайте файл окружения для подключения к бд на основе .env.example
6. Поднимитесь в директорию с файлом manage.py
7. Подготовьте миграции командой ```python manage.py makemigrations```
8. Загрузите подготовленные миграции ```python manage.py migrate```
9. Загрузите тестовый датасет в бд ```python manage.py loaddata core/fixtures/dataset.json```
10. Создайте суперпользователя командой python ```manage.py createsuperuser```
11. Запустите проект ```python manage.py runserver```

## Доступный API
1. http://127.0.0.1:8000/api/visits 
2. http://127.0.0.1:8000/api/points
3. http://127.0.0.1:8080/admin
