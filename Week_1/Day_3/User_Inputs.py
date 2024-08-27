name = input("What is your name? ")

age = input("What is your Age? ")

y = "years" if int(age) > 1 else "year"

print ("Hello " + name + "! You are " + age + " " + y + " old.")


try:
    age = int(age)  
    if 0 < age < 10:
        print("You are too young")
    elif 10 < age <= 20:
        print("Your age is okay, keep playing")
    else:
        print("You are too old to play this code game")
except ValueError:
    print("Please enter a valid number for age.")
