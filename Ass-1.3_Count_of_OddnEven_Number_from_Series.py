'''Write a Python program to count the number of even and odd numbers from a series of numbers.

Sample numbers : numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)   

Expected Output :

Number of even numbers : 4

Number of odd numbers : 5'''

numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
Odd=0
Even=0
for i in numbers:
    if i%2==0:
        Even=Even+1
    else:
        Odd=Odd+1
print('Number of Even Numbers : ',Even)
print('Number of Odd Numbers : ',Odd)