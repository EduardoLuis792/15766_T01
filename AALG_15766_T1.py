import random

class EquipoVoley:
    def __init__(self, nombre):
        self.nombre = nombre
        self.partidosGanados = 0
        self.partidosPerdidos = 0
        self.setGanados = 0

equipo1 = EquipoVoley("Equipo 1")
equipo2 = EquipoVoley("Equipo 2")
equipos = [equipo1, equipo2]

def RegistraSet(indice_equipo):
    rival = 1 - indice_equipo
    equipos[indice_equipo].setGanados += 1

    partido_terminado = False
    if equipos[indice_equipo].setGanados == 3:
        equipos[indice_equipo].partidosGanados += 1
        equipos[rival].partidosPerdidos += 1
        print(f"\n{equipos[indice_equipo].nombre} gana el partido\n")
        partido_terminado = True
    return partido_terminado

def Puntos():
    return random.randint(10, 28)

def PuntosExtras():
    return random.randint(0, 6)

def JugarPartido():
    while equipo1.setGanados < 3 and equipo2.setGanados < 3:
        p1 = 0
        p2 = 0
        print(f"\n- Nuevo Set -")
        print(f"{equipo1.nombre}: {p1} | {equipo2.nombre}: {p2}")

        intentos = 0
        while True:
            if (p1 >= 25 or p2 >= 25) and abs(p1 - p2) >= 2:
                if p1 > p2:
                    print(f"-> {equipo1.nombre} gana el set ({p1}-{p2})")
                    if RegistraSet(0):
                        return
                else:
                    print(f"-> {equipo2.nombre} gana el set ({p2}-{p1})")
                    if RegistraSet(1):
                        return
                break

            if intentos >= 20:
                if p1 > p2:
                    print(f"(Desempate forzado) -> {equipo1.nombre} gana el set ({p1}-{p2})")
                    if RegistraSet(0):
                        return
                else:
                    print(f"(Desempate forzado) -> {equipo2.nombre} gana el set ({p2}-{p1})")
                    if RegistraSet(1):
                        return
                break

            add_p1 = PuntosExtras()
            add_p2 = PuntosExtras()
            p1 += add_p1
            p2 += add_p2
            print(f"(Puntos extra) {equipo1.nombre}: {p1} | {equipo2.nombre}: {p2} (+{add_p1}, +{add_p2})")
            intentos += 1

def ResultadoTorneo():
    for i in range(len(equipos) - 1):
        for j in range(len(equipos) - i - 1):
            if equipos[j].partidosGanados < equipos[j + 1].partidosGanados:
                equipos[j], equipos[j + 1] = equipos[j + 1], equipos[j]

    print("\n- Resultados del Torneo -")
    for e in equipos:
        print(f"{e.nombre} - Ganados: {e.partidosGanados}, Perdidos: {e.partidosPerdidos}")

def main():
    n = int(input("¿Cuantos partidos jugaran los equipos? "))
    for i in range(n):
        print(f"\n- Partido {i + 1} -")
        equipo1.setGanados = 0
        equipo2.setGanados = 0
        JugarPartido()
    ResultadoTorneo()

main()













