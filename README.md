# proyecto-1-fundamentos
proyecto1 aestrella


[Enunciado Proyecto 1 (1).pdf](https://github.com/user-attachments/files/22163511/Enunciado.Proyecto.1.1.pdf)


PROYECTO N°1
Búsqueda Informada – Algoritmo A*
Aplicación en un juego
Fecha de entrega código: Domingo 14 de septiembre de 2025
Modalidad: Trabajo Grupal (de 2 a 4 integrantes. No puede ser individual)
Ponderación: 15% de la nota del curso
1. Objetivo.
El objetivo de este proyecto es que modeles un juego combinatorial para resolverlo mediante el
algoritmo A* y compares su eficiencia con el algoritmo BFS.
2. Selección del juego.
Para que tu elección sea viable, el juego debe cumplir con:
- Se juegue con solo un jugador (si es un jugador contra el computador se considera que
posee 2 jugadores).
- El juego debe tener su información visible en todo momento (ejemplo: el juego de
buscaminas no serviría).
- Debe tener una meta clara que determina cuando concluye el juego.
- Se debe poder establecer un conjunto de reglas de producción que permita
Además, las reglas deben ser finitas y claramente identificables. Las puedes reconocer al
determinar cuál(es) acción(es) permiten que el juego cambie de estado: por ejemplo,se pinta una
celda, se da un paso en un recorrido, se coloca una pieza, se mueve una ficha, etc (depende del
juego que elijas)
3. Sobre la implementación en Python.
Debes usar como código base el mostrado en clases de cátedra: aestrella_(puzzle_8).py
disponible en CANVAS.
Tu trabajo consiste en definir la clase nodo para el juego que seleccionaste. Recuerda mantener
los atributos padre y costo. Además, en el código base verás que hay definidas 2 funciones
heurísticas: esto solo fue a modo de ejemplo para que se observara cuánto se reduce el número
de nodos revisados por A* cuando una heurística es más informada. Para el proyecto solo debes
definir una función heurística.
En el “BLOQUE PRINCIPAL” debes establecer el estado inicial para realizar las pruebas de tu código
y también puedes modificar el valor de MAX (número de iteraciones de la búsqueda) con el valor
que necesites.
Ingeniería Civil Informática
Fundamentos de Inteligencia Artificial
Irene Zuccar Parrini 2
4. Sobre la eficiencia de A*:
Para probar que la heurística diseñada en A* mejora el tiempo de respuesta al revisar menos
nodos del grafo de estados, debes comparar el número de nodos revisados por A* con el número
de nodos revisados por BFS (Búsqueda en Amplitud), usando la misma clase nodo diseñada. Esto
significa que debes utilizar el código “busqueda_no_informada_(puzzle_8).py”
5. Sobre la entrega.
Debes entregar los archivos Aestrella.py y BFS.py, con el código para resolver el juego que
escogiste.
Además debes entregar un archivo de texto llamado readme.txt con la siguiente información:
Integrantes:
- Nombre y Apellidos integrante 1 (NRC: XXXX)
- Nombre y Apellidos integrante 2 (NRC: XXXX)
- Nombre y Apellidos integrante 3 (NRC: XXXX)
- Nombre y Apellidos integrante 4 (NRC: XXXX)
Nombre del Juego: XXXXXXXXXXXXXX
Enlace a algún sitio para poder comprender en qué consiste la versión del juego que
consideraste
Heurística implementada: (explicación)
XXXXXXXXXXXXXXXXXX . . .
Estado inicial 1: XXXXX
N° nodos revisados A*: XXXXXX
N° nodos revisados BFS: XXXXXX
Estado inicial 2: XXXXX
N° nodos revisados A*: XXXXXX
N° nodos revisados BFS: XXXXXX
Estado inicial 3: XXXXX
N° nodos revisados A*: XXXXXX
N° nodos revisados BFS: XXXXXX
Estado inicial 4: XXXXX
N° nodos revisados A*: XXXXXX
N° nodos revisados BFS: XXXXXX
Estado inicial 5: XXXXX
N° nodos revisados A*: XXXXXX
N° nodos revisados BFS: XXXXXX
Los 3 archivos los debes comprimir en un .zip y nombrar al archivo comprimido con el número
de tu grupo. Este archivo es el que debes subir a la casilla de entrega en Canvas.
Ingeniería Civil Informática
Fundamentos de Inteligencia Artificial
Irene Zuccar Parrini 3
6. Sobre la evaluación.
1. Ambos códigos que entregues serán ejecutado y probado con los diferentes estados iniciales.
2. Debes usar el algoritmo A* y BFS entregado para este proyecto y solo hacer las modificaciones
indicadas en este enunciado. Si usas otra implementación la evaluación de este proyecto será
un 1.0.
3. Debes entregar un código debidamente ordenado. Consideraré:
- En el código deben estar solo métodos e instrucciones que tu programa utiliza y no debe
poseer instrucciones “basura” (esas que se comentan porque ya no se usan, o las que no
se comentan, pero nada las ejecuta).
- Debes usar identificadores representativos para las variables, parámetros de entrada y
funciones.
- Si lo estimas conveniente, agrega comentarios.
4. No se aceptarán trabajos atrasados.
5. Cualquier detalle de este proyecto que no haya sido mencionado en este enunciado, se
aclarará mediante un anuncio en Canvas.
