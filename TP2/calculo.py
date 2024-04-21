import numpy as np

def calc_Imp(S_11, S_12, S_21, S_22, Zo):
    # Se definen los módulos
    Smod11 = np.abs(S_11)
    Smod12 = np.abs(S_12)
    Smod21 = np.abs(S_21)
    Smod22 = np.abs(S_22)

    # Se obtiene el valor de delta
    delta = S_11 * S_22 - S_12 * S_21

    # Se analiza estabilidad
    K = (
        np.inf
        if Smod12 * Smod21 == 0
        else (1 - Smod11**2 - Smod22**2 + np.abs(delta) ** 2) / (2 * Smod12 * Smod21)
    )
    if K < 1:
        return None

    # Se obtienen los valores de las variables auxiliares
    B1 = 1 + Smod11**2 - Smod22**2 - np.abs(delta) ** 2
    B2 = 1 + Smod22**2 - Smod11**2 - np.abs(delta) ** 2
    C1 = S_11 - (delta * np.conj(S_22))
    C2 = S_22 - (delta * np.conj(S_11))
    Cmod1 = np.abs(C1)
    Cang1 = np.angle(C1)
    Cmod2 = np.abs(C2)
    Cang2 = np.angle(C2)

    # Se calculan las reflexiones de entrada y salida del transistor
    Rmod_in = (
        np.inf if Cmod1 == 0 else (B1 - np.sqrt(B1**2 - 4 * Cmod1**2)) / (2 * Cmod1)
    )
    Rang_in = Cang1
    Rmod_out = (
        np.inf if Cmod2 == 0 else (B2 - np.sqrt(B2**2 - 4 * Cmod2**2)) / (2 * Cmod2)
    )
    Rang_out = Cang2

    Ri = Rmod_in * np.exp(1j * Rang_in)
    Ro = Rmod_out * np.exp(1j * Rang_out)

    # Se calculan las impedancias de entrada y salida del transistor
    Zi = Zo * (1 + Ri) / (1 - Ri)
    Zo = Zo * (1 + Ro) / (1 - Ro)

    # Se calculan las impedancias de fuente y de carga que deberá ver el transistor
    Zs = np.round(np.conj(Zi), 2)
    Zl = np.round(np.conj(Zo), 2)
    return Zs, Zl, K, Ri, Ro

S11 = (-0.71+0.35j)
S12 = (0.04+0.06j)
S21 = (1.64+2.61j)
S22 = (-0.58+0.21j)

Lms, Lml = np.conj(calc_Imp(S11, S12, S21, S22, 50)[3]),np.conj(calc_Imp(S11, S12, S21, S22, 50)[4])

Gtmax = (1/(1-np.abs(Lms)**2))*np.abs((S21))**2*((1-np.abs(Lml)**2)/(np.abs(1-(S22)*Lml)**2))

print(Gtmax)
