'''Write a Python program to square the elements of a list using map() function.


Sample List:  [4, 5, 2, 9]

Square the elements of the list:

[16, 25, 4, 81]'''

num = [4, 5, 2, 9]

def square(a):
    return a**2

result = map(square,num)

print(list(result))