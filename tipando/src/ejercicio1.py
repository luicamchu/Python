from typing import List, Dict

estudiantes: List[Dict[int, str]] = []
cursos: List[Dict[str, str]] = []

inscripciones: Dict[int, List[str]] = {}

def agregar_estudiantes(id: int, nombre: str) -> None:
    estudiantes.append({"id":id, "nombre":nombre})

def agregar_curso(codigo: int, nombre: str) -> None:
    cursos.append({"codigo": codigo, "nombre": nombre})

def inscribir_estudiantes(id: int, codigo: str) -> None:
    if id not in inscripciones:
        inscripciones[id] = []
    inscripciones[id].append(codigo)

def mostrar_estudiantes() -> None:
    for e in estudiantes:
        print(f"El id: {e["id"]}, nombre: {e["nombre"]}")
    
#2 funciones mas


