#Fibonacci Sequence

'''Write a Python program to get the Fibonacci series between 0 to 50

Note : The Fibonacci Sequence is the series of numbers :

0, 1, 1, 2, 3, 5, 8, 13, 21, ....

Every next number is found by adding up the two numbers before it.

Expected Output : 1 1 2 3 5 8 13 21 34'''

num1=0
num2=1
i=0

print(num2)

while True:
    F_num=num1+num2
    num1=num2
    num2=F_num
    i=i+1
    if F_num>=50:
        break
    print(F_num)
    
