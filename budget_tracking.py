# Import external libraries
import sqlite3


# Defensive Value error check for integers
def value_err(command: str):
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


# Pulling the different categories
def pull_categories():
    """
    Pulls the data out of the category table and puts it in a list

    :returns: All the categories listed
    :rtype: list
    """
    db = sqlite3.connect('budgets')
    cursor = db.cursor()
    category_list = []
    cursor.execute('''SELECT category FROM category ''')
    for row in cursor:
        category_list += row
    db.close()
    return category_list


# Creating a list of numbers that correspond with how many categories there are
def category_number_list():
    """
    Pulls the data out of the category table and counts it from 1 and puts the 
    numbers in a list

    :returns: consecutive numbers
    :rtype: list
    """
    category_list = pull_categories()
    num_list = []
    num = 1
    while(len(category_list) >= num):
        num_list.append(num)
        num += 1
    return num_list


# displaying the different categories
def display_categories():
    """
    Gets data from category list and prints it out for the user

    :returns: A numbered string of all the categories
    :rtype: String
    """
    category_list = pull_categories()
    num = 0
    str_list = """Num\tCategories\n"""
    while(len(category_list)>num):
        str_list += (str(num+1) + "\t" + category_list[num] +"\n")
        num += 1
    return str_list


# Checks if the category entered exist
def category_exists(entered_category: str, category_list: list):
    """
    Checks if the category entered from the user exists in a list

    :param str entered_category: The user's input of their selected category
    :param list category_list: A list with category values

    :returns: A true or false
    :rtype: Boolean
    """
    does_exist = False
    if (entered_category in category_list):
        does_exist = True
    else:
        does_exist = False
    return does_exist


# Adding a new category to the category table
def add_category(id_category, new_category):
    """
    Adds the new category to the category table in the database
    
    :param int id_category: The unique identify ID 
    :param str new_category: The name of the new category
    """
    db = sqlite3.connect('budgets')
    cursor = db.cursor()
    cursor.execute('''INSERT INTO category(category_number, category)
                   VALUES(?,?)''', (id_category, new_category))
    db.commit()
    print("Category has been added to the database\n")
    db.close()


# Organises data from database into seperate lists
def pulling_expenses():
    """
    Pulling all the data from the expenses table and putting the data in 
    seperate appropriate lists

    :returns: All the expenses' ids
    :rtype: list

    :returns: All the expenses' category numbers
    :rtype: list

    :returns: All the expenses' prices
    :rtype: list
    """
    # empty lists to put data in them
    id_list = []
    category_num_list = []
    price_list = []

    # Reading in information from Database
    db = sqlite3.connect('budgets')
    cursor = db.cursor()
    cursor.execute('''SELECT id, category_number, price FROM expenses ''')
    # Putting data in appropriate lists
    for row in cursor:
        id_list.append(row[0])
        category_num_list.append(row[1])
        price_list.append(row[2])
    db.commit()
    db.close()   
    return id_list, category_num_list, price_list


# Displays all the titles of the book
def display_expenses():
    """
    Displays all the expenses from the expenses table
    """
    print("list of expenses")
    print("ID\tCategory_number\t\tPrice")

    # Reading in information from Database
    db = sqlite3.connect('budgets')
    cursor = db.cursor()
    cursor.execute('''SELECT id, category_number, price FROM expenses ''')
    # Displaying data out line by lie
    for row in cursor:
        print('{0}\t{1}\t\t\t{2}'.format(row[0],row[1],row[2]))
        

# Displays expenses if they fall into the selected category
def display_some_expenses(category_num):
    """
    Displays some of the expenses from the expenses table if they fall under 
    the user selected category

    :param int category_num: The user selected category
    """
    print("list of expenses")
    str_expenses = "ID\tCategory_number\t\tPrice\n"
    # Reading in data from database
    db = sqlite3.connect('budgets')
    cursor = db.cursor()
    cursor.execute('''SELECT id, category_number, price FROM expenses 
                             WHERE category_number = ? ''', (category_num,))
    num_counter = 0
    for row in cursor:
        str_expenses += ('{0}\t{1}\t\t\t{2}\n'.format(row[0],row[1],row[2]))
        num_counter += 1
    db.commit()
    db.close()
    if num_counter == 0:
        print("There are no expenses under this category\n")
    else:
        print(str_expenses)


# Adding expenses to the expense table
def add_expense(id, category_number, price):
    """
    Adds the new expense to the expenses table in the database

    :param int id: The unique identify ID 
    :param int category_number: The category number
    :param int price: The cost of the new expense
    """
    db = sqlite3.connect('budgets')
    cursor = db.cursor()
    cursor.execute('''INSERT INTO expenses(id, category_number, price)
                   VALUES(?,?,?)''', (id, category_number, price))
    db.commit()
    print("Expense has been added to the database\n")
    db.close()


# Main section
print("Welcome back to your budget tracker app\n")
# Continuously runs through the menu until the user exits
while True:
    # Lets the user select their choice
    menu = value_err('''Select one of the following options
                         1. Add expense
                         2. View all expenses
                         3. View an expense by a category
                         4. Add income
                         5. View all incomes
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
        print("Exising Categories")
        print(display_categories())

        # Seeing if the user wants to add a new category or use existing one
        menu_1_bool = False
        while menu_1_bool == False:
            menu_for_1 = value_err('''Select one of the following options
                                1. Add expense with an existing category
                                2. Add expense with a new category
                                : ''')
            if menu_for_1 == 1 or menu_for_1 == 2:
                menu_1_bool = True
            
            else:
                print("\nPlease only enter 1 or 2")
        
        # Adding expense with existing category
        if menu_for_1 == 1:
            print("")
            print("Which Category do you want to add your expense to?")
            s1 = """Select the number of the category\n"""
            menu_cate = value_err(f'''{s1}{display_categories()}: ''')

            # Making sure user selected an existing option
            user_bool = False
            options_list = category_number_list()
            while(user_bool == False):
                if(menu_cate in options_list):
                    user_bool = True
                else:
                    print("\nPlease only select a number from the options")
                    menu_cate = value_err(f'''{s1}{display_categories()}: ''')

            # Getting info from user to add to database
            category_list = pull_categories()
            print(f"\nAdding an expense to the {category_list[menu_cate-1]}")
            price = value_err("Please enter how much it costs: ")
            id_list, category_num_list, price_list = pulling_expenses()
            id = len(id_list) + 1
            # Adding expense to expenses table
            add_expense(id, menu_cate, price)

        # Adding new Category to category table & expense to expanses table
        elif menu_for_1 == 2:
            print("\nCreating a new expense category")
            category_list = pull_categories()
            new_category = input("Enter the name of the new category: ")

            # Making sure the category doesnt already exist
            while(category_exists(new_category, category_list) == True):
                print("\nPlease enter a name that does not already exist")
                new_category = input("Enter the name of the new category: ")
            
            # Adding the category to the Category Table
            id_category = len(category_list) + 1
            add_category(id_category, new_category)

            # Adding expense to expenses table
            category_list = pull_categories()
            print(f"Adding an expense to the {category_list[id_category-1]}")
            id_list, category_num_list, price_list = pulling_expenses()
            id = len(id_list) + 1
            price = value_err("Please enter how much it costs: ")
            add_expense(id, id_category, price)

    # Allows the user to view all their expenses
    elif menu == 2:
        display_expenses()
        print("")

    # Allows user to select what expenses they want to view
    elif menu == 3:
        # Selecting the category
        print("\nWhich category do you want to view you expenses from?")
        s1 = """Select the number of the category\n"""
        menu_cate = value_err(f'''{s1}{display_categories()}: ''')
         # Making sure user selected an existing option
        user_bool = False
        options_list = category_number_list()
        while(user_bool == False):
            if(menu_cate in options_list):
                user_bool = True
            else:
                print("\nPlease only select a number from the options")
                menu_cate = value_err(f'''{s1}{display_categories()}: ''')

        print("")       
        display_some_expenses(menu_cate)

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

    # Allows user to see their budget for a selected category
    elif menu == 8:
        pass

    # Allows user to set finacial goals 
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
