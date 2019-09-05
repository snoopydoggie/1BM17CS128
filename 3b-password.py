import string
import random
i=1
def randompassword():
    chars1=string.ascii_uppercase
    chars2=string.ascii_lowercase
    chars3=string.digits
    chars4=string.punctuation
    size=random.randint(2,4)
    str1=''.join(random.choice(chars1) for x in range(1,size))
    str2=''.join(random.choice(chars2) for x in range(1,size))
    str3=''.join(random.choice(chars3) for x in range(1,size))
    str4=''.join(random.choice(chars4) for x in range(1,size))
    result=list(str1+str2+str3+str4)
    random.shuffle(result)
    return ''.join(result)
    
while i!=-1:
    print(randompassword())
    print('Enter 1 to generate password and -1 to exit')
    i=int(input())
