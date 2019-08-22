list1=[]
n=int(input("Enter the number of elements:"));
for i in range(0,n):
    ele=int(input())
    list1.append(ele)
list2=[]
for i in list1:
    if(i%2==0):
        list2.append(i)
for i in list2:
    print(i)
