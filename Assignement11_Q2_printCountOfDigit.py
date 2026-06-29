"""def countdigit(n):
    if n == 0:
        return 1
    count = 0
    while n > 0:
        n = n // 10
        count = count + 1
    return count"""
def main():

    n = int(input("Enter a number: "))
    if n == 0:
        return 1
    count = 0
    while n > 0:
        n = n // 10
        count = count + 1
    print("Number of digits in", n, "is:", count)

if __name__ == "__main__":
    main()