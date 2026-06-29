b = bytearray([65, 66, 67])
b[0]=97
print(b)  # Output: b'ABC' 

"""def alphabates():
    for i in range(65, 97):
        print(chr(i), end=" ")

alphabates() 
# Output: A B C D E F G H I J K L M N O P Q R S T U V W X Y Z


x= None
print(type(x))   # Output: None
print(x == False)         # Output: None


def fun():
    pass
fun()  # Output: None
"""
x = 100
def squere():
    global x
    print("global first :",x)   
    x = x+1 
    print("global x :",x)  # Output: global x : 101
squere()  # Output: Squere of is : 25


