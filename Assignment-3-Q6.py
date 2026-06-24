print("****************************************")
print("*************Assignment 3***************")
print("*************Question No.6 **************")
print("****************************************")
import sys
def main():
    a = 11
    print("Datatype :",type(a)) # <class 'int'>
    print("Memory Address :",id(a))
    print("Size of a :",sys.getsizeof(a)) 
    print("-----------------------------------------------")

    a = 11.5
    print("Datatype :",type(a)) # <class 'float'>    
    print("Memory Address :",id(a))
    print("Size of a :",sys.getsizeof(a))
    print("-----------------------------------------------")
    a   = "Hello"
    print("Datatype :",type(a)) # <class 'str'>
    print("Memory Address :",id(a))
    print("Size of a :",sys.getsizeof(a))
    print("-----------------------------------------------")


if __name__ == "__main__":
    main()
