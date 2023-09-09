def nuevoTema(tema):
    print("=================" , tema, "===============")

def imprimirLista(alumnos):
    print('------------------')
    print('alumnos', alumnos)
    print('alumnos[4]: ', alumnos[4])  # Selecciona el objeto con índice 4
    print('alumnos[1:3]:', alumnos[1:3])  # Selecciona el objeto desde el 1 hasta el 2
    print('alumnos[:]:', alumnos[:])  # Dame todos los alumnos
    print('alumnos[-1]:', alumnos[-1])  # Dame el último elemento de la lista
    print('alumnos[-2]:', alumnos[-2])  # Dame el penultimo elemento de la lista
    print('alumnos[1:8:2]', alumnos[1:8:2])  # Dame los elementos del 1 al 7 pero con un salto del 2
