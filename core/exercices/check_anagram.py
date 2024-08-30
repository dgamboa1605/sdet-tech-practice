# Write a Python function to check if two strings are anagrams.
def check_anagram(str1, str2):
    return sorted(str1) == sorted(str2)

print(check_anagram("listen", "silent"))
print(check_anagram("hello", "world"))