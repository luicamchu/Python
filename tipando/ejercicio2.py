from typing import NamedTuple, List, Dict, Any

Estudiante = NamedTuple("Estudiante", [("id", int), ("nombre", str), ("cursos", List[str])])
Curso = NamedTuple("Curso", [("codigo", int), ("nombre", str), ("estudiantes", List[int])])

estudiantes: List[Estudiante] = []
cursos: List[Curso] = []

inscripciones: Dict[int, Any] = {}

def agregar_estudiante(id:int, nombre: str) -> None:
    estudiante = Estudiante(id, nombre, [])
    estudiantes.append(estudiante)

def agregar_curso(codigo:int, nombre: str) -> None:
    curso = Curso(codigo, nombre, [])
    cursos.append(curso)

def 