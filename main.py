from Funciones import nuevoTema, imprimirLista
from Clases import Padre, Hijo

# -----------------  variables
nuevoTema('variables')

print('hola mundo')
a = 5
print("a:", a)

b = 4.342
print('b:', b)

print("a, b:", a, b)

opcion = True
print('opcion:', opcion)

# -----------------  if-else
nuevoTema('instrucciones de control (if-else)')
c = 2

if c > 5:
    print('c es mayor a 5')
    # ESTE BLOQUE DE CÓDIGO NUNCA SE EJECUTA (PARA DEMOSTRAR QUE PYTHON ES UN LENGUAJE INTERPRETADO)
    kjsfdhflkjsdfhkljdhsdkjlfhsdkflhklhyetrtrey34
else:
    print('c NO es mayor a 5')

# -----------------  listas
nuevoTema('listas')
frutas = ['piñas', 'peras', 'manzanas', 'platanos']
print('frutas', frutas)

varios = ['zapatos', 3, 78.45, True, frutas]
print('varios: ', varios)

print('\n')
alumnos = ['Oswaldo', 'Carlos', 'Carolina', 'Johana', 'Karla', 'Alan', 'Alejandra', 'Eduardo', 'Luis']
imprimirLista(alumnos)

# Para agregar un elemento
alumnoFaltante = 'Marcos Aurelio'
alumnos.append(alumnoFaltante)
imprimirLista(alumnos)

# Para remover un elemento
alumnos.remove(alumnos[2])
imprimirLista(alumnos)

# -----------------  for
nuevoTema('Instrucciones de control - for')
for fruta in frutas:
    print(fruta)

# ---------------- Clases
nuevoTema('Clases')
juan = Padre('Juan', 24)
juan.quienSoy()
juan.trabajar()

pedro = Padre('Pedro', 40)
pedro.quienSoy()
pedro.trabajar()

print('-------------')
rigoberto = Hijo('Rigoberto', 23)
rigoberto.quienSoy()
rigoberto.trabajar()

