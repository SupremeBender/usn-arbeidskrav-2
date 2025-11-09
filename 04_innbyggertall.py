data = {
    "Norge": ["Oslo", 0.634],
    "England": ["London", 8.982],
    "Frankrike": ["Paris", 2.161],
    "Italia": ["Roma", 2.873],
}

land = input("Skriv inn et land: ")
hovedstad, befolkning = data[land]  # tildeler variabler til dict-elementer

print(
    f"{hovedstad} er hovedstaden i {land} og det er "
    f"{befolkning} mill innbyggere i {hovedstad}."
)

legge_til = input("Ønsker du å legge til flere land? (j/n): ")

# Hvis brukeren svarer ja, legg til nytt land
if legge_til == "j":
    nytt_land = input("Hva heter det nye landet? ")
    ny_hovedstad = input(f"Hva er hovedstaden i {nytt_land}? ")
    ny_befolkning = input(f"Hvor mange millioner inbyggere er det i {ny_hovedstad}?")

    # Oppdater dict med nye data
    data.update({nytt_land: [ny_hovedstad, ny_befolkning]})
    print(
        f"{nytt_land} lagt til med hovedstad {ny_hovedstad}"
        f" og befolkingstall {ny_befolkning} millioner."
    )
    print("dictionary oppdatert:")
    print(data)
