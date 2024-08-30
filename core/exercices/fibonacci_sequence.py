def fibonacci(number):
    a = 0
    b = 1
    result = [a, b]
    while b < number:
        aux = a + b
        result.append(aux)
        a = b
        b = aux

    return result
    


print(fibonacci(4))
print(fibonacci(5))
print(fibonacci(6))

def fibonacci2(number):
    a, b = 0, 1
    result = []
    for _ in range(number):
        result.append(a)
        a, b = b, a + b

    return result

print(fibonacci2(4))
print(fibonacci2(5))
print(fibonacci2(6))
