def findodd(number):
    number != 0
    for i in range(1, number +1):
        if i % 2 != 0:
            print(i)
def main():
    num = int(input("Enter the number to find odd numbers:"))
    findodd(num)

if __name__ == "__main__":
    main()  
