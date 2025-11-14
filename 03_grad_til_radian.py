"""

Konverter grader til radianer.
Bendik Spikkerud
2025 11 14

"""

import numpy as np


def rad_converter(v_grad):  # Konverterer grader til radianer
    v_rad = v_grad * np.pi / 180
    return v_rad


grader = float(input("Skriv inn gradtallet:"))
radian = rad_converter(grader)  # Kjører radianfunksjonen.

print(f"radianen er {radian}")
