def multiplicationTable(No):
    if No != 0:
        for i in range(1, 11):
            print(No * i)
def main():
    num = int(input("Enter the number for multiplication table:"))
    multiplicationTable(num)

if __name__ == "__main__":
    main()
