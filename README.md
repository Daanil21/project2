# Проект "Банковские операции"

## Описание:

Проект "Банковские операции" - это веб-приложение на Python для управления картами и счетами.

## Установка:

1. Клонируйте репозиторий:
```
git clone https://github.com/username/project2.git
```
2. Установите зависимости:
```
pip install -r requirements.txt
```
3. Создайте базу данных и выполните миграции:
```
python manage.py migrate
```

4. Запустите локальный сервер:
```
python manage.py runserver
```
## Использование:

1. Откройте приложение в вашем веб-браузере.
2. Создайте новый проект и начните добавлять задачи.
3. Назначайте сроки выполнения и приоритеты для задач, чтобы эффективно управлять проектами.

## Документация:

На данный момент есть функции:

1. Для маскировки карт/счетов [Функция 1](src/masks.py)
2. Для определенных карт/счетов с маскировкой [Функция 2](src/widget.py)
3. Для список словарей сортировка и поиск нужных строк [Функция 3](src/processing.py) 



## Лицензия:

Этот проект лицензирован по [лицензии MIT](LICENSE)