def fun(number):
    if number > 1:
        for i in range(1, number):
            if (number % i) == 0:
                print(number, "is not a prime number")
                break
        else:
            print(number, "is a prime number")
def main():
    number = int(input("Enter a number: "))
    fun(number)

if __name__ == "__main__":
    main()