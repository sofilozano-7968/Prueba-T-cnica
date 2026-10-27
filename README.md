# Trycore Match API 🚀

API desarrollada con **FastAPI** para evaluar y calcular la compatibilidad (*match*) entre los perfiles de candidatos y los requerimientos de las vacantes laborales.

---

## 📋 Descripción

Esta aplicación analiza la información provista sobre un candidato y una vacante, calculando un puntaje (*score*) de 0 a 100 basado en:
* **Cobertura de habilidades (*skills*):** Porcentaje de coincidencia entre las habilidades requeridas y las del candidato.
* **Brecha de experiencia:** Diferencia en años respecto al mínimo requerido por la vacante.
* **Bonificación por tipo de contrato:** Puntos adicionales según el tipo de contratación propuesta (*indefinido*, *obra_laboral*, *prestación de servicios*).

Además, clasifica el resultado en categorías (`NO_FIT`, `MAYBE`, `GOOD_FIT`, `EXCELLENT_FIT`) y proporciona una lista detallada con las razones del puntaje obtenido.

---

## 🛠️ Tecnologías Utilizadas

* **Python 3.13+**
* **FastAPI** (Framework web asíncrono)
* **Pydantic** (Validación de datos y esquemas)
* **Uvicorn** (Servidor ASGI)

---

## ⚙️ Instalación y Configuración Local

1. **Clona el repositorio:**
   ```bash
   git clone [https://github.com/sofilozano-7968/Prueba-T-cnica.git](https://github.com/sofilozano-7968/Prueba-T-cnica.git)
   cd trycore-match
