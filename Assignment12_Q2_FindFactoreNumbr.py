def findFactorNumber(num):
    factors = []
    for i in range(1, num + 1):
        if num % i == 0:
            factors.append(i)
    return factors
def main():
    num = int(input("Enter a number: "))
    factors = findFactorNumber(num)
    print(f"The factors of {num} are: {factors}")   

if __name__ == "__main__":  
    main()