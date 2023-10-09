'''Write a Python program to reverse a string.

Sample String : "1234abcd"

Expected Output : "dcba4321"'''

string1="1234abcd"

def Reverse_string(s):
    r_string=s[::-1]
    return r_string

result=Reverse_string(string1)

print('Reverse String :',result)