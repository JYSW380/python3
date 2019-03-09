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

myfile = open("employee.txt", "w")
myfile.write("mike")
myfile.close()

myfile = open("employee.txt", "w")
myfile.write("mike\nhello")
myfile.close()

myfile = open("employee.txt", "a")
myfile.write("\ntoday")
myfile.close()

myfile = open("employee.txt", "a+")  # a+ both read and write
myfile.seek(0)  # need seek(0) to put cursor at beginning of text file because with a+ mode
print(myfile.read())  # cursor put the end of the file
myfile.write("\nhappy")
myfile.close()


number = [1, 2, 3]
newfile = open("number.txt", "w")
for i in number:
    newfile.write(str(i) + "\n")
newfile.close()