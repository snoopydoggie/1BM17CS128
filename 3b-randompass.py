import random
import string
def randomString():
    pw = string.ascii_letters + string.digits + string.punctuation
    size = random.randint(8,12)
    return ''.join(random.choice(pw) for i in range(size))
print("Random String with the combination of lowercase and uppercase letters")
print ("Random String is ", randomString() )

