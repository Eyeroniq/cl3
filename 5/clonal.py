import numpy as np
import matplotlib.pyplot as plt

# Objective function to maximize
def objective_function(x):
    return x * np.sin(10 * np.pi * x) + 1.0

# Parameters
POP_SIZE = 20
CLONE_RATE = 5
MUTATION_RATE = 0.2
MAX_GEN = 100
DOMAIN = (-1, 2)

# Generate initial population
def initialize_population(size, domain):
    return np.random.uniform(domain[0], domain[1], size)

# Mutation: small random change
def mutate(x, mutation_rate, domain):
    mutation = np.random.normal(0, mutation_rate)
    x_new = x + mutation
    return np.clip(x_new, domain[0], domain[1])

# Main Clonal Selection Algorithm
def clonal_selection():
    population = initialize_population(POP_SIZE, DOMAIN)
    best_solution = None
    best_fitness = -np.inf

    for generation in range(MAX_GEN):
        fitness = objective_function(population)

        # Track best
        max_idx = np.argmax(fitness)
        if fitness[max_idx] > best_fitness:
            best_fitness = fitness[max_idx]
            best_solution = population[max_idx]

        # Selection: take top half
        sorted_idx = np.argsort(fitness)[::-1]
        selected = population[sorted_idx[:POP_SIZE // 2]]

        # Cloning and mutation
        clones = []
        for antibody in selected:
            for _ in range(CLONE_RATE):
                clone = mutate(antibody, MUTATION_RATE * (1 - objective_function(np.array([antibody]))[0] / best_fitness), DOMAIN)
                clones.append(clone)

        # Evaluate clones and pick best
        clone_fitness = objective_function(np.array(clones))
        best_clones_idx = np.argsort(clone_fitness)[::-1][:POP_SIZE]
        population = np.array(clones)[best_clones_idx]

        # Optional: replace worst 2 individuals with random new ones
        replace_count = 2
        population[-replace_count:] = initialize_population(replace_count, DOMAIN)

    return best_solution, best_fitness

# Run algorithm
best_x, best_y = clonal_selection()
print(f"Best solution found: x = {best_x:.5f}, f(x) = {best_y:.5f}")
