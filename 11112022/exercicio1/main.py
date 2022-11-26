from animal import Animal

animal = Animal(input("Digite a especie: "), input("Digite a raça: "), input("Digite o porte: "), input("Digite a cor: "))

print(f'A especie: {animal.especie} - A raça: {animal.raca} - O porte: {animal.porte} - A cor {animal.cor}')

print(animal)

animal2 = Animal(input("Digite a especie: "), input("Digite a raça: "), input("Digite o porte: "), input("Digite a cor: "))

print(f'A especie: {animal2.especie} - A raça: {animal2.raca} - O porte: {animal2.porte} - A cor {animal2.cor}')

print(animal2)


