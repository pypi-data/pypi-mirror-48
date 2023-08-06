from heurispy.framework import inicia_exploracion_heuristica, genera_lista_ejecuciones_heuristicas
from heurispy.problema import Problema
from heurispy.heuristicas.busqueda_local_iterada import BusquedaLocalIterada


def generar_solucion_nueva():
    import numpy
    import random
    lista_numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    random.shuffle(lista_numeros)
    solucion_nueva = numpy.zeros(shape=(15, 15))
    for i in range(len(lista_numeros)):
        solucion_nueva[lista_numeros[i]][i] = 1
    return solucion_nueva


def funcion_objetivo(solucion):
    import numpy

    matriz_rutas = numpy.array([[50,  1,  4, 50,  1,  8, 50,  6,  4,  2, 50, 50, 50, 50, 50],
                                [ 1, 50,  1, 10,  5, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50],
                                [ 4,  1, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50,  1, 50, 50],
                                [50, 10, 50, 50, 50, 50, 50, 50, 50,  1,  1,  2,  2, 50,  5],
                                [ 1,  5, 50, 50, 50,  1, 50, 50, 50, 50, 50, 50, 50, 50, 50],
                                [ 8, 50, 50, 50,  1, 50,  1,  7, 50, 50, 50, 50, 50, 50, 50],
                                [50, 50, 50, 50, 50,  1, 50,  1, 13, 50, 50, 50, 50, 50, 50],
                                [ 6, 50, 50, 50, 50,  7,  1, 50,  1, 50, 50, 50, 50, 50, 50],
                                [ 4, 50, 50, 50, 50, 50, 13,  1, 50,  1,  7, 50, 50, 20, 50],
                                [ 2, 50, 50,  1, 50, 50, 50, 50,  1, 50,  3, 50,  8, 50, 50],
                                [50, 50, 50,  1, 50, 50, 50, 50,  7,  3, 50, 50, 50,  1, 50],
                                [50, 50, 50,  2, 50, 50, 50, 50, 50, 50, 50, 50, 50,  1,  1],
                                [50, 50,  1,  2, 50, 50, 50, 50, 50,  8, 50, 50, 50, 50,  1],
                                [50, 50, 50, 50, 50, 50, 50, 50, 20, 50,  1,  1, 50, 50,  8],
                                [50, 50, 50,  5, 50, 50, 50, 50, 50, 50, 50,  1,  1,  8, 50]])
    return numpy.sum(numpy.multiply(matriz_rutas, solucion))


def vecindad(solucion):
    import numpy
    import random

    nueva_solucion = numpy.copy(solucion)
    valor1 = numpy.random.randint(15)
    valor2 = random.choice(numpy.delete(numpy.arange(0, 15), valor1))
    nueva_solucion[[valor1, valor2]] = nueva_solucion[[valor2, valor1]]
    return nueva_solucion


if __name__ == '__main__':

    problema_kilometros = Problema(dominio=generar_solucion_nueva,
                                   funcion_objetivo=funcion_objetivo,
                                   funcion_variacion_soluciones=vecindad)

    localIterada = BusquedaLocalIterada(problema_kilometros, max_iteraciones=100000)

    parametros_locGui = dict(busqueda_local_sin_minimo_global=[50, 100], rango_perturbacion=[4],
                             busqueda_iterada_sin_mejora=[50])

    lista_bloque_parametros_guiada = genera_lista_ejecuciones_heuristicas(parametros_locGui, repeticiones=10)

    inicia_exploracion_heuristica(localIterada, lista_bloque_parametros_guiada)
