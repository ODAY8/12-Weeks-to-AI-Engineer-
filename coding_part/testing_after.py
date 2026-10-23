name = input("Enter your name: ")
age = input ("Enter your age: ")

if name and age:
    age = int(age)
    print("hello " + name + " next year, you will be " + str(age + 1) + "years old ")
else:
     print("Enter your name and age")


