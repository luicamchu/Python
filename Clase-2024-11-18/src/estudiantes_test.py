from estudiantes import *
# TEST #
if __name__ == "__main__":
    print ("\n<<< **** INICIO TEST **** >>>\n")
    
    # Añadir 3 estudiantes de forma aleatoria:
    añadir_estudiante(obtenerDatosEstudianteAleatorio())
    añadir_estudiante(obtenerDatosEstudianteAleatorio())
    añadir_estudiante(obtenerDatosEstudianteAleatorio())
    
    # Mostras las fichas escolares:
    mostrarIterable(fichasEstudiantes, "Fichas de Estudiantes:")
    # Mostrar los nombres de estudiantes:
    mostrarIterable(obtenerNombresEstudiantes(ordenado=True), "Nombres de Estudiantes:")
    # Añadir todas las asignaturas a los estudiantes:
    for a in get_args(Asignaturas): # Asignaturas es un Literal
        for n in listadoEstudiantes.keys(): # listadoEstudiantes es un diccionario
            añadir_asignatura(n, a)
    # Añadir los examenes a todas las asignaturas de todos los estudiantes:
    for n in listadoEstudiantes.keys(): # listadoEstudiantes es un diccionario
        for a in listadoEstudiantes[n].keys(): # listadoEstudiantes[n] es un diccionario
            for e in get_args(Examenes): # Examenes es un Literal
                registrar_examen(n, a, e)
    # Añadir las calificaciones a todos los examenes a todas las asignaturas de todos los estudiantes:
    for n in listadoEstudiantes.keys(): # listadoEstudiantes es un diccionario
        for a in listadoEstudiantes[n].keys(): # listadoEstudiantes[n] es un diccionario
            for e in listadoEstudiantes[n][a].keys(): # listadoEstudiantes[n][a] es un diccionario
                registrar_calificacion(n, a, e, fechaAleatoria(), Fraction(randint(0,10), randint(1,10)))
    # Añadir ausencias en asignaturas de estudiantes de forma aleatoria
    for n in listadoEstudiantes.keys():
        for i in range(randint(0,5)):
            registrar_ausencia(n, choice(get_args(Asignaturas)), fechaAleatoria())
    print ("."*80)
    # Mostrar listado de estudiantes y asignaturas
    print(f"\nInformación de Estudiantes y Asignaturas:\n")
    mostrarListadoEstudiantes()
    print ("\n"+"."*80)
    # Mostrar listado de ausencias de estudiantes y asignaturas
    print(f"\nInformación de ausencias de Estudiantes y Asignaturas:\n")
    mostrarAusencias()
    print(f"\n\tEstudiantes con más ausencias: {estudiante_con_mas_ausencias()}")
    for a in get_args(Asignaturas):
        print(f"\t\tEstudiantes con más ausencias en {a}: {estudiante_con_mas_ausencias(asignatura=a)}")
    print(f"\n\tEstudiantes con más ausencias desde Octubre/2024: {estudiante_con_mas_ausencias(asignatura=None,
    fDesde=date(2024,10,1), fHasta=None)}")
    for a in get_args(Asignaturas):
        print(f"\t\tEstudiantes con más ausencias desde Octubre/2024 en {a}: {estudiante_con_mas_ausencias(asignatura=a, fDesde=date(2024,10,1), fHasta=None)}")
    print ("\n"+"."*80)
    print("\nInformación sobre el mejor examen por Estudiante:")
    for n in listadoEstudiantes.keys():
        print(f"\n\tEstudiante {n}: {mejorExamenEstudiante(n)}. \n\tDesglose por asignatura:")
    for e in listadoEstudiantes[n].keys():
        print(f"\t\t{mejorExamenEstudiante(n, e)}")
    print ("\n"+"."*80)
    # Mostrar promedios de calificaciones de la asignatura y de los estudiantes por asignatura
    print ("\nPromedios de calificaciones:\n")
    for n in listadoEstudiantes.keys():
        for a in listadoEstudiantes[n].keys():
            print(f"\tPromedio de la asignatura {a}: {redondearDecimales(promedio_asignatura(a))}")
            print(f"\t\tPromedio de {n} en esta asignatura: {redondearDecimales(promedio_estudiante_asignatura(n,
    a))}\n")
    print ("\n<<< **** FIN TEST **** >>>\n")
