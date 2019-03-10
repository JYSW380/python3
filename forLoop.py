# example 1
mylist = "trick"
for i in mylist:
    print(i)

# example 2
mylist = ["trick"]
for i in mylist:
    print(i)

# example 3
mylist = ["Terribly Tricky"]
for word in mylist:

    for letter in word[-6:]:
        print(letter)

# example 4
mylist = [1, 2, 3, 4, 5]
for i in mylist:
    if i > 2:
        print(i)

# example 5
myfile = open("fruits.txt")
fruit = myfile.read()
myfile.close()
fruit = fruit.splitlines()
for item in fruit:
    print(len(item))

# example 6
correct_pw = "123"
name = input("enter your name: ")
surname = input("enter your surname: ")
pw = input("please enter a password: ")
while pw != correct_pw:
    pw = input("please enter a password: ")

print("hi %s you are logged in" % name)  # string formatting
print("hi %s %s, you are logged in" % (name, surname))

# example 7
a = ['a', 'b', 'c']
b = [1, 2, 3]
for i, j in zip(a, b):
    print("%s is %s" % (i, j))



