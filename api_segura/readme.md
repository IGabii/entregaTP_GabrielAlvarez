# API de Productos

Este proyecto implementa una API REST para gestionar productos. Permite crear, listar, editar y eliminar registros desde una interfaz web o mediante peticiones JSON.

## Tecnologías
- Python 3.14
- Django 5.2
- Django REST Framework
- SQLite

## Modelo
El modelo `Producto` incluye:
- nombre (mínimo 3 caracteres)
- descripción
- precio (mayor a cero)
- disponible (booleano)
- fecha_creación (automática)

## Endpoints
- `GET /api/productos/` → lista de productos
- `POST /api/productos/` → crear producto
- `GET /api/productos/<id>/` → detalle
- `PUT /api/productos/<id>/` → editar
- `DELETE /api/productos/<id>/` → eliminar

## Validaciones
- El precio no puede ser menor o igual a cero
- El nombre debe tener al menos 3 caracteres

## Uso
1. Activar entorno virtual
2. Ejecutar `python manage.py runserver`
3. Acceder a `http://127.0.0.1:8000/api/productos/`


