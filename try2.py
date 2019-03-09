# function 1
def string_length(mystring):
    if type(mystring) == int:
        return "Sorry integers don't have length"
    elif type(mystring) == float:
        return "Sorry floats don't have length"
    else:
        return len(mystring)


print(string_length("hello"))
print(string_length(10))
print(string_length(10.99))


# function 2
def convert(original, coefficient):
    return original * coefficient


print(convert(10, 0.3048))


# function 3
def convert(original, coefficient=0.3048):
    return original * coefficient


print(convert(10))
print(convert(10, 0.62))


# function 4
def cel_to_fah(value):
    return (value * (9 / 5)) + 32


print(cel_to_fah(10))
