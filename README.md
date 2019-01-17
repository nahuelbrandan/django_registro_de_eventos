# django_registro_de_eventos

**Autor** : Nahuel Brandan nahuelbrandan123@gmail.com

## Descripción:

Programa que nos permite agendar eventos.

Ejemplo:
![home](http://i64.tinypic.com/1zx9vlu.png)

## Prerequisitos

Utilizo python 3.7.1 y Django 2.1.4

## Instalación

* Creamos un entorno virtual ejecutando: *virtualenv -p python3 env*

* Ingresamos al entorno: *source env/bin/activate*

* Instalamos los requerimientos con: *pip install -r requirements.txt*

* Ejecutamos el script primera_vez para setear las configuraciones iniciales: *./primera_vez.sh*

* Ejecutamos *python manage.py migrate* para cargar los modelos creados.

* Corremos el proyecto con: *python manage.py runserver* y vamos a nuestro navegador e ingresamos a la url: *http://127.0.0.1:8000/*.
