# API de Tareas con FastAPI

## 📌 Descripción

API REST desarrollada con FastAPI que permite gestionar tareas mediante operaciones CRUD.

## 🚀 Funcionalidades

* Crear tareas
* Listar tareas
* Actualizar tareas
* Eliminar tareas
* Persistencia en archivo JSON
* Validación con Pydantic

## 🛠️ Tecnologías

* Python
* FastAPI
* Pydantic
* JSON
* YAML

## 📦 Instalación

```bash
git clone https://github.com/tu_usuario/tu_repo.git
cd proyecto_api
```

Instalar dependencias:

```bash
pip install fastapi uvicorn pyyaml
```

## ▶️ Ejecución

```bash
uvicorn main:app --reload
```

Abrir en navegador:

* http://127.0.0.1:8000/docs

## 🔗 Endpoints

### GET /tareas

Obtiene todas las tareas

### POST /tareas

Crea una tarea

```json
{
  "titulo": "Ejemplo"
}
```

### PUT /tareas/{id}

Actualiza una tarea

### DELETE /tareas/{id}

Elimina una tarea

## 🧪 Pruebas

Se realizaron pruebas utilizando Postman mediante una colección con todos los endpoints.

## 📁 Persistencia

Los datos se almacenan en `data.json`

## 👨‍💻 Autor

Emmanuel Paniagua Hernández
