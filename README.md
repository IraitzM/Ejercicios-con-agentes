# Proyecto Geometry

Este proyecto presenta varias opciones de agentes de cara a entender cómo estos funcionan e interactúan entre sí.

## Estructura del Proyecto

### Módulos Principales

1. **app.py**
   - Punto de entrada principal de la aplicación
   - Implementa la interfaz de usuario con Streamlit
   - Gestiona el historial de chat y la interacción del usuario

2. **agents.py**
   - Implementa los agentes

3. **tools.py**
   - Contiene las herramientas a emplear por los agentes

## Tecnologías Utilizadas

- Python (>3.12)
- Streamlit para la interfaz de usuario
- LangChain para el framework de IA
- OpenAI GPT-4 como modelo de lenguaje
- Arquitectura basada en agentes

## Requisitos Previos

- Python 3.x
- Cuenta de OpenAI con acceso a GPT-4
- Variables de entorno configuradas (.env)

## Cómo Usar

1. Configurar las variables de entorno necesarias

Crearemos un fichero _.env_ con las credenciales necesarias para Open AI (podéis ver el fichero _.env.example_)

2. Instalar las dependencias:

Bien empleando `pip`
   ```bash
   pip install -r requirements.txt
   ```
O `uv`
   ```bash
   uv sync
   ```
3. Ejecutar la aplicación una vez activado el entorno:
   ```bash
   streamlit run app.py
   ```
4. Interactuar con el asistente a través de la interfaz web

## Ejemplos de Uso

- Calcular el área de un círculo: "¿Cuál es el área de un círculo con radio 5?"
- Calcular el área de un cuadrado: "¿Cuál es el área de un cuadrado con lado 4?"