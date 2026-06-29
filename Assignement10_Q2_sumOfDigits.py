def sumOffirstNnaturalNumber(No):
    sum = 0
    while No > 0:
        sum = sum + No
        print("Sum of digits:", sum)
        No = No - 1
        print("Remaining number:", No)  
    return sum
def main():
    num = int(input("Enter the number to find sum of digits:"))
    result = sumOffirstNnaturalNumber(num)
    print("Sum of digits:", result)

if __name__ == "__main__":
    main()
    