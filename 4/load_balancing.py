import random
from collections import deque

class Server:
    def __init__(self, id):
        self.id = id
        self.connections = 0

    def handle_request(self):
        self.connections += 1

    def release_request(self):
        if self.connections > 0:
            self.connections -= 1

    def __str__(self):
        return f"Server {self.id}: {self.connections} connections"

class LoadBalancer:
    def __init__(self, num_servers):
        self.servers = [Server(i) for i in range(num_servers)]
        self.rr_index = 0  # Round Robin tracker

    def round_robin(self):
        server = self.servers[self.rr_index]
        self.rr_index = (self.rr_index + 1) % len(self.servers)
        return server

    def least_connections(self):
        return min(self.servers, key=lambda s: s.connections)

    def random_choice(self):
        return random.choice(self.servers)

    def distribute_request(self, algorithm='round_robin'):
        if algorithm == 'round_robin':
            server = self.round_robin()
        elif algorithm == 'least_connections':
            server = self.least_connections()
        elif algorithm == 'random':
            server = self.random_choice()
        else:
            raise ValueError("Invalid algorithm selected")

        server.handle_request()
        return server.id

    def show_server_status(self):
        for server in self.servers:
            print(server)

# === Simulation ===
if __name__ == "__main__":
    lb = LoadBalancer(num_servers=4)
    num_requests = 20
    algorithm = 'least_connections'  # Change to: 'round_robin' or 'random'

    print(f"\nDistributing {num_requests} requests using {algorithm} algorithm...\n")
    for _ in range(num_requests):
        server_id = lb.distribute_request(algorithm)
        print(f"Request sent to Server {server_id}")

    print("\nServer Status After Distribution:")
    lb.show_server_status()
