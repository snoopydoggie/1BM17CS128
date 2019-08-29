import re
def func(str1):
    s=" "
    li=list(re.split(r'(\s+)',str1))
    lis = li.reverse()
    for i in li:
        s+=i
    return s
def func1(str1):
    s=" "
    for i in str1:
        s=i+s
    print(" ",s)
str1=input("string:\n")
s1=func(str1)
print(s1)
func1(s1)
         
