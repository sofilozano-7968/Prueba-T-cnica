# Trycore Match API 🚀

Micro-servicio desarrollado con **FastAPI** para evaluar el nivel de compatibilidad (*match*) entre el perfil de un candidato y los requerimientos de una vacante laboral.

---

## 📋 Características y Reglas de Negocio

La API evalúa tres factores principales para calcular una puntuación de 0 a 100:
1. **Cobertura de skills (70%):** Porcentaje de habilidades del candidato que coinciden con las de la vacante.
2. **Brecha de experiencia (20%):** Penalización por los años faltantes respecto al mínimo requerido.
3. **Tipo de contrato (10%):** Bonificación según la contratación: `indefinido` (+10 pts), `obra_laboral` (+5 pts), `prestacion_servicios` (+0 pts).

### Categorización del Match:
* **`EXCELLENT_FIT`**: Score ≥ 85
* **`GOOD_FIT`**: 65 ≤ Score < 85
* **`MAYBE`**: 40 ≤ Score < 65
* **`NO_FIT`**: Score < 40

---

## ⚙️ Cómo Correr (Instalación y Ejecución)

1. **Clonar el repositorio:**
   ```bash
   git clone [https://github.com/sofilozano-7968/Prueba-T-cnica.git](https://github.com/sofilozano-7968/Prueba-T-cnica.git)
   cd trycore-match
