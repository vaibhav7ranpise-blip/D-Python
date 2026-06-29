def sum(n):
    if n == 0:
        return 0
    total = 0
    while n > 0:
        digit = n % 10
        total =  total + digit
        n = n // 10
    return total
def main(): 
    
    n = int(input("Enter a number: "))
    result = sum(n)
    print("Sum of digits in", n, "is:", result)

if __name__ == "__main__":
    main()  