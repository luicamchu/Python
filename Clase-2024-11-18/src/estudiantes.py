from faker import Faker
from fractions import Fraction
from random import randint, choice
from datetime import date, timedelta
from typing import Iterable, NamedTuple, List, Dict, Literal, NewType, Optional, Set, Tuple, TypeVar, get_args

# Se define una variable de tipo genérico T
T = TypeVar('T')

# Se define variable para generar faker
fake = Faker()

# Se definen otros tipos a partir de un tipo existente
Estudiante = str # Nombre del estudiante -> NewType ('Estudiantes', str)
Asignatura = str # Nombre de la asignatura -> NewType ('Asignatura', str)
Examen = str # Nombre del examen -> NewType ('Examen', str)
Calificacion = Fraction # Calificacion -> NewType ('Calificacion', Fraction)

# Se definen dos Literales con las Asignaturas (de un MBA) y los Exámenes
Asignaturas = Literal["Finanzas", "Emprendimiento", "Marketing"]
Examenes = Literal["escrito", "oral"]

# Se utilizan Tuplas para la Nota y la Ficha de Estudiante:
Nota = NamedTuple("Nota", [("fechaExamen", date), ("notaExamen", Calificacion)])
Ficha = NamedTuple("Ficha", [("nombre", Estudiante), ("edad", int), ("direccion", str)])

# Estructura de datos de Estudiantes, Ausencias y Fichas Escolares
listadoEstudiantes: Dict[Estudiante, Dict[Asignatura, Dict[Examen, List[Nota]]]] = {} 
# Contiene por estudiante, asignatura y examen, las Notas
ausenciasEstudiantes: Dict[Estudiante, Dict[Asignatura, Set[date]]] = {} 
# Contiene por estudiante y asignatura, las fechas de ausencias
fichasEstudiantes: List[Ficha] = []

# Implementar función para obtener datos de estudiantes de forma aleatoria
# Debe devolver la tupla Ficha con nombre, edad y dirección del Estudiante
def obtenerDatosEstudianteAleatorio() -> Ficha:
    nombreEstudiante = fake.name()
    edadEstudiante = randint(18, 99)
    direccionEstudiante = fake.address() + ", "+ fake.city() + ", " + fake.country()
    return Ficha(nombreEstudiante, edadEstudiante, direccionEstudiante)

# Implementar función para obtener una fecha anterior a hoy de forma aleatoria
# Debe devolver la fecha (date) obtenida
def fechaAleatoria() -> date:
    return date(randint(0000, date.year-1), randint(1, date.month-1), randint(1, date.day-1))

# Implementar función para redondear un número a n decimales (por defecto n=1)
# Esta función tiene como parámetro de entrada el número a redondear
# Debe devolver el número redondeado (float)
def redondearDecimales(num: float, n: int = 1) -> float:
    return round(num, n)

# Implementar función para añadir un estudiante en listadoEstudiantes, en ausenciasEstudiantes y en fichasEstudiantes
# Esta función tiene como parámetro de entrada una tupla con los datos del estudiante
# Si el estudiante ya existe mostrar un mensaje indicándolo.
# Devolver True si ha ido bien o False, en caso contrario.
def añadir_estudiante(fichaEstudiante: Ficha) -> bool:
    result: bool = False
    if fichaEstudiante.nombre not in listadoEstudiantes:
        listadoEstudiantes[fichaEstudiante.nombre] = {}
        if fichaEstudiante.nombre not in ausenciasEstudiantes:
                ausenciasEstudiantes[fichaEstudiante.nombre] = {}
                if fichaEstudiante.nombre not in fichasEstudiantes:
                        fichasEstudiantes.append(fichaEstudiante)
                        result = True
    else:
        print(f"El estudiante {fichaEstudiante.nombre} ya existe.")
    return result

# Implementar función para obtener solo los nombres de los estudiantes que aparecen en el diccionario listadoEstudiantes
# Esta función tiene 2 parámetros, uno que indica si listado ordenado y, otro, que indica orden (reverse)
# Debe devolver una lista con los nombres
def obtenerNombresEstudiantes(ordenado: bool = True, ordenReverse: bool = False) -> List[Estudiante]:
    # listado = [nombre for nombre in listadoEstudiantes.keys()]
    # result = sorted(listado) if ordenado else listado
    # return reversed(result) if ordenReverse else result
    return sorted(listadoEstudiantes, key=lambda x:x[0], reverse=ordenReverse) \
        if ordenado else [nombre for nombre in listadoEstudiantes.keys()]

# Implementar función para añadir en listadoEstudiantes y ausenciasEstudiantes una asignatura del estudiante
# Esta función tiene 2 parámetros, uno indica el nombre del estudiante y el otro el nombre de la asignatura
# Si el estudiante ya existe o la asignatura del estudiante ya existe, mostrar un mensaje indicándolo.
# Devolver True si ha ido bien o False, en caso contrario.
def añadir_asignatura(nombre: Estudiante, asignatura: Asignatura) -> bool:
    result: bool = False
    if nombre in listadoEstudiantes:
        if asignatura not in listadoEstudiantes[nombre]:
            listadoEstudiantes[nombre][asignatura] =  {}
        #if nombre in ausenciasEstudiantes:
        #    if asignatura not in ausenciasEstudiantes[nombre]:
            ausenciasEstudiantes[nombre][asignatura] = set()
            result = True
        else:
            print(f"La asignatura {asignatura} del estudiante {nombre} ya existe")
    else:
        print(f"El estudiante {nombre} no esxite.")
    return result
  
# Implementar función para registrar en listadoEstudiantes un examen de una asignatura del estudiante
# Esta función tiene 3 parámetros, el nombre del estudiante, el nombre de la asignatura y el examen
# Si el estudiante no existe o la asignatura del estudiante no existe o el examen de la asignatura del
# estudiante no existe, mostrar un mensaje indicándolo.
# Devolver True si ha ido bien o False, en caso contrario.
def registrar_examen(nombre: Estudiante, asignatura: Asignatura, examen: Examen) -> bool:
    result = False
    if nombre in listadoEstudiantes:
        if asignatura in listadoEstudiantes[nombre]:
            if examen not in listadoEstudiantes[nombre][asignatura]:
                listadoEstudiantes[nombre][asignatura][examen] = []
                res = True
            else:
                print(f"El examen {examen} ya existe para la asignatura {asignatura} del estudiante {nombre}")
        else:
            print(f"El estudiante {nombre} no tiene la asignatura {asignatura}")
    else:
        print(f"El estudiante {nombre} no esxite.")
    return result
# Implementar función para registrar, en listadoEstudiantes, una calificación de un examen de una
# asignatura de un estudiante
# Esta función tiene 4 parámetros, el nombre del estudiante, el nombre de la asignatura, el examen y la nota.
# Si el estudiante no existe o la asignatura del estudiante no existe o el examen de la asignatura no existe,
# mostrar un mensaje indicándolo.
# Devolver True si ha ido bien o False, en caso contrario.
def registrar_calificacion(nombre: Estudiante, asignatura: Asignatura, examen: Examen, \
fecha: date, nota: Calificacion) -> bool:
    res: bool = False
    if nombre in listadoEstudiantes:
        if asignatura in listadoEstudiantes[nombre]:
            if examen in listadoEstudiantes[nombre][asignatura]:
                listadoEstudiantes[nombre][asignatura][examen].append(Nota(fechaExamen=fecha, notaExamen=nota))
                res = True
    if not res:
        print(f"La combinación estudiante {nombre}, asignatura {asignatura} y examen {examen} no existe")
    return res

# Implementar función para registrar, en ausenciasEstudiantes, una ausencia de un estudiante a una asignatura
# Esta función tiene 3 parámetros, el nombre del estudiante, el nombre de la asignatura y la fecha de la ausencia.
# Si el estudiante no existe o la asignatura del estudiante no existe, mostrar un mensaje indicándolo.
# Devolver True si ha ido bien o False, en caso contrario.
def registrar_ausencia(nombre: Estudiante, asignatura: Asignatura, fecha: date) -> bool:
    res: bool = False
    if nombre in ausenciasEstudiantes:
        if asignatura in ausenciasEstudiantes[nombre]:
            ausenciasEstudiantes[nombre][asignatura].add(fecha)
        res = True
    if not res:
        print(f"El estudiante {nombre} o la asignatura {asignatura} no existen.")
    return res

# Implementar función para calcular el promedio de calificaciones de un estudiante y asignatura
# Esta función tiene 2 parámetros, el nombre del estudiante y la asignatura del estudiante
# Si el estudiante no existe o la asignatura del estudiante no existe, mostrar un mensaje indicándolo.
# Devolver la calificación (float) obtenida, en caso de obtener algún valor o None, en caso contrario.
def promedio_estudiante_asignatura(nombre: Estudiante, asignatura: Asignatura) -> Optional[float]:
    if nombre in listadoEstudiantes and asignatura in listadoEstudiantes[nombre]:
        total: List = []
        for calificaciones in listadoEstudiantes[nombre][asignatura].values():
            #total.extend([c.notaExamen for c in calificaciones])#añadiendo elementos a la lista
            total.extend([c[1] for c in calificaciones])#añadiendo elementos a la lista
        if total:
            return float(sum(total)/len(total))
    else:
        print(f"El estudiante {nombre} o la asignatura {asignatura} no existe.")
# Implementar función para calcular el promedio de calificaciones por asignatura
# Esta función tiene como parámetro el nombre de la asignatura
# Devolver la calificación (float) obtenida, en caso de obtener algún valor o None, en caso contrario.
def promedio_asignatura(asignatura: Asignatura) -> Optional[float]:
    asignaturaXnotas:dict = {}
    total: List = []
    for nombre in listadoEstudiantes.values():
        if asignatura in listadoEstudiantes[nombre][asignatura]:
            for calificaciones in listadoEstudiantes[nombre][asignatura].values():
                total.extend([cal for _, cal in calificaciones])
    if total:
        return float(sum(total)/len(total))
    
    return None
                
# Implementar función para obtener el examen con mejor calificación de un estudiante y asignatura del estudiante.
# Esta función tiene 2 parámetros, el nombre del estudiante y, opcionalmente, la asignatura.
# Chequear que el nombre del estudiante existe en listadoEstudiantes. Si no existe devolver una excepción.
# Devolver una tupla con el nombre de la asignatura, el examen y la calificación.
# En caso de no obtener ningún valor en la tupla, devolver None.
def mejorExamenEstudiante(nombre: Estudiante, asignaturaEstudiante: Asignatura|None = None) -> Optional[Tuple[Asignatura, Examen, Calificacion]]:
    if nombre not in listadoEstudiantes:
        raise(f"El estudiante {nombre} no existe.")
    mejorNota:Fraction = Fraction(0)
    mejorExamen:Tuple[Asignatura, Examen, Calificacion] = None
    
    for asignatura, examenes in listadoEstudiantes[nombre].items():
        if asignaturaEstudiante is None or asignaturaEstudiante == asignatura:#me vale para cualquier asignatura, incluso none, que no falle, que siga
            for examen, calificaciones in examenes.items():
                for c in calificaciones:
                    if c[1] > mejorNota:
                        mejorNota = c[1]
                        mejorExamen = (asignatura, examen, mejorNota)
    return mejorExamen
            
    
# Implementar función para obtener las ausencias de un estudiante.
# Esta función tiene 3 parámetros (todos opcionales): la asignatura, la fecha desde y la fecha hasta.
# Los parámetros se deben tener en cuenta al objeto de filtrar la información.
# Es decir, si estos no están informados (None), no se debe tener en cuenta.
# Devolver un conjunto con los nombres de los estudiantes. En caso de no obtener ningún nombre, devolver None.
def estudiante_con_mas_ausencias(asignatura: Asignatura|None = None, fDesde: date|None = None, \
fHasta: date|None = None) -> Optional[Set[Estudiante]]:
    numeroAusencias:int = 0
    numeroMaximoAusencias:int = 0
    res:Set[Estudiante] = set()
    fechaDesde:date = fDesde if fDesde is not None else date.min
    fechaHasta:date = fHasta if fHasta is not None else date.max
    
    

# Función para mostrar (print) toda la información almacenada en listadoEstudiantes
def mostrarListadoEstudiantes() -> None:
    for estudiante, asignaturas in listadoEstudiantes.items():
        print(f"> Estudiante: {estudiante}")
    for asignatura, examenes in asignaturas.items():
        print(f"\t- Asignatura: {asignatura}")
    for examen, calificaciones in examenes.items():
        print(f"\t\t. Examen: {examen} -> Calificaciones: {[Nota(fechaExamen=f, notaExamen=n) for f, n in
    calificaciones]}")
# Función para mostrar (print) toda la información almacenada en ausenciasEstudiantes
def mostrarAusencias() -> None:
    for n in listadoEstudiantes.keys():
        print(f"\tAusencias de {n}: {ausenciasEstudiantes[n]}")
# Función para mostrar (print) un iterable
def mostrarIterable(listado: Iterable, texto:str|None = None) -> None:
    if not listado:
        raise "No hay elementos a mostrar"
    print ("."*80)
    if texto.isprintable:
        print ("\n" + texto + "\n")
    if isinstance(listado, List) or isinstance(listado, Dict) or isinstance(listado, Tuple):
        for i, l in enumerate(listado):
            if isinstance(l, Tuple):
                print (str(l))
            else:
                print (str(i)+". "+str(l))
    else:
        print(listado)
    print ("\n")