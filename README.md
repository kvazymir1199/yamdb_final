<<<<<<< develop

# api_final

## Authors:

[dazdik](https://github.com/dazdik)

[FedOK007](https://github.com/FedOK007)

[kvazymir1199](https://github.com/kvazymir1199)

## Discription:

### REST API для YaMDb

Created on the basis of the framework [Django REST Framework (DRF)](https://github.com/ilyachch/django-rest-framework-rusdoc)

> The YaMDb project collects user reviews of works. The works are divided into categories: "Books", "Films", "Music".
>
> The works themselves are not stored in YaMDb, you can't watch a movie or listen to music here.
>
> In each category there are works: books, movies or music.
>
> A work can be assigned a genre from the preset list (for example, "Fairy Tale", "Rock" or "Arthouse").
>
> Grateful or outraged users leave text reviews for the works and rate the work, an average rating of the work is formed from user ratings.

## Technologies

Python 3.7

Django 3.2.15

## Start Project

Clone the repository and go to it on the command line:

```
git@github.com:kvazymir1199/api_yamdb.git
```

Пo to the project directory

```go
cd api_yamdb
```

Create and activate a virtual environment:

```
python -m venv venv
```

```
source venv/Scripts/activate
```

```
python -m pip install --upgrade pip
```

Install dependencies from requirements.txt:

```
pip install -r requirements.txt
```

```
Запуск проекта в Docker

Для запуска приложения в контейнерах установите Docker на ваш компьютер (сервер).

Наполнение .env
Файл .env должен находится в директории в директории infra.
Пример наполнения данного файла:

DB_ENGINE=django.db.backends.postgresql - # указываем, что работаем с postgresql
DB_NAME=postgres # указываем имя базы данных
POSTGRES_USER=postgres # задаем логин для подключения к базе данных
POSTGRES_PASSWORD=postgres # устанавливаем пароль для подключения к БД (установите свой)
DB_HOST=db # название сервиса (контейнера)
DB_PORT=5432 # порт для подключения к БД
После наполнения файла .env необходило изменить константу DATABASE файла settings.py
следующим образом:

DATABASES = {
    'default': {
        'ENGINE': os.getenv('DB_ENGINE'),
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('POSTGRES_USER'),
        'PASSWORD': os.getenv('POSTGRES_PASSWORD'),
        'HOST': os.getenv('DB_HOST'),
        'PORT': os.getenv('DB_PORT')
    }
}
Последовательность запуска приложения
Сборка контейнера. Перейдите в папку infra и выполните команду docker-compose для сборки и запуска контейнера:
docker-compose up -d --build
Запуск приложения api_yamdb. После сборки контейнеров необходимо выполнить следующие команды в терминале:
# Миграции
docker-compose exec web python manage.py migrate
# Создание суперпользователя
docker-compose exec web python manage.py createsuperuser
# Сбор статики
docker-compose exec web python manage.py collectstatic --no-input
# Резервное копирование данных из БД
docker-compose exec web python manage.py dumpdata > dump.json
python3 manage.py shell  
# выполнить в открывшемся терминале:
>>> from django.contrib.contenttypes.models import ContentType
>>> ContentType.objects.all().delete()
>>> quit()

python manage.py loaddata fixtures.json

> When you launch the project, at http://127.0.0.1:8000/redoc / documentation for the Yandex API will be available. The documentation describes how the API works. The documentation is presented in Doc format.

## Request examples

> Get (http://127.0.0.1:8000/api/v1/categories/1):

```

{
"name": "Film",
"slug": "Movie"
}

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

=======

Mironov Denis

Дарья Андреевна
```
https://github.com/kvazymir1199/yamdb_final>/actions/workflows/yamdb_workflow.yml/badge.svg