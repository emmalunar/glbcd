# # # # names = ["sam", "john", "james"]
# # # # map(len, names)

# # # # for i in names:

# # # # print(list(len.names))


# def too_old(x): return x > 30
# ages = [22, 25,29, 34, 56, 24, 12]
# filter(too_old, ages) 
# print(list(filter(too_old, ages)))

# def acceptable_students_dict(x):
#     age  = x['age']  
#     level = x['level']
#     return ((age > 25) and (level >= 2))
# data = [ {"age":25,
#              "level":1},
#              {"age":17,
#               "level":3},
#               {"age":100,
#                "level":3}

#     ]
# filter(acceptable_students_dict.data)
# # print(list(filter(acceptable_students_dict)))





# # def uni(slogan):
# #     return print("ucc" + slogan)


# # uni()
# # print(uni)


# items = [1, 2, 3, 4, 5]
# squares = map((lambda x : x **2), items)
# print(list(squares)) 

def is_even():
    numbers = [1,56,234,87,4,76,24,69,90,135]
    if is_even:
        return True
    else:
        return False
    
    for i in numbers:
        if i % 2 == 0:
            print(i)
    # return 0