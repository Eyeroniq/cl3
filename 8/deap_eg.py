import random
from deap import base, creator, tools, algorithms

# Evaluation function: minimize the sum of squares (a simple quadratic)
def eval_func(individual):
    return sum(x ** 2 for x in individual),

def main():
    # DEAP setup
    creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
    creator.create("Individual", list, fitness=creator.FitnessMin)

    toolbox = base.Toolbox()
    
    # Attribute generator
    toolbox.register("attr_float", random.uniform, -5.0, 5.0)
    
    # Individual and population generator
    toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_float, n=3)
    toolbox.register("population", tools.initRepeat, list, toolbox.individual)
    
    # Genetic operators
    toolbox.register("evaluate", eval_func)
    toolbox.register("mate", tools.cxBlend, alpha=0.5)
    toolbox.register("mutate", tools.mutGaussian, mu=0, sigma=1, indpb=0.2)
    toolbox.register("select", tools.selTournament, tournsize=3)

    population = toolbox.population(n=50)
    generations = 20

    # Evolution process
    for gen in range(generations):
        offspring = algorithms.varAnd(population, toolbox, cxpb=0.5, mutpb=0.1)
        
        # Evaluate fitness
        fits = list(map(toolbox.evaluate, offspring))
        for fit, ind in zip(fits, offspring):
            ind.fitness.values = fit

        population = toolbox.select(offspring, k=len(population))

    # Select best individual
    best_ind = tools.selBest(population, k=1)[0]
    best_fitness = best_ind.fitness.values[0]
    print("Best individual:", best_ind)
    print("Best fitness:", best_fitness)

if __name__ == "__main__":
    import multiprocessing
    multiprocessing.freeze_support()  # Optional for Windows support
    main()
