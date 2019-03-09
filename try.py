address = ["becky street", 7800, "japan"]
pins = {"mark": 1234, "joe": 1111, "alice": 4567}

print(address[0], address[1])
# print(len(address))
# print(type(address[1]))
# print(address[0:2])  slicing is upper bound exclusive
# print(address[-2])

# address.append("usa")
# address.remove("usa")
# print(address)
# print(dir(address))
# print("Python is fun"[-3:][-1])

# person = {"name": "jack", "surname": "smith", "age": "29"}
# person.pop("name")
# person["name"] = "hello"
# person["age"] = 90
# print(person)

# keys = ["a", "b", "c"]
# values = [1, 2, 3]
# mydirct = dict(zip(keys, values))
# print(mydirct)

pin = int(input("enter your pin"))

def find_in_file(f):
    myfile = open("sample.txt")
    fruit = myfile.read()
    fruit = fruit.splitlines()
    if f in fruit:
        return "that fruit is in the list"
    else:
        return "so such thing"


if pin in pins.values():
    fruit = input("enter fruit")
    print(find_in_file(fruit))
else:
    print("incorrect pin")
    print("this can be accessed by only: ")
    for key in pins.keys():
        print(key)



