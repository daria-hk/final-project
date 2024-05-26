import random

#симуляція кидків
def simulate(amount):
    possbl_sum_of_cubes = {i: 0 for i in range(2, 13)}  #ініціалізація словника для підрахунку сум
    for _ in range(amount):
        first_random_numb = random.randint(1, 6)
        second_random_numb = random.randint(1, 6)
        sum_of_numb = first_random_numb + second_random_numb
        possbl_sum_of_cubes[sum_of_numb] += 1
    return possbl_sum_of_cubes

#розрахунок вірогідності
def probabilities(simulation, possbl_sum_of_cubes):
    probabl = {key: value / possbl_sum_of_cubes for key, value in simulation.items()}
    return probabl

simulation = simulate(15000)
probability = probabilities(simulation, 15000)

#for key, value in simulation.items():
#    print(f"Сума {key}: частота {value}")

for key, value in probability.items():
    print(f"Сума {key}: ймовірність {round(value * 100, 2)} %")