'''Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.

Sample String : 'The quick Brow Fox'

Expected Output :

No. of Upper case characters : 3

No. of Lower case Characters : 12'''

string1='The quick Brow Fox'

upper=[]
lower=[]


def check_alpha(s):
    for i in s:
        if i.isupper():
            upper.append(i)
        elif i.islower():
            lower.append(i)
    print('No. of Upper case characters : ',len(upper))
    print('No. of Lower case Characters : ',len(lower))
    return 

result=check_alpha(string1)


