# i=0

# while i<5:
#     print("Step1")
#     print("Step2")
#     print("Step3")
#     print("-------------")
#     i+=1

# print("Final step")
    
# No of times:1,2,3,4,5
# i value: 0,1,2,3,4,5

# 1-50


# i=1
# while i<=50:
#     print(i)
#     i+=1

# i = 50            

# while i >= 1:     
#     print(i)
#     i = i - 1

# str1="Hello world"
# print(str1[7])

# a="Livinkumar"

# for char in range(1,10,3):
#     print(char)
#     print("-------------")
    
# i=10 
# while i<=20:
#     if i==14:
#         i+=1
#         continue
#     print(i)
#     i+=1

# print("Loop ended!")

# i=10,11,12,13,14,15,16......20,21
# 10,11,12,13,15...20


# for i in range(10):
#     if i==5:
#         break
#     print(i)

# for i in range(5):
#     print("Hello")

secretNumber=33

while True:
    guessedNumber=int(input("Guess a number : "))
    if guessedNumber==secretNumber:
        print("You won!")
        break
    else:
        print("Try again!")

# for i in range(1000):
#     guessedNumber=int(input("Guess a number : "))
#     if guessedNumber==secretNumber:
#         print("You won!")
#         break
#     else:
#         print("Try again!")