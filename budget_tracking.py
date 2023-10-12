# Import external libraries
import sqlite3


# Defensive Value error check for integers
def value_error_int(command: str):
    '''
    Checks if user entered the an integer if not continuously asks until 
    they enter an integer

    :param str command: The command/options given to the user

    :returns: The option the user selected
    :rtype: int
    '''
    while True:
        try:
            value_entered = int(input(command))
            break
        except ValueError:
            print("\nPlease only enter a number")
    return value_entered


# Main section
print("Welcome back to your budget tracker app\n")
# Continuously runs through the menu until the user exits
while True:
    # Lets the user select their choice
    menu = value_error_int('''Select one of the following options
                         1. Add or Update expenses
                         2. View all expenses
                         3. View an expense by a category
                         4. Add or Update income
                         5. View income
                         6. View income by category
                         7. Set budget for a category 
                         8. View budget for a category
                         9. Set financial goals
                         10. View progress towards financial goals
                         11. Quit
                         : ''')
    print("")

    # Allows the user to add or update expenses to the expenses table
    if menu == 1:
        pass
    
    # Allows the user to view all their expenses
    elif menu == 2:
        pass

    # Allows user to select what expenses they want to view
    elif menu == 3:
        pass
    
    # Allows user to add or update their income
    elif menu == 4:
        pass
    
    # Allows user to view their income from a selected category
    elif menu == 5:
        pass

    # Sets a budget for a specific category
    elif menu == 6:
        pass

    # Set their budget for a selected category
    elif menu == 7:
        pass

    # Allows user to see their bidget for a selected category
    elif menu == 8:
        pass

    # Allows user to set or update finacial goals 
    elif menu == 9:
        pass

    # Allows user to view their progress towords their finacial goals
    elif menu == 10:
        pass

    # Exits the program
    elif menu == 11:
        print("Goodbye!")
        exit()

    # Lets user know they have made an invalid choice
    else:
        print("\nYou have entered an invalid number, Please try again")
