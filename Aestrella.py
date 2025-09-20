
from heapq import heappush, heappop
from typing import List, Optional

class nodo:
    def __init__(self, estado: List[List[int]], padre: Optional["nodo"], costo: int, num_discos: int):
        self.estado = [list(t) for t in estado]
        self.padre = padre
        self.costo = costo
        self.num_discos = num_discos
        self.f = self.costo + self.heuristica()
    def __lt__(self, o): return self.f < o.f
    def __eq__(self, o): return isinstance(o, nodo) and self.estado == o.estado
    def __str__(self): return f"Torre A: {self.estado[0]}\nTorre B: {self.estado[1]}\nTorre C: {self.estado[2]}"
    def heuristica(self): return len(self.estado[0]) + len(self.estado[1])
    def aplicaRegla(self, r: int):
        movs = {1:(0,1),2:(0,2),3:(1,0),4:(1,2),5:(2,0),6:(2,1)}
        if r not in movs: return None
        o,d = movs[r]; est = [list(t) for t in self.estado]
        if not est[o]: return None
        if est[d] and est[o][-1] > est[d][-1]: return None
        disco = est[o].pop(); est[d].append(disco)
        return nodo(est, self, self.costo+1, self.num_discos)
    def sucesores(self, A, C):
        L=[]; 
        for i in range(1,7):
            s=self.aplicaRegla(i)
            if s is not None and s not in A and s not in C: L.append(s)
        return L
    def esMeta(self):
        obj=list(range(self.num_discos,0,-1))
        return self.estado[2]==obj and not self.estado[0] and not self.estado[1]

def ingresaLista(lista, nd): heappush(lista, nd); return lista
def Solucion(nd, inicial):
    sol=[]; 
    while nd is not inicial: sol=[str(nd)]+sol; nd=nd.padre
    return [str(inicial)]+sol

def Aestrella(nodoInicial, MAX=100000):
    ABIERTOS=[]; heappush(ABIERTOS, nodoInicial); CERRADOS=[]; exito=False; fracaso=False; cont=0
    while not exito and not fracaso and cont<=MAX:
        if not ABIERTOS: fracaso=True; break
        nodoActual=heappop(ABIERTOS); CERRADOS.append(nodoActual)
        if nodoActual.esMeta(): exito=True; break
        for nd in nodoActual.sucesores(ABIERTOS, CERRADOS): heappush(ABIERTOS, nd)
        cont += 1
    return (Solucion(nodoActual, nodoInicial), cont) if exito else (None, cont)

if __name__=="__main__":
    N=3; estado_inicial=[list(range(N,0,-1)),[],[]]; inicial=nodo(estado_inicial,None,0,N)
    resp, nodos=Aestrella(inicial); print("Nodos revisados:", nodos)
