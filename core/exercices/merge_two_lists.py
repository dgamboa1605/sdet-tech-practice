# Write a Python function to merge two lists into a list of tuples.
def merge_lists(list1, list2):
    return list(zip(list1, list2))

print(merge_lists([1, 2, 3], ["a", "b", "c"]))