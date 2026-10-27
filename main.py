from typing import Literal

from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field 

app = FastAPI(title="Trycore Match API")

class Candidato(BaseModel):
    skills: list[str]
    experiencia_anios: int = Field(..., ge=0)

class Vacante(BaseModel):
    skills_requeridas: list[str]
    experiencia_min: int = Field(ge=0)
    tipo_contrato: Literal[
        "indefinido", "obra_laboral",
        "prestacion de servicios"
    ]

class Solicitud(BaseModel):
    candidato: Candidato
    vacante: Vacante

@app.exception_handler(RequestValidationError)
async def error_validacion(request: Request , exc:
RequestValidationError):
    error = exc.errors()[0]
    campo = str(error.get("loc")[-1])
    mensaje = (
        f"campo  {campo } requerido"
        if error ["type"] == "missing"
        else f"tipo de dato invalido para el campo {campo}"
    )
    return JSONResponse(status_code=400, content={"error": mensaje})

def calcular_match(candidato: Candidato, vacante: Vacante):
    requeridas = set(vacante.skills_requeridas)
    coincidencias  = len(set(candidato.skills) & requeridas)
    cobertura = coincidencias / len(requeridas) if requeridas else 1.0

    brecha_experiencia = max(0, vacante.experiencia_min - candidato.experiencia_anios)

    bono = {
            "indefinido": 1.0,
            "obra_laboral": 5,
            "prestacion de servicios": 0
        } [vacante.tipo_contrato]

    score = round(
            cobertura * 70 + max(0, 1 - brecha_experiencia / 5) * 20 + bono 
        )

    if score < 40:
        categoria = "NO_FIT"
    elif score < 65:
        categoria = "MAYBE"
    elif score < 85:
        categoria = "GOOD_FIT"
    else:
        categoria = "EXCELLENT_FIT"

    razones = [
        f"Coincide en {coincidencias} de {len(requeridas)} skills"
        if requeridas else "La vacante no requiere skills : cobertura 100%",
        f"Brecha de experiencia: {brecha_experiencia} años",
        f"Bonificación por tipo de contrato: {bono} puntos"
    ]

    return {
            
            "score": score,
            "categoria": categoria,
            "razones": razones,
            "cobertura_skills": cobertura,
            "brecha_experiencia": brecha_experiencia,
            }

@app.post("/match")
def match(solicitud: Solicitud):
    return calcular_match(solicitud.candidato, solicitud.vacante)































