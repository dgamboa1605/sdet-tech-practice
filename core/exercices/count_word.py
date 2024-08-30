# Write a Python function to count the number of words in a string.
def count_words(str):
    result = str.split()
    return len(result)

print(count_words("hello world"))

def count_words2(str):
    return len(str.split())

print(count_words2("hello world"))