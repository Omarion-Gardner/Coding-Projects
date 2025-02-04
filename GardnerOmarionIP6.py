import sys
def welcome():
    print("""Welcome to the Spice Tracker App 
 
Spices: None 
Options: 
A) Add a new spice 
D) Delete a spice 
S) Sort all spices 
Q) Quit """)

#Omarion Gardner
#Independent Programming 6
#11/9/2023

    

def addSpice(name):   #Creates a function that adds spices into a list
    a=input("Please enter the spice to add: ")   #Input statement prompting user to enter spices
    name.append(a)
    return("Added",a)


def delSpice(name):   #Creates a function that deletes spices from the list
    d=input("Please enter the spice to delete: ")  #Input statement prompting user to delete spices
    if d in name:
        name.remove(d)
        return("Deleted",d)

    else:
        return("Could not remove",d,",it was not found!") #Error message if spice was not entered by user

def sortSpice(name):  #Creates a function that sorts the spices
    list.sort(name)
    return "Sorted spices."


def main():    #Main function to call other function
    welcome()
    spices=[]     #Empty list of spices
    while True:          #Used a while statement to validate user's input
        choice=input("Please choose from the above options: ")    #Assigned the variable "choice" to tell program what to do based of what the user entered
        if choice=="A" or choice=="a":
            print(addSpice(spices))
            
        elif choice=="D" or choice=="d":
            print(delSpice(spices))

        elif choice=="Q" or choice=="q":
            print("Happy cooking!")
            sys.exit()     #Exits system if the user enters "Q" or "q"

        elif choice=="S" or choice=="s":
            print(sortSpice(spices))
        else:
            print("Sorry,",choice,",is not a valid option.")   #Error message if the user enters a choice that's not an option
            
            
if __name__=="__main__":
    main()
