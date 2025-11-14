import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 200) # Generer array x med punkter

y = -x**2 - 5 # Regn ut y basert på formelen

plt.plot(x, y) # Tegn grafen
plt.show() # Vis grafen
