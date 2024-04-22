import numpy as np


def s_L4_stub_in(Zin, Zs, Zo, lda):
    # Se obtiene la constante de fase:
    b = 2 * np.pi / lda
    # Se adapta el stub paralelo para cancelar la parte imaginaria.
    # Se obtiene la admitancia de entrada del transistor:
    Yin = 1 / Zin
    # Se obtiene la parte imaginaria:
    Yimin = np.imag(Yin)
    # Se obtiene la distancia necesaria de la microtira para cancelar la parte imaginaria mediante un stub en circuito abierto:
    d = np.arctan(-Zo * Yimin) / b
    # Se obtiene ahora la parte real habiendo cancelado la parte imaginaria y se lo convierte a impedancia:
    Zr = 1 / np.real(Yin)

    # Se adapta la impedancia real a la impedancia necesaria mediante el método del cuarto de lambda.
    # Se obtiene el Zo necesario en el camino de longitud cuarto de lambda:
    ZoL4 = np.sqrt(Zr * Zs)
    return d, ZoL4


def out_L4_stub_l(Zout, Zl, Zo, lda):
    b = 2 * np.pi / lda
    # Se adapta la impedancia compleja mediante el método de cuarto de lambda.
    # Se obtiene el Zo necesario en el camino de longitud cuarto de lambda:
    ZoL4 = np.sqrt(Zl * np.real(Zout))
    # Se adapta el stub paralelo para cancelar la parte imaginaria.
    # Se obtiene la admitancia imaginaria al final del adaptador de cuarto de lambda:
    YimoutL4 = np.imag(Zout) / ZoL4**2
    # Se obtiene la distancia necesaria de la microtira para cancelar la parte imaginaria mediante un stub en circuito abierto:
    d = np.arctan(-Zo * YimoutL4) / b
    return d, ZoL4
