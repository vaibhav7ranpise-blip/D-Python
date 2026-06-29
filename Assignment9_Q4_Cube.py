def Cube(No):
    if No != 0:
        No = No * No * No
    print ("Cube of NUmber is :",No)

def main():
    num = int(input("Enter the number for conver in Cube:"))
    Cube(num)

if __name__ == "__main__":
    main()
    