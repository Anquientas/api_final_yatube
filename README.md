# api_final
## Описание


## Как запустить проект

#### Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/Anquientas/api_final_yatube.git
```

```
cd api_final_yatube
```

#### Cоздать и активировать виртуальное окружение (рекомендуется исопльзовать Python 3.9):

- для Linux:

```
python3 -m venv venv
```

```
source venv/bin/activate
```

- для Windows:

```
py -3.9 -m venv venv
```

```
source venv/Scripts/activate
```

#### Установить зависимости из файла requirements.txt:

- для Linux:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

- для Windows:

```
py -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

#### Выполнить миграции:

- для Linux:

```
python3 manage.py migrate
```

- для Windows:

```
py manage.py migrate
```

#### Запустить проект:

- для Linux:

```
python3 manage.py runserver
```

- для Windows:

```
py manage.py runserver
```

## Примеры

Документацию проекта можно изучть после запуска по адресу:

```
http://127.0.0.1:8000/redoc/
```
