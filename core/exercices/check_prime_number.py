def is_prime(number):
    if number < 2:
        return False
    
    flag = True

    for i in range(2, number):
        if number % i == 0:
            flag = False
            break
    
    return flag

print(is_prime(5))
print(is_prime(4))
print(is_prime(2))
print(is_prime(3))
print(is_prime(10))
print(is_prime(13))


def is_prime2(number):
    if number <= 1:
        return False
    
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    
    return True

print(is_prime2(5))
print(is_prime2(4))
print(is_prime2(2))
print(is_prime2(3))
print(is_prime2(10))
print(is_prime2(13))