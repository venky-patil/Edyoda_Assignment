'''Write a Python function to sum all the numbers in a list.

Sample List : (8, 2, 3, 0, 7)

Expected Output : 20

Explanation:

Summation should like 8+2+3+0+7 = 20'''

list1=(8, 2, 3, 0, 7)

total=0

def sum_of_list(l):
    global total
    for i in l:
        total=total+i
    
    return total
    
result=sum_of_list(list1)
print('Sum of List Elements :',result)