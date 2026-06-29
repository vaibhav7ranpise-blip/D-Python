def fact_num(number):
    n = 5
    fact = 1
    while n > 0:
        fact = fact * n
        n = n - 1
    return fact
def main():
    num = int(input("Enter the number to find factorial:"))
    result = fact_num(num)
    print("Factorial of", num, "is:", result)

if __name__ == "__main__":
    main()  