# Write a Python function to generate a list of squares of numbers from 1 to n.

def generate_squares(number):
    result = []
    for i in range(1, number + 1):
        result.append(i*i)
    
    return result

print(generate_squares(5))

def list_of_squares(number):
    return [i**2 for i in range(1, number + 1)]

print(list_of_squares(5))