import csv
from typing import NamedTuple,List,Set,Tuple,Dict,Optional
from datetime import datetime,date

Commit = NamedTuple("Commit",
    [("id", str), # Identificador alfanumérico del commit
    ("mensaje", str), # Mensaje asociado al commit
    ("fecha_hora", datetime) # Fecha y hora en la que se registró el commit
])
Repositorio = NamedTuple("Repositorio",
    [("nombre", str), # Nombre del repositorio
    ("propietario", str), # Nombre del usuario propietario
    ("lenguajes", Set[str]), # Conjunto de lenguajes usados
    ("privado", bool), # Indica si es privado o público
    ("commits", List[Commit]) # Lista de commits realizados
])

def lee_repositorios(csv_filename: str) -> List[Repositorio]:
    repositorios = []
    with open(csv_filename, encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        for nombre, propietario, lenguajes, privado, commits in reader:
            commits = parse_commits(commits)
            lenguajes = parse_lenguajes(lenguajes)
            privado = parse_bool(privado)
            repositorio = Repositorio(nombre, propietario, lenguajes, privado, commits)
            repositorios.append(repositorio)
    return repositorios

def parse_lenguajes(lenguajes_str: str) -> Set[str]:
    return set(lenguajes_str.split(','))

def parse_bool(privado_str: str) -> bool:
    res = None
    privado = privado_str.lower()
    if privado == "true":
        res = True
    elif privado == "false":
        res = False
    return res

def parse_commits(commits_str: str) -> List[Commit]:
    commits_str= commits_str.replace("[","").replace("]","").strip()
    res = []
    if len(commits_str) > 0:
        commits_list = commits_str.split(";")
        res = [parse_commit(commit) for commit in commits_list]
    return res

def parse_commit(commit_str: str) -> Commit:
    id, mensaje, fecha_hora_str = commit_str.split('#')
    return Commit(
        id = id.strip(),
        mensaje = mensaje.strip(),
        fecha_hora = parse_fecha_hora(fecha_hora_str)
    )

def parse_fecha_hora(fecha_hora_str: str) -> datetime:
    return datetime.strptime(fecha_hora_str, "%Y-%m-%d %H:%M:%S")