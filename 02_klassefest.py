antall_elever = int(input("Skriv inn antall elever: "))
elever_per_pizza = 4  # Hvor mange elever hver pizza dekker.

# Ceiling division (//) runder ned til nærmeste hele pizza.
# For å runde opp legger vi på en hel pizza minus 1 bit før vi deler.
antall_pizza = (antall_elever + elever_per_pizza - 1) // elever_per_pizza

print(f"Det må handles inn {antall_pizza} pizzaer til festen.")
