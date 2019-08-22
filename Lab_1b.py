def fibonacci(n):
    if(n<=1):
        return 1
    
    else:
        return fibonacci(n-1)+fibonacci(n-2)

i = int(input("Enter number: "))
for x in range(0,i):
    print(fibonacci(x))
