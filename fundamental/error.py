def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return 'zero can not be divided'

print(divide(1,0))

