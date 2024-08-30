# Write a Python function to calculate the sum of the digits of a number.
def sum_digits(number):
    result = 0
    for i in str(number):
        result += int(i)
    
    return result

print(sum_digits(458))


def sum_digits2(number):
    return sum(int(digit) for digit in str(number))

print(sum_digits2(458))