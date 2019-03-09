# way 1
myfile = open("fruits.txt")
fruit = myfile.read()
myfile.close()
fruit = fruit.splitlines()
for f in fruit:
    print(f)

# way 3
myfile = open("fruits.txt", "r")
fruit = myfile.read()
myfile.close()
print(fruit)
