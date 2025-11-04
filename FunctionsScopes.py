# def printSteps():
#     print("Step1")
#     print("Step2")
#     print("Step3")
    
# printSteps()
# printSteps()
# printSteps()


# def sum(a,b,c):
#     print("Welcome!")
#     print(a+b+c)

# sum(7,8,10)
# sum(5,5,"5")

# sum(c=10,a=19,b=0)

# def sum(a,b,c=10):
#     print(a+b+c)

# sum(4,5)
# sum(4,5,21)

# def sum(*numbers):
#     ans=0
#     for num in numbers:
#         ans+=num
#     print(ans)

# sum(56,324,45,23,45,23,34,23)
    
# def printSteps():
#     print("Step1")
#     print("Step2")
#     print("Step3")

# a=printSteps()
# print(a)

# def product(a,b):
#     print(a*b)
#     return a*b

# print(product(9,10))

# Scopes

a=10

def dummy():
    a=15
    print("The value of a from inside of the function:",a)

dummy()

print("The value of a from outside of the function:",a)
