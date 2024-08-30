# Write a Python function to check whether a number is even or odd.
def check_even_or_odd(number):
    flag = False
    if number % 2 == 0:
        flag = True
    
    return flag

print(check_even_or_odd(3))
print(check_even_or_odd(4))

def even_or_odd(number):
    return number % 2 == 0

print(even_or_odd(3))
print(even_or_odd(4))