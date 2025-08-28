def square(number):
    return number * number

numbers = [1, 2, 3, 4]
squared_numbers = list(map(square, numbers))

print(squared_numbers)