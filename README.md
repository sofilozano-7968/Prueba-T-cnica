# Trycore Match API 🚀

Microservicio desarrollado con **Python y FastAPI** para evaluar el nivel de compatibilidad (*match*) entre el perfil de un candidato y los requisitos de una vacante laboral.

La API calcula una puntuación teniendo en cuenta las habilidades, la experiencia laboral y el tipo de contrato.

## 📋 Características y reglas de negocio

La API evalúa tres factores para calcular el puntaje de compatibilidad:

1. **Cobertura de habilidades (70 puntos):** calcula la proporción de habilidades requeridas por la vacante que coinciden con las del candidato.
2. **Experiencia laboral (20 puntos):** asigna una puntuación según los años de experiencia faltantes frente al mínimo requerido.
3. **Tipo de contrato:** aplica una bonificación según el contrato seleccionado.

### Bonificaciones por tipo de contrato

- `indefinido`: +1 punto.
- `obra_laboral`: +5 puntos.
- `prestacion de servicios`: +0 puntos.

El puntaje se redondea al entero más cercano.

### Categorías de compatibilidad

- **`EXCELLENT_FIT`**: puntaje igual o superior a 85.
- **`GOOD_FIT`**: puntaje igual o superior a 65 e inferior a 85.
- **`MAYBE`**: puntaje igual o superior a 40 e inferior a 65.
- **`NO_FIT`**: puntaje inferior a 40.

La puntuación máxima con la fórmula actual es de 91 puntos para un contrato indefinido.

## 🛠️ Tecnologías utilizadas

- Python
- FastAPI
- Pydantic
- Uvicorn
- Pytest
- HTTPX

## 📁 Estructura del proyecto

```text
Prueba-T-cnica/
├── main.py
├── test_main.py
└── README.md
```

- `main.py`: contiene la API, los modelos de datos y la lógica de cálculo del match.
- `test_main.py`: contiene las pruebas automatizadas para verificar el funcionamiento del proyecto.
- `README.md`: contiene la documentación y las instrucciones de instalación y ejecución.

## ⚙️ Instalación y ejecución

### 1. Requisitos previos

Debes tener instalado:

- Python 3.10 o superior.
- Git.
- pip.

### 2. Clonar el repositorio

Ejecuta el siguiente comando en la terminal:

```bash
git clone https://github.com/sofilozano-7968/Prueba-T-cnica.git
```

### 3. Ingresar a la carpeta del proyecto

```bash
cd Prueba-T-cnica
```

### 4. Instalar las dependencias

Ejecuta:

```bash
pip install fastapi uvicorn pytest httpx
```

### 5. Iniciar el servidor

Ejecuta el siguiente comando:

```bash
uvicorn main:app --reload
```

Si el servidor inicia correctamente, la API estará disponible en:

http://127.0.0.1:8000

El parámetro `--reload` permite reiniciar automáticamente el servidor cuando se realizan cambios en el código.

Para detener el servidor, presiona `Ctrl + C` en la terminal.

## 📖 Documentación de la API

FastAPI genera una documentación interactiva que permite probar los endpoints.

Abre en el navegador:

http://127.0.0.1:8000/docs

### Endpoint principal

**POST `/match`**

Recibe la información de un candidato y una vacante, y devuelve el resultado del cálculo de compatibilidad.



### Descripción de los campos de respuesta

- `score`: puntaje total de compatibilidad.
- `categoria`: clasificación del candidato según el puntaje.
- `razones`: lista de explicaciones del resultado.
- `cobertura_skills`: proporción de habilidades coincidentes.
- `brecha_experiencia`: cantidad de años que faltan para cumplir la experiencia mínima requerida.

## 🧪 Pruebas unitarias

El proyecto utiliza **Pytest** para ejecutar pruebas automatizadas que verifican la lógica de cálculo y el comportamiento de la API.

Para ejecutar las pruebas, abre una terminal en la carpeta del proyecto y ejecuta:

```bash
pytest -v
```

Las pruebas incluidas verifican:

- Compatibilidad excelente (`EXCELLENT_FIT`).
- Compatibilidad baja (`NO_FIT`).
- Compatibilidad media (`MAYBE`).
- Compatibilidad buena (`GOOD_FIT`).
- Experiencia superior a la mínima requerida.
- Vacantes sin habilidades requeridas.
- Funcionamiento del endpoint `/match`.
- Validación de campos obligatorios.
- Rechazo de tipos de datos inválidos.

Pytest mostrará el resultado de cada prueba en la terminal.

