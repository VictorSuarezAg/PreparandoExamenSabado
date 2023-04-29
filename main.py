from Escuderia import Escuderia

escuderias = []
numeroEscuderias = int(input("Digite el numero de escuderias: "))
contador = 1
while contador <= numeroEscuderias:
    escuderia = Escuderia()
    escuderia.nombre = input("Digite el nombre de la escuderia: ")
    escuderia.casaMotor = input("Digite el nombre de la casa del motor: ")
    escuderia.pilotoPpal.nombre= input("Digite el nombre del piloto principal: ")
    escuderia.pilotoPpal.fechaNacimiento = input(
        "Digite la fecha de nacimiento del piloto principal: ")
    escuderia.pilotoPpal.salarioAnual = int(input(
        "Digite el salario anual del piloto principal: "))
    escuderia.pilotoPpal.pais = input(
        "Digite el pais del piloto principal: ")
    escuderia.pilotoSec.nombre = input(
        "Digite el nombre del piloto secundario: ")
    escuderia.pilotoSec.fechaNacimiento = input(
        "Digite la fecha de nacimiento del piloto secundario: ")
    escuderia.pilotoSec.salarioAnual = int(input(
        "Digite el salario anual del piloto secundario: "))
    escuderia.pilotoSec.pais = input(
        "Digite el pais del piloto secundario: ")
    escuderia.costos = int(input("Digite los costos de la escuderia: "))
    
    escuderias.append(escuderia)
    contador =  contador + 1
    
#Recorriendo la lista de escuderias
for escuderia in escuderias:
    print(f'La escuderia se llama {escuderia.nombre} y su costo es ${escuderia.costos} ')
    
costoMayor = 0
nombreEscuderiaCara = None
for escuderia in escuderias:
    if (escuderia.costos > costoMayor):
        costoMayor = escuderia.costos
        nombreEscuderiaCara = escuderia.nombre

print(f'La escuderia mas cara es {nombreEscuderiaCara} con un costo de {costoMayor}')