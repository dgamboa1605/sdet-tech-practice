# Write a Python function to count the number of vowels in a string.
def count_vowels(str):
    check = "aeiouAEIOU"
    count = 0
    for i in str:
        if i in check:
            count += 1
    
    return count

print(count_vowels("hello"))
print(count_vowels("hellOO"))

def count_vowels2(str):
    vowels = "aeiouAEIOU"
    return sum(1 for char in str if char in vowels)

print(count_vowels2("hello"))
print(count_vowels2("hellOO"))