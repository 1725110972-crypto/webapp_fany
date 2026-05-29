# Demo de una Webapp con Python3, Web.py y Sqlite3

## 1. Crear un ambiente virtual (Virtual Environment)

Crear un virtual environment para instalar las librerias necesarias de Python.

```` shell 
python3 -m venv .venv

````

## 2. Iniciar en Virtual Environment
Iniciar el virtual environment para instalar las librerias necesarias para el proyeto.

```` shell 
source .venv/bin/activate
````

## 3. Actualizar **PIB**
Actualizar el instalador de paquetes de Python **PIB** es la actualización

```` shell 
pip install --upgrade pip
````

## 4. instalar el mircro-framework **web.py**
Instalar el *mircro-framework* **web.py** para la creación de Aplicaciones Web utilizando Python.(Cheetah servidor web que instalaremos)

```` shell 
pip install web.py
````

## 5. Crear el archivo **requirements.txt**
Crear el archivo **requirements-txt** con la lista de las lobrerias y versiones de cada una, necesarias para el proyecto.(version de libreria)

```` shell
pip freeze > requirements.txt
````

## 6. Crear el archivo **runtime.txt**
Crear el archivo **runtime.txt** con la version de Python3 utilizada.(mandamelo al archivo runtime)

```` shell
python3 -V > runtime.txt
````

## 7. Crear el archivo **.gitignore**
Crear el archivo **.gitignore** para indicar las carpetas y archivos que no se vana sincronizar con el repositorio.

```` shell
*.pyc
__pycache__/
.venv/
````

## 8. Indexar las carpetas y archivos
Indexar las carpetas y archivos creados o modificados

```` shell
git add .
````

## 9. Crear el punto de control **commit**
Crear el punto den control con los cambios realizados el proyecto.


```` shell
git commit -m "CREATED configuración de la virtual environment"
````

## 10. Sincronizar los cambios al repositorios 
Sincronizar los cambiios realizados al proyecto con el repositorio.

```` shell
git push -u origin main
````
