import random
import time

while True:
    try:
        archivo = input("Introduce el nombre del archivo: ")
        abrir_archivo = open(archivo)
        #print(abrir_archivo)
        break
    except: 
        print("Lo siento, archivo no encontrado o no pusiste la extensión del archivo")
        continue
while True:
    try:
        equipo_pregunta = input("¿De cuántos integrantes cada equipo? Por favor, introduce un número entero: ")
        int_equipo_pregunta = int(equipo_pregunta)
        break
    except:
        print("Por favor, introduce un número entero")
        print("----")
        continue


cant_de_alumnos = 0
nombres =  dict()

for nombre in abrir_archivo:
    nombre_sin_espacio = nombre.rstrip()
    nombres[nombre_sin_espacio] = nombres.get(nombre_sin_espacio, 0) + 1
    cant_de_alumnos = cant_de_alumnos + 1
    #print(cant_de_alumnos)

lista_de_nombres = [(n) for n,v in nombres.items()]
#print(lista_de_nombres)

numero_de_equipo = 1

while cant_de_alumnos > int_equipo_pregunta:
    print("Equipo", numero_de_equipo)
    for i in range(int_equipo_pregunta):
        persona_random = random.choice(lista_de_nombres)
        cant_de_alumnos = cant_de_alumnos - 1
        print(persona_random)
        lista_de_nombres.remove(persona_random)
        #print(lista_de_nombres)
    print("----")
    numero_de_equipo = numero_de_equipo + 1

if cant_de_alumnos < int_equipo_pregunta:
    print("Equipo", numero_de_equipo)
    for restante in lista_de_nombres:
        print(restante)   
    print("----")

print("¡Equipos listos! Que comiencen los juegos del hambre")
print("----")
time.sleep(1200)

