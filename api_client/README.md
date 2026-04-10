# API Client en Python

## 📌 Descripción

Este proyecto es un cliente de API desarrollado en Python que consulta datos desde una API pública, procesa la información y genera un resumen en formato JSON.

## 🚀 Funcionalidades

* Consumo de API REST usando requests
* Procesamiento de datos (posts)
* Generación de resumen
* Guardado en archivo JSON
* Configuración mediante archivo YAML

## 🛠️ Tecnologías utilizadas

* Python 3
* requests
* JSON
* YAML

## 📦 Instalación

Clonar el repositorio:

```bash
git clone https://github.com/tu_usuario/backend-practice.git
cd backend-practice/api_client
```

Crear entorno virtual (opcional pero recomendado):

```bash
python3 -m venv venv
source venv/bin/activate
```

Instalar dependencias:

```bash
pip install requests pyyaml
```

## ▶️ Uso

Ejecutar el script:

```bash
python3 main.py
```

## 📊 Ejemplo de salida

```
Total de posts: 100

1 - titulo...
2 - titulo...
```

## ⚙️ Configuración

El archivo `config.yaml` permite modificar:

* URL de la API
* archivo de salida

## 📁 Salida

Se genera un archivo:

* `data.json` → contiene el resumen de datos

## 🧠 Aprendizajes

* Consumo de APIs REST
* Manejo de JSON
* Manejo de errores
* Uso de YAML para configuración

## 👨‍💻 Autor

Emmanuel Paniagua Hernández
