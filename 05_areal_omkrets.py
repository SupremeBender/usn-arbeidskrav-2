import math

def omkr_areal(a, b): # input diameter og høyde
    r = a / 2 # Radius er halve diameter
    omkrets_halvsirkel = math.pi * r
    areal_halvsirkel = math.pi * r**2 / 2 
    omkrets_trekant = b + math.hypot(b, a)
    areal_trekant = a * b / 2
    omkrets_total = omkrets_halvsirkel + omkrets_trekant
    areal_total = areal_halvsirkel + areal_trekant
    return omkrets_total, areal_total
    
a = float(input("Skriv inn diameteren til halvsirkelen: "))
b = float(input("Skriv inn høyden til trekanten: "))
omkrets, areal = omkr_areal(a, b) # Kjører funksjonen fra tidligere
print(f"Omkretsen av figuren: {omkrets}")
print(f"Arealet av figuren: {areal}")
