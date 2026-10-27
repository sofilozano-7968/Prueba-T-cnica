
from fastapi.testclient import TestClient
from main import app, Candidato, Vacante, calcular_match

cliente = TestClient(app)


def evaluar(cs, ce, vs, ve, contrato):
    return calcular_match(
        Candidato(skills=cs, experiencia_anios=ce),
        Vacante(
            skills_requeridas=vs,
            experiencia_min=ve,
            tipo_contrato=contrato
        )
    )


def test_excellent_fit():
    r = evaluar(
        ["python", "sql"], 5,
        ["python", "sql"], 3,
        "indefinido"
    )
    assert r["score"] == 91
    assert r["categoria"] == "EXCELLENT_FIT"


def test_no_fit():
    r = evaluar(
        [], 0,
        ["python", "sql", "java"], 10,
        "indefinido"
    )
    assert r["categoria"] == "NO_FIT"


def test_maybe():
    r = evaluar(
        ["python"], 5,
        ["python", "sql", "java"], 5,
        "prestacion de servicios"
    )
    assert r["categoria"] == "MAYBE"
    assert r["score"] == 43


def test_good_fit():
    r = evaluar(
        ["python", "sql", "java"], 3,
        ["python", "sql", "java", "html"], 5,
        "indefinido"
    )
    assert r["categoria"] == "GOOD_FIT"


def test_experiencia_superior():
    r = evaluar(
        ["python"], 8,
        ["python"], 3,
        "indefinido"
    )
    assert r["brecha_experiencia"] == 0


def test_skills_vacias():
    r = evaluar(
        ["python"], 2,
        [], 2,
        "indefinido"
    )
    assert r["cobertura_skills"] == 1.0


def test_endpoint():
    r = cliente.post("/match", json={
        "candidato": {
            "skills": ["python"],
            "experiencia_anios": 2
        },
        "vacante": {
            "skills_requeridas": ["python"],
            "experiencia_min": 2,
            "tipo_contrato": "indefinido"
        }
    })

    assert r.status_code == 200
    assert "score" in r.json()
    assert len(r.json()["razones"]) == 3


def test_campo_faltante():
    r = cliente.post("/match", json={
        "candidato": {
            "skills": []
        },
        "vacante": {
            "skills_requeridas": [],
            "experiencia_min": 0,
            "tipo_contrato": "indefinido"
        }
    })

    assert r.status_code == 400
    assert "error" in r.json()


def test_tipo_invalido():
    r = cliente.post("/match", json={
        "candidato": {
            "skills": [],
            "experiencia_anios": "muchos"
        },
        "vacante": {
            "skills_requeridas": [],
            "experiencia_min": 0,
            "tipo_contrato": "indefinido"
        }
    })

    assert r.status_code == 400
