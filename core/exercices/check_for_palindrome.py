def palindrome(data):
    index = len(data)
    result = True
    for i in data:
        last = data[index - 1]
        if i == last:
            index -= 1
        else:
            result = False
    
    return result

print(palindrome("radar"))
print(palindrome("hello"))


def palindrome(data):
    return data == data[::-1]

print(palindrome("civic"))
print(palindrome("civic1"))