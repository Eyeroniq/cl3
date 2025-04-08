import numpy as np
import random

# Define the distance matrix
distance_matrix = np.array([
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
], dtype=float)

# Replace 0s on the diagonal with np.inf to prevent division by zero in visibility
np.fill_diagonal(distance_matrix, np.inf)

# Parameters
num_ants = 10
num_iterations = 50
evaporation_rate = 0.5
pheromone_constant = 1.0
heuristic_constant = 1.0

num_cities = len(distance_matrix)
pheromone = np.ones((num_cities, num_cities))
visibility = 1 / distance_matrix  # Heuristic: inverse of distance

best_route = None
shortest_distance = float('inf')

for iteration in range(num_iterations):
    ant_routes = []

    for ant in range(num_ants):
        current_city = random.randint(0, num_cities - 1)
        visited_cities = [current_city]

        while len(visited_cities) < num_cities:
            probabilities = []
            total_prob = 0

            for city in range(num_cities):
                if city not in visited_cities:
                    pheromone_value = pheromone[current_city][city] ** pheromone_constant
                    visibility_value = visibility[current_city][city] ** heuristic_constant
                    prob = pheromone_value * visibility_value
                    probabilities.append((city, prob))
                    total_prob += prob

            # Normalize and choose next city based on probability
            if total_prob == 0:
                selected_city = random.choice([city for city in range(num_cities) if city not in visited_cities])
            else:
                rand_val = random.uniform(0, total_prob)
                cumulative = 0
                for city, prob in probabilities:
                    cumulative += prob
                    if cumulative >= rand_val:
                        selected_city = city
                        break

            visited_cities.append(selected_city)
            current_city = selected_city

        # Return to start to complete tour
        visited_cities.append(visited_cities[0])
        ant_routes.append(visited_cities)

    # Pheromone update
    delta_pheromone = np.zeros((num_cities, num_cities))
    for route in ant_routes:
        route_distance = sum(distance_matrix[route[i]][route[i+1]] for i in range(num_cities))
        for i in range(num_cities):
            city_a = route[i]
            city_b = route[i+1]
            delta_pheromone[city_a][city_b] += 1 / route_distance
            delta_pheromone[city_b][city_a] += 1 / route_distance  # symmetric TSP

        # Update best route if shorter
        if route_distance < shortest_distance:
            best_route = route
            shortest_distance = route_distance

    pheromone = (1 - evaporation_rate) * pheromone + delta_pheromone

# Output
print("Best route:", best_route)
print("Shortest distance:", round(shortest_distance, 2))
