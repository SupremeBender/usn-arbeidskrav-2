"""

Alder i gitt år basert på fødselsår.
Bendik Spikkerud
2025 11 14

"""

alder = int(input("Hvilket år er du født? "))
år = 2024  # Året det skal regnes ut alder i.

hvor_gammel = år - alder  # Trekk alder fra årstall.

print(f"Du fyller {hvor_gammel} år i {år}.")  # Print resultatet.
