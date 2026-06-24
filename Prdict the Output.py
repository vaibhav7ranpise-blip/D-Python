"""b = bytes([65, 66, 67])
print(b)  # Output: b'ABC' """

def alphabates():
    for i in range(65, 255):
        print(chr(i), end=" ")

alphabates() 
# Output: A B C D E F G H I J K L M N O P Q R S T U V W X Y Z