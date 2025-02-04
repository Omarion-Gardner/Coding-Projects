#Omarion Gardner
#Independent Programming 5
#10/26/2023
import sys

def Welcome():  # Welcomes user to program
    print("Welcome to the CSU English plural word maker!")

def getValidInput():  # Validates the user's input and return error message if input doesn't meet requirements
    while True:
        v = "aeiou"
        a = input("Please enter a word with no spaces or numeric digits (or q to quit): ")
        a = a.lower()  # converts input to lowercase

        if a == "q":  # check if user wants to quit
            return a

        if not a.isalpha() or a.isspace():  # Returns error message if input isn't alphabets or has spaces
            print("This word has a number or space in it, please try again.")
            continue

        # Pluralization rules
        if a[-1] == "s" or a[-2:] == "ss" or a[-2:] == "sh" or a[-2:] == "ch" or a[-1] == "x" or a[-1] == "z":
            print(a + "es")
        elif a[-1] == "y" and a[-2] not in v:  # If word ends with 'y' and doesn't have a vowel before it, replace 'y' with 'ies'
            print(a[:-1] + "ies")
        else:
            print(a + "s")
        break  # exit loop after a valid input

def main():
    Welcome()
    
    while True:  # Keep asking until the user wants to quit
        result = getValidInput()
        if result == "q":  # If the user inputs the letter q, the program will print goodbye and exit
            print("Goodbye!")
            sys.exit()

if __name__ == "__main__":
    main()

    
