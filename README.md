# yamdb api

[![API for YaMDB project workflow](https://github.com/bondarval/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg?branch=main)](https://github.com/bondarval/yamdb_final/actions/workflows/yamdb_workflow.yml)

[![Python](https://img.shields.io/badge/-Python-464646?style=flat-square&logo=Python)](https://www.python.org/)
[![Nginx](https://img.shields.io/badge/-NGINX-464646?style=flat-square&logo=NGINX)](https://nginx.org/ru/)
[![gunicorn](https://img.shields.io/badge/-gunicorn-464646?style=flat-square&logo=gunicorn)](https://gunicorn.org/)
[![docker](https://img.shields.io/badge/-Docker-464646?style=flat-square&logo=docker)](https://www.docker.com/)
[![GitHub%20Actions](https://img.shields.io/badge/-GitHub%20Actions-464646?style=flat-square&logo=GitHub%20actions)](https://github.com/features/actions)
[![Yandex.Cloud](https://img.shields.io/badge/-Yandex.Cloud-464646?style=flat-square&logo=Yandex.Cloud)](https://cloud.yandex.ru/)
[![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray)](https://www.django-rest-framework.org/)
[![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)](https://www.postgresql.org/)

## Discription:

### REST API для YaMDb

Создан на основе
фреймворка [Django REST Framework (DRF)](https://github.com/ilyachch/django-rest-framework-rusdoc)

Проект YaMDb собирает отзывы пользователей о работах. Работы разделены на категории: "Книги", "Фильмы", "Музыка".
Сами работы не хранятся в Imdb, вы не можете посмотреть фильм или послушать музыку здесь.
В каждой категории есть свои произведения: книги, фильмы или музыка.
Произведению можно присвоить жанр из предустановленного списка (например, "Сказка", "Рок" или "Артхаус").

Благодарные или возмущенные пользователи оставляют текстовые отзывы о работах и оценивают работу,
из оценок пользователей формируется средняя оценка работы.

## Technologies

- [Python 3.10](https://www.python.org/downloads/release/python-388/)
- [Django 3.2](https://www.djangoproject.com/download/)
- [Django Rest Framework 3.12.4](https://www.django-rest-framework.org/)
- [PostgreSQL 13.0](https://www.postgresql.org/download/)
- [gunicorn 20.0.4](https://pypi.org/project/gunicorn/)
- [nginx 1.21.3](https://nginx.org/ru/download.html)

# Контейнер
- [Docker 20.10.14](https://www.docker.com/)
- [Docker Compose 2.4.1](https://docs.docker.com/compose/)

# URL's
- http://84.252.137.228/api/v1
- http://84.252.137.228/admin
- http://84.252.137.228/redoc

## Start Project

### Clone the repository and go to it on the command line:

```
git@github.com:kvazymir1199/api_yamdb.git
```

### to the project directory

```
cd api_yamdb
```

### Create and activate a virtual environment:

```
python -m venv venv
```

```
source venv/Scripts/activate
```

```
python -m pip install --upgrade pip
```

### Install dependencies from requirements.txt:

```
pip install -r requirements.txt
```

### Get project in Docker

#### Для запуска приложения в контейнерах установите Docker на ваш компьютер (сервер).

Наполнение env
(Файл .env должен находится в директории в директории infra.)

1) Пример наполнения env файла:
    * DB_ENGINE=django.db.backends.postgresql
    * DB_NAME=postgres
    * POSTGRES_USER=postgres
    * POSTGRES_PASSWORD=postgres
    * DB_HOST=db
    * DB_PORT=5432
2) После наполнения файла .env необходило изменить константу DATABASE файла settings.py
   следующим образом:

    * DATABASES = {
        * 'default': {
            * 'ENGINE': os.getenv('DB_ENGINE'),
            * 'NAME': os.getenv('DB_NAME'),
            * 'USER': os.getenv('POSTGRES_USER'),
            * 'PASSWORD': os.getenv('POSTGRES_PASSWORD'),
            * 'HOST': os.getenv('DB_HOST'),
            * 'PORT': os.getenv('DB_PORT')
              }
              }
            *
3) Последовательность запуска приложения. Сборка контейнера:
    * Перейдите в папку infra и выполните команду docker-compose для сборки и запуска контейнера:
      docker-compose up -d --build
    * Запуск приложения api_yamdb. После сборки контейнеров необходимо выполнить следующие команды в терминале:
    * Миграции:

      ```docker-compose exec web python manage.py migrate```

    * Создание суперпользователя:

      ```docker-compose exec web python manage.py createsuperuser```

    * Сбор статики:

      ```docker-compose exec web python manage.py collectstatic --no-input```

    * Резервное копирование данных из БД:

      ```docker-compose exec web python manage.py dumpdata > dump.json```
    * Открыть терминал

      ```python3 manage.py shell```

    * выполнить в открывшемся терминале:
       ``` 
      from django.contrib.contenttypes.models import ContentType
      ContentType.objects.all().delete()
      quit()
      ```
    * Заполнить базу данных из файла с дампом:
      ```
      python manage.py loaddata fixtures.json
      ```

When you launch the project, at http://127.0.0.1:8000/redoc / documentation for the Yandex API will be available. The
documentation describes how the API works. The documentation is presented in Doc format.

## Request examples

**Get**: http://127.0.0.1:8000/api/v1/categories/1

``` 
[
  {
    "count": 0,
    "next": "string",
    "previous": "string",
    "results": [
      {
        "name": "string",
        "slug": "string"
      }
    ]
  }
]
```

**POST**: http://84.252.137.228/api/v1/categories/

Тело запроса:

```
{
  "name": "string",
  "slug": "string"
}
```

Пример ответа:

```
{
  "name": "string",
  "slug": "string"
}
```

**GET**: http://84.252.137.228/api/v1/users/

```
[
  {
    "count": 0,
    "next": "string",
    "previous": "string",
    "results": [
      {
        "username": "string",
        "email": "user@example.com",
        "first_name": "string",
        "last_name": "string",
        "bio": "string",
        "role": "user"
      }
    ]
  }
]
```

## Requirements:

```
asgiref==3.5.2
atomicwrites==1.4.1
attrs==22.1.0
certifi==2022.9.24
charset-normalizer==2.0.12
colorama==0.4.5
Django==2.2.16
django-filter==21.1
djangorestframework==3.12.4
djangorestframework-simplejwt==5.2.1
idna==3.4
importlib-metadata==4.13.0
iniconfig==1.1.1
packaging==21.3
pluggy==0.13.1
py==1.11.0
PyJWT==2.1.0
pyparsing==3.0.9
pytest==6.2.4
pytest-django==4.4.0
pytest-pythonpath==0.7.3
pytz==2022.4
requests==2.26.0
sqlparse==0.4.3
toml==0.10.2
typing_extensions==4.3.0
urllib3==1.26.12
zipp==3.8.1
```

## Authors:

* [kvazymir1199](https://github.com/kvazymir1199)
