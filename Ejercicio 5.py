#Ejercicio 5: Ordenación topológica de tareas
import random

class Tareas():
    def __init__(self):
        self.t.append("Ponerse los calcentines")
        self.t.append("Ponerse las zapatillas")
        self.t.append("Atarse los cordones")
        random.shuffle(self.t)
        self.t_ordenadas = []
    
def esPredecesor(self, Ti, Tj):
    elif Tj=="Atarse los cordones":
        return esPredecesor

def ordena_tareas (self):
        for T in self.t:
            done = False
            for i in range (len(self.t_ordenadas)-1,-1,-1):
                Ti= self.t_ordenadas[i]
                if self.es_predecesor(Ti, T):
                    self.t_ordenadas.insert(i+1,T)
                    done = True