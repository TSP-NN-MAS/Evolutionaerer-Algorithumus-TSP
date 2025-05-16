import random
import math

# Erstellt eine Tour mit zufälliger Permutation
def create_tour(number_of_cities):
    tour = list(range(number_of_cities))
    random.shuffle(tour)
    return tour

# Berechnet die Distanz zwischen den Städten in einer Permutation(Tour) mit Satz des Pythagoras
def calculate_distance(citys, tour):
    distance = 0
    number_of_citys = len(tour)
    for i in range(number_of_citys):
        from_city = citys[tour[i]]
        to_city = citys[tour[(i + 1) % number_of_citys]]
        dx = to_city[0] - from_city[0]
        dy = to_city[1] - from_city[1]
        distance += math.sqrt(dx * dx + dy * dy)
    return distance

# Erstellt eine Population(Gruppe) von Permutationen(Touren)
def create_population(population_size, number_of_citys):
    population = []
    for i in range(population_size):
        population.append(create_tour(number_of_citys))
    return population

# Wählt zufällig 3 Permutationen(Touren) aus der Population und wählt davon die kürzeste
def tournament_selection(population, citys, k=3):
    competitors = random.sample(population, k)
    best = min(competitors, key=lambda tour: calculate_distance(citys, tour))
    return best

# Wählt Eltern mit tournament_selection aus und tut sie in eine Liste an Eltern
def select_parents(population, cities, μ):
    parents = []
    for i in range(μ):
        parent = tournament_selection(population, cities)
        parents.append(parent)
    return parents

# Wählt teil aus Elternteil 1 und rest aus Elternteil 2 aus um sie in einem Kind einzufügen, Order Crossover(OX)
def order_crossover(parent1, parent2, num_of_citys):
    start = random.randint(0, num_of_citys - 2)
    end = random.randint(start + 1, num_of_citys - 1)
    child = [None] * len(parent1)
    child[start:end+1] = parent1[start:end+1]
    pos = 0
    for city in parent2:
        if city not in child:
            while child[pos] is not None:
                pos += 1
            child[pos] = city
            pos += 1
    return child

# Mutiert eine Permutation(Tour) mit einer Mutationswahrscheinlichkeit, indem 2 zufällige Städte miteinander getauscht werden
def mutate(tour, mutation_rate):
    if random.random() < mutation_rate:
        i, j = random.sample(range(len(tour)), 2)
        tour[i], tour[j] = tour[j], tour[i]
    return tour

# Generiert Kinder aus 2 Eltern mit order_crossover, indem aus μ Eltern λ Kinder erstellt werden. Bei dem Jedes Elternteil, bei ausreichend großem λ, mindestens 1-mal kombiniert wird und falls nötig noch zufällige Eltern miteinander kombiniert werden
def generate_children(population, citys, μ, λ, mutation_rate):
    children = []
    parents = select_parents(population, citys, μ)
    random.shuffle(parents)
    for i in range(0, len(parents)-1, 2):
        if len(children) > λ:
            break
        parent1 = parents[i]
        parent2 = parents[i+1]
        child = mutate(order_crossover(parent1, parent2, len(citys)), mutation_rate)
        children.append(child)
    while len(children) < λ:
        random_parent1 = random.choice(parents)
        random_parent2 = random.choice(parents)
        child = mutate(order_crossover(random_parent1, random_parent2, len(citys)), mutation_rate)
        children.append(child)
    return children
