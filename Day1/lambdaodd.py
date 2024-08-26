def is_odd(x):
    if x % 2 == 0:
        return True
        
numbers = [1,56,234,87,4,76,24,69,90,135]

# even = map(is_odd, numbers)
filter_odd= filter(lambda x : x % 2 != 0, numbers)
print(list(filter_odd))
