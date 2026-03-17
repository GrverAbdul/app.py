####################################################################################
####################################################################################
## ESTUDIANTE: GROVER ABDUL MAMANI SANGA
## holamundo->app.py
####################################################################################
####################################################################################


print("Hola mundo desde Python!!")

#variables en python

#enteros
edad = 20
#float
precio = 50.5
#Strings
nombre = "Bruno Diaz"
#Booleanos
bandera = True

#SALIDA
print("Nombre: ", nombre)
print("Edad: ", edad)
print("Precio: " + str(precio))

#Entradas
nombre = input("INTRODUCE TU NOMBRE: ")
print("Hola "+nombre)

########################################################################################
#SUMA
num1 = input("Ingrese el primer número: ")
num2 = input("Ingrese el segundo número: ")
#Conversion de str a int, str a float
suma = int(num1) + int(num2)
print("La suma es: ", suma)

suma = float(num1) + float(num2)
print("La suma es: ", suma)

########################################################################################
#objetos
curso = "Python para iniciantes"
#sus metodos
print(curso.upper())
print(curso)
print(curso.lower())
print(curso.capitalize())

#busqueda
print(curso.find("y"))
print(curso.find("cia"))

#Reemplazos
print(curso.replace("para","FOR"))
print(curso)

#operador
print("FOR" in curso)

########################################################################################
#OPERADORES MATEMATICOS
print(10 + 5)
print(10 - 5)
print(10 * 5)
print(10 / 4)
#Division entera
print(print(10 // 4))
#modulo
print(10%3)
#exponente
print(2 ** 4)

x = 10
x = x + 5
print(x)
#operador de asignacion compacto
y = 20
y += 5
print(y)

#precedencia de operadores
x = 10 + 3 * 2
print(x)

########################################################################################
#Espresiones booleanas en python True or False
x = 3 > 2
print(x)

x = 5  == 3
print(x)

x = 5  != 3
print(x)

#and, or, not, Op. logicos
precio = 25
print(precio > 20 and precio <30)
precio = 5
print(precio > 20 or precio < 30)
print(not precio > 10)

########################################################################################
#sentencia condicional
temperatura = int(input("Indica la temperatura actual: "))

if temperatura > 22:
    print("Esta haciendo calor")
else:
    print("Hace frio")

if temperatura > 28:
    print("Esta haciendo calor")
elif temperatura > 20:
    print("Hace un dia agradable")
elif temperatura > 10:
    print("Hace un un poco de frio, prrrrr")
else:
    print("Hace frio")

print("Proceso concluido")

########################################################################################
#Bucles
contador = 12
while (contador <= 20):
    print(contador)
    contador += 1

i = 1
while (i <= 10):
    print(i)
    i += 1

########################################################################################
#LISTAS 
frutas = ['Manzana', 'Fresa', 'Naranjas', 'Pera', 'Maracuya']
print(frutas)
print(frutas[0])
print(frutas[4])
#contando de derecha a izquierda
print(frutas[-2])
#rangos
print(frutas[1:3])

#Metodos de listas
numeros = [1,2,3,4,5]

#adicionar elementos a una lista
numeros.append(6)
print(numeros)

#insertar elementos en una posicion determinada
numeros.insert(0,-1)
print(numeros)

numeros.insert(1,0)
print(numeros)

#eliminar un elemento en su primera aparicion
numeros.remove(0)
print(numeros)

#verificar si un elemento se encuentra en la lista
print(3 in numeros)

#tamaño de la lista
print(len(numeros))

#elimina el contenido de la lista
numeros.clear()
print(numeros)

########################################################################################
#objeto range
numeros = range(5)
print(numeros)

for item in numeros:
    print(item)

for item in range(5,10):
    print(item)

for item in range(10,20,2):
    print(item)

########################################################################################
#Tuplas
numeros = (1,2,3,4,5,6)
#imprimiendo un elemento
print(numeros[3])
#concurrencia
print(numeros.count(5))
#busqueda del indice del elemento
print(numeros.index(2))
########################################################################################
#Diccionario: almacena pares de valores clave-valor
mi_diccionario = {'nombre':'Bruno Diaz', 'edad':'25', 'ciudad':'La Paz'}
print(mi_diccionario)

#acceder a un valor
print(mi_diccionario['nombre'])
print(mi_diccionario['edad'])
print(mi_diccionario['ciudad'])

#agregar elementos
mi_diccionario['profesion'] = 'Ingeniero'
print(mi_diccionario)

#Eliminar un elemento
del mi_diccionario['ciudad']
print(mi_diccionario)

#obtener las claves del diccionario
print(mi_diccionario.keys())
#obtener los valores del diccionario
print(mi_diccionario.values())

#verificar si una clave existe
if 'edad' in mi_diccionario:
    print("Clave encontrada")

#Recorrido de un diccionario
for clave, valor in mi_diccionario.items():
    print("[Clave: ]",clave,"[Valor: ]",valor)

########################################################################################
# Funciones -> son bloques de codigo que realizan una tarea especifica y que son reutilizables

#funcion sin parametros
def saludar():
    print("Hola, bienvenidos al curso de Python")

#Funcion con parametros
def saludo(nomb):
    print("Hola "+nomb+" bienvenido a clases")

#llamada a la funcion
saludar()
saludo("Bruno Diaz")
saludo("Ricardo Tapia")

#Funcion que devuelve valores
def sumar(a, b):
    return a+b
#llamada a la funcion sum
resultado = sumar(10, 20)
print("La suma es: ", resultado)

#Establecer valores por defecto para los parametros de una funcion
def bienvenida(nombr="Estudiante"):
    print("Bienvenido ", nombr)
#llamada a la funcion sum bienvenida
bienvenida()
bienvenida("Susana")

#Funcion con argumentos variables
def sumador(*args):
    return sum(args)

#llamada a la funcion sumador
print(sumador(1,2,3,4,5))
print(sumador(4,5,6))