even_list = []
list_As_str = input("Enter the list of numbers separated by space: ")
list_ip = list_As_str.split(' ')
for e in list_ip:
    n = int(e)
    if n%2==0:
        even_list.append(n)
print(even_list)    
