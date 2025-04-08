from xmlrpc.server import SimpleXMLRPCServer

# Function to calculate factorial
def factorial(n):
    if n < 0:
        return "Factorial not defined for negative numbers"
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n+1):
            result *= i
        return result

# Create the RPC server
server = SimpleXMLRPCServer(("localhost", 8000))
print("Server is running on port 8000...")

# Register the function
server.register_function(factorial, "factorial")

# Start the server
server.serve_forever()
