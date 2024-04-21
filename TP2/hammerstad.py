import numpy as np

c = 3e8
e0 = 8.854e-12
u0 = 4 * np.pi * 1e-7


def get_permitividad_efectiva(WH, er):
    if WH < 0.35:
        return (er + 1) / 2 + ((1 + 12 / WH) ** (-0.5) + 0.04 * (1 - WH) ** 2) * (
            er - 1
        ) / 2
    else:
        return (er + 1) / 2 + ((1 + 12 / WH) ** (-0.5)) * (er - 1) / 2


def get_A(Zo, er):
    return (Zo) / 60 * np.sqrt((er + 1) / 2) + (er - 1) / (er + 1) * (0.23 + 0.11 / er)


def get_B(Zo, er):
    return (377 * np.pi) / (2 * Zo * np.sqrt(er))


def get_WH_menor(Zo, er):
    A = get_A(Zo, er)
    return (8 * np.exp(A)) / (np.exp(2 * A) - 2)


def get_WH_mayor(Zo, er):
    B = get_B(Zo, er)
    return (2 / np.pi) * (
        B
        - 1
        - np.log(2 * B - 1)
        + (er - 1) * (np.log(B - 1) + 0.39 - 0.61 / er) / (2 * er)
    )


def get_WH(Zo, er):
    WH_menor = get_WH_menor(Zo, er)
    if WH_menor <= 2:
        return WH_menor
    else:
        return get_WH_mayor(Zo, er)


def get_impedancia_caracteristica(WH, ef):
    if WH <= 1:
        return (60 / np.sqrt(ef)) * np.log(8 / WH + WH / 4)
    else:
        return (120 * np.pi / np.sqrt(ef)) / (WH + 1.393 + 0.667 * np.log(WH + 1.444))


def get_W_efectivo(W, H, t):
    if H >= 2 * np.pi * W:
        return W + (1 + np.log(4 * np.pi * H / t)) * (t / np.pi)
    else:
        return W + (1 + np.log(2 * H / t)) * (t / np.pi)
