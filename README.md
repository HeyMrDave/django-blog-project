# 📝 Blog con Django

Este es un proyecto básico de **Blog** desarrollado con el framework [Django](https://www.djangoproject.com/).  
Forma parte de mi aprendizaje en el stack **backend con Python**.

## 📌 Funcionalidades
- Crear, editar, borrar y listar artículos (CRUD).
- Organización por categorías (**relación uno a muchos**).
- Página de detalle de cada artículo con URL dinámica basada en `slug`.
- Interfaz con **Bootstrap** para un diseño sencillo.
- (Opcional) Subida de imagen de portada para los artículos.
- (Opcional) Búsqueda de artículos por título.

## 🛠️ Tecnologías utilizadas
- [Python 3.x](https://www.python.org/)
- [Django 5.x](https://docs.djangoproject.com/)
- SQLite (base de datos por defecto)
- HTML, CSS y Bootstrap para la interfaz

## 🚀 Instalación y uso

1. Clonar este repositorio:
   ```bash
   git clone https://github.com/HeyMrDave/django-blog-project.git
2. Crear y activar un entorno virtual:

python -m venv venv
source venv/bin/activate   # En Linux/Mac
venv\Scripts\activate      # En Windows


3. Instalar dependencias:

pip install django
pip install Pillow # Para la subida de imagenes


4. Aplicar migraciones:

python manage.py migrate


5. Crear un superusuario (opcional, para acceder al admin):

python manage.py createsuperuser


6. Ejecutar el servidor de desarrollo:

python manage.py runserver


7. Abrir en el navegador:

http://127.0.0.1:8000/

📂 Estructura del proyecto
blog-django/
│── blog/            # Aplicación principal
│── templates/       # Archivos HTML
│── static/          # Archivos CSS/JS
│── db.sqlite3       # Base de datos
│── manage.py        # Script principal de Django

🎯 Objetivo de aprendizaje

Este proyecto fue desarrollado con el propósito de:

Practicar fundamentos de Django (CRUD, modelos, vistas y plantillas).

Comprender relaciones entre modelos en bases de datos.

Implementar una página de detalle con URL dinámica usando slugs.

Publicar un proyecto completo en GitHub como portafolio.

👨‍💻 Desarrollado por David Cabezas
