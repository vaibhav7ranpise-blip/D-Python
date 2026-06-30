def check_vowel(char):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return char in vowels

def main():
    char = input("Enter a character: ")
    if check_vowel(char):
        print(f"{char} is a vowel.")
    else:
        print(f"{char} is not a vowel.") 

if __name__ == "__main__":  
    main()
    