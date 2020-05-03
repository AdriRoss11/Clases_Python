class PartidoFutbol:
    def __init__(self, equipo1, equipo2, liga, division, dia_partido, var, arbitro_principal, arbitro_var):
        self.equipo1 = equipo1
        self.equipo2 = equipo2
        self.liga = liga
        self.division = division
        self.dia_partido = dia_partido
        self.var = var
        self.arbitro_principal = arbitro_principal
        self.arbitro_var = arbitro_var

    def mostrar_arbitros(self):
        resultado = ""
        if (self.var == True) :
            resultado = "Arbitro Principal: " + self.arbitro_principal + "\nArbitro Var: " + self.arbitro_var
        else:
            resultado = "Arbitro Principal else: " + self.arbitro_principal
        return resultado

    def mostrar_datos_partido(self):
        resultado = "Equipos a enfrentarse el día de hoy " + self.dia_partido + " son..."
        resultado += "\nLocal: " + self.equipo1 + " Visitante: " + self.equipo2
        resultado += "\nDe la " + self.division + " división y de la Liga: " + self.liga
        return resultado

    def resultado_partido(self, score1, score2):
        resultado = ""
        if (score1 == score2) : resultado = "Empate de " + self.equipo1 + " vs " + self.equipo2
        elif (score1 > score2) : resultado = "Gano: " + self.equipo1
        else : resultado = "Gano: " + self.equipo2
        return resultado

    def __str__(self):
        return "Equipo 1:{} \nEquipo 2:{} \nLiga:{} \nDivisión:{} \nDía:{} \nVar:{} \nArbitro Principal: {} \nArbitro Var: {}".format(self.equipo1, self.equipo2, self.liga, self.division, self.dia_partido, self.var,                       self.arbitro_principal, self.arbitro_var)

print("**Partido de Futbol**")
partido_futbol = PartidoFutbol("Bolivar", "The Strongest", "Boliviana", "1ra", "Domingo", True, "Gery Vargas", "Antelo")
print("-"*25)
print(partido_futbol)
print("-"*25)
print(partido_futbol.mostrar_datos_partido())
print("-"*25)
print(partido_futbol.mostrar_arbitros())
print("-"*25)
print(partido_futbol.resultado_partido(5,5))


class SeminarioWeb:
    def __init__(self, nombre_webinar, pais, ciudad, fecha_inicio, cantidad_participantes):
        self.nombre_webinar = nombre_webinar
        self.pais = pais
        self.ciudad = ciudad
        self.fecha_inicio = fecha_inicio
        self.cantidad_participantes = cantidad_participantes

    def obtener_nuevo_seminario(self, nombre_seminario):
        return "El nuevo seminario es: " + nombre_seminario

    def cantidad_inscritos (self):
        return self.cantidad_participantes

    def inicio_seminario(self):
        return "Inicio el Seminario..."

    def termino_seminario(self):
        return "Termino el Seminario..."

    def __str__(self):
        return "Nombre Seminario Web:{} \nPaís:{} \nCiudad:{} \nFecha de Inicio:{}, \nParticipantes Inscritos:{}".format(self.nombre_webinar, self.pais, self.ciudad, self.fecha_inicio, self.cantidad_participantes)

print("**Seminario Web**")
seminario_web = SeminarioWeb("Marketing Digital", "Bolivia", "La Paz", "5 de Mayo", 400)
print(seminario_web)
print("-"*25)
print(seminario_web.inicio_seminario())
print("-"*25)
print(seminario_web.obtener_nuevo_seminario("Bioseguridad en el Trabajo"))
print("-"*25)
print(seminario_web.cantidad_inscritos())
print("-"*25)
print(seminario_web.termino_seminario())
print("-"*25)