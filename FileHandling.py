file=open('FileHandling.txt','r')

# print(file)
# print(file.read())
# print(file.readline())
# print(file.readline())

print(file.readlines()[6])

file.close()


# file=open('FileHandling.txt','w')

# content="The new content has arrived!.\nOld content vanished!"

# file.write(content)

# file.close()

# file=open('FileHandling.txt','a')

# content="\nThe new content has arrived!.\nOld content vanished!"

# file.write(content)

# file.close()



# print("Hello.\n HHi")