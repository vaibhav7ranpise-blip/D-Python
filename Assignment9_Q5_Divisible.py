def divisible(num):
    if num % 3 == 0 and num % 5 == 0:
        print("Divisible by both 3 and 5")
    else:
        print("not Divisible by both 3 and 5")

def main():
    No = int(input("Enter the Number :"))
    divisible(No)       

if __name__ == "__main__":
    main()
     
