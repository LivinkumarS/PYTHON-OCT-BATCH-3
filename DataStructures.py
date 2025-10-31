# a=[1,2,3,"four","five","six",4.5,5.6,False,2,3]

# a[9]=22

# a.append("leo")
# a.extend(["leo",22,33,44])
# a.insert(2,"leo")
# a.remove(4.5)
# a.remove(2)
# a.pop(2)
# a.pop()
# a.pop()


# print(a.index(33))
# print(a.count(33))

# b=[234,43,23,3,324,54534,32]

# b.sort()
# b.reverse()

# print(b)

# Tuple 

# a=(23,54,45,45,1,32,4,2)

# a[3]=999

# print(a[3])
# print(a.index(45))

# person1=("allen",6)
# name,age=person1
# print(name)
# print(age)

# Set 

# s1={21,34,4,43,1,1,1,2,3}
# s2={1,2,3,4,5,6,7}

# print(s1.union(s2))
# print(s1.intersection(s2))
# print(s1.difference(s2))
# print(s2.difference(s1))

lis1=[
    1,
    2,
    3,
    4,
    [
        5,
        6,
        7,
        [
            "eight",
            "nine",
            "ten"
        ]
    ]
]
print(lis1[4][-1][-1][2])