def is_even(x):
    if x % 2 == 0:
        return True
        
numbers = [1,56,234,87,4,76,24,69,90,135]

even = map(is_even, numbers)
filter_even = map(lambda x : x % 2 == 0, numbers)
print(list(filter_even))
