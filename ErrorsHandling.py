print("Hello")
print("Hi")

# if True:
#     print("Welcome")

# print(8/0) #zeroDivError
# print(8+"*")


try:
    a=int(input("Enter number1: "))
    b=int(input("Enter number2: "))
    print(a/b)
except ZeroDivisionError:
    print("Invalid expression")
except ValueError:
    print("Invalid Input")
finally:
    print("Final Step")



