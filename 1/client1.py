import xmlrpc.client

# Connect to the server
proxy = xmlrpc.client.ServerProxy("http://localhost:8000/")

# Take input from user
number = int(input("Enter an integer to calculate its factorial: "))

# Call remote function
result = proxy.factorial(number)

# Print the result
print(f"Factorial of {number} is: {result}")
