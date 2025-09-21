PROYECTO 1 — Fundamentos de IA
A* (informado) vs BFS (no informado)

Integrantes:
- Cristobal Flores Villegas (NRC: 8060)
- Benjamin Peña Diaź (NRC: 8060)
- Fransisco Morales Diaz (NRC: 8061)

Nombre del Juego: Torres de Hanoi

Enlace a algún sitio para poder comprender en qué consiste la versión del juego que consideraste:
https://www.geogebra.org/m/NqyWJVra


Heurística implementada (explicación):
h(n) = número de discos que NO están en la Torre C (destino).
Justificación: es una heurística admisible porque nunca sobreestima el costo real restante. 
Cada disco fuera de la Torre C requiere al menos un movimiento para llegar al destino, por lo que h(n) ≤ costo óptimo restante.

Estado inicial 1: N = 2 discos — A: [2, 1], B: [], C: []
N° nodos revisados A*: 5
N° nodos revisados BFS: 7

Estado inicial 2: N = 3 discos — A: [3, 2, 1], B: [], C: []
N° nodos revisados A*: 17
N° nodos revisados BFS: 25

Estado inicial 3: N = 4 discos — A: [4, 3, 2, 1], B: [], C: []
N° nodos revisados A*: 53
N° nodos revisados BFS: 71

Estado inicial 4: N = 5 discos — A: [5, 4, 3, 2, 1], B: [], C: []
N° nodos revisados A*: 177
N° nodos revisados BFS: 233

Estado inicial 5: N = 6 discos — A: [6, 5, 4, 3, 2, 1], B: [], C: []
N° nodos revisados A*: 582
N° nodos revisados BFS: 687

Los 3 archivos los debes comprimir en un .zip y nombrar al archivo comprimido con el número de tu grupo. Este archivo es el que debes subir a la casilla de entrega en Canvas.