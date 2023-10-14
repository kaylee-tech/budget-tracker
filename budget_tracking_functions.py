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

    :returns: All the categories numbers
    :rtype: list
    """
    db = sqlite3.connect('budgets')
    cursor = db.cursor()
    category_list = []
    category_number_list = []
    cursor.execute('''SELECT category_number, category FROM category
                   ORDER BY category_number''')
    for row in cursor:
        category_list.append(row[1])
        category_number_list.append(row[0])
    db.commit()
    db.close()
    return category_list, category_number_list


# displaying the different categories
def display_categories():
    """
    Gets data from category list and prints it out for the user

    :returns: A numbered string of all the categories
    :rtype: String
    """
    category_list, category_num_list = pull_categories()
    num = 0
    str_list = """Num\tCategories\n"""
    while(len(category_list)>num):
        str_list += (f"{category_num_list[num]}\t{category_list[num]}\n")
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


# Displays all the expenses from the expenses table
def display_expenses():
    """
    Displays all the expenses from the expenses table
    """
    print("list of expenses")
    str_expenses = "ID\tCategory_number\t\tPrice\n"

    # Reading in information from Database
    db = sqlite3.connect('budgets')
    cursor = db.cursor()
    cursor.execute('''SELECT id, category, price FROM expenses 
                   INNER JOIN category ON 
                   category.category_number = expenses.category_number''')
    # Displaying data out line by lie
    num_counter = 0
    for row in cursor:
        str_expenses += '{0}\t{1}\t\t\t{2}\n'.format(row[0],row[1],row[2])
        num_counter += 1
    if num_counter == 0:
        print("There are no expenses in the table right now\n")
    else:
        print(str_expenses)
    db.commit()
    db.close() 
        

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


# Organises data from database into seperate lists
def pulling_income():
    """
    Pulling all the data from the income table and putting the data in 
    seperate appropriate lists

    :returns: All the incomes' ids
    :rtype: list

    :returns: All the incomes' category numbers
    :rtype: list

    :returns: All the incomes' amounts
    :rtype: list
    """
    # empty lists to put data in them
    id_list = []
    category_num_list = []
    amount_list = []

    # Reading in information from Database
    db = sqlite3.connect('budgets')
    cursor = db.cursor()
    cursor.execute('''SELECT id, category_number, amount FROM income ''')
    # Putting data in appropriate lists
    for row in cursor:
        id_list.append(row[0])
        category_num_list.append(row[1])
        amount_list.append(row[2])
    db.commit()
    db.close()   
    return id_list, category_num_list, amount_list


# Displays the incomes from the income table
def display_income():
    """
    Displays all the income records from the income table
    """
    print("list of incomes")
    str_income ="ID\tCategory_number\t\tamount\n"

    # Reading in information from Database
    db = sqlite3.connect('budgets')
    cursor = db.cursor()
    cursor.execute('''SELECT id, category, amount FROM income 
                   INNER JOIN category ON 
                   category.category_number = income.category_number''')

    # Displaying data out line by lie
    num_counter = 0
    for row in cursor:
        str_income += '{0}\t{1}\t\t\t{2}\n'.format(row[0],row[1],row[2])
        num_counter += 1
    if num_counter == 0:
        print("There is no income in this table\n")
    else:
        print(str_income)
    db.commit()
    db.close() 


# Displays incomes if they fall into the selected category
def display_some_incomes(category_num):
    """
    Displays some of the incomes from the income table if they fall under 
    the user selected category

    :param int category_num: The user selected category
    """
    print("list of incomes")
    str_income = "ID\tCategory_number\t\tamount\n"
    # Reading in data from database
    db = sqlite3.connect('budgets')
    cursor = db.cursor()
    cursor.execute('''SELECT id, category_number, amount FROM income 
                            WHERE category_number = ? ''', (category_num,))
    num_counter = 0
    for row in cursor:
        str_income += '{0}\t{1}\t\t\t{2}\n'.format(row[0],row[1],row[2])
        num_counter += 1
    db.commit()
    db.close()
    if num_counter == 0:
        print("There is no income under this category\n")
    else:
        print(str_income)


# Adding income to the income table
def add_income(id, category_number, amount):
    """
    Adds the new income to the income table in the database

    :param int id: The unique identify ID 
    :param int category_number: The category number
    :param int amount: The cost of the new income
    """
    db = sqlite3.connect('budgets')
    cursor = db.cursor()
    cursor.execute('''INSERT INTO income(id, category_number, amount)
                   VALUES(?,?,?)''', (id, category_number, amount))
    db.commit()
    print("income has been added to the database\n")
    db.close()


# Organises data from database into seperate lists
def pulling_budgets():
    """
    Pulling all the data from the budget table and putting the data in 
    seperate appropriate lists

    :returns: All the budgets' ids
    :rtype: list

    :returns: All the budgets' category numbers
    :rtype: list

    :returns: All the expenses budgets' limits
    :rtype: list
    """
    # empty lists to put data in them
    id_list = []
    category_num_list = []
    bud_limit = []

    # Reading in information from Database
    db = sqlite3.connect('budgets')
    cursor = db.cursor()
    cursor.execute('''SELECT id, category_number, expenses_budget
                    FROM budget ''')
    # Putting data in appropriate lists
    for row in cursor:
        id_list.append(row[0])
        category_num_list.append(row[1])
        bud_limit.append(row[2])
    db.commit()
    db.close()   
    return id_list, category_num_list, bud_limit


# Displays the budgets from the budget table
def display_budgets():
    """
    Displays all the budget records from the budget table
    """
    print("list of budgets")
    st1 = "Category_number"
    st2 = "Expense Budget"
    str_bud =f"ID\t{st1}\t\t{st2}\n"

    # Reading in information from Database
    db = sqlite3.connect('budgets')
    cursor = db.cursor()
    cursor.execute('''SELECT id, category, expenses_budget FROM budget 
                   INNER JOIN category ON 
                   category.category_number = budget.category_number''')
    # Displaying data out line by lie
    num_counter = 0
    for row in cursor:
        str_bud += '{0}\t{1}\t\t\t{2}\n'.format(row[0],row[1],row[2])
        num_counter += 1
    db.commit()
    db.close() 
    if num_counter == 0:
        end_str = "There are no budget records in this table\n"
        return end_str
    else:
        return str_bud
   

# Displays budget records if they fall into the selected category
def display_some_budgets(category_num):
    """
    Displays some of the budget records from the budget table if they fall 
    under the user selected category

    :param int category_num: The user selected category
    """
    print("list of budgets")
    st1 = "Category_number"
    st2 = "Expense Budget"
    str_bud =f"ID\t{st1}\t\t{st2}\n"
    # Reading in data from database
    db = sqlite3.connect('budgets')
    cursor = db.cursor()
    cursor.execute('''SELECT id, category_number, expenses_budget FROM budget
                   WHERE category_number = ? ''', (category_num,))
    num_counter = 0
    for row in cursor:
        str_bud += '{0}\t{1}\t\t\t{2}\n'.format(row[0],row[1],row[2])
        num_counter += 1
    db.commit()
    db.close()
    if num_counter == 0:
        print("There are no budget records under this category\n")
    else:
        print(str_bud)


# Displays the empty budgets
def display_empty_budgets():
    """
    Displays the categories that have no budget from the budget table 
    """
    id_list, budget_category, budget_cost = pulling_budgets()
    cate, options_list = pull_categories()
    category_list, num_list = pull_categories()
    space_for_new_bud = True
    if len(id_list) == len(options_list):
        space_for_new_bud = False

    # Printing out list of empty budget categories
    if(space_for_new_bud == True):
        print("list of empty budgets")
        st1 = "Category_number"
        str_bud =f"ID\t{st1}\n"

        num_checker = 0
        num_count = 0
        while len(options_list) > num_count:
            if options_list[num_count] in budget_category:
                pass
            else: 
                num_bud = str(num_count+1)
                str_bud += (f"{num_bud}\t{category_list[num_count]}\n")
                num_checker += 1   
            num_count += 1
    # Results
    if num_checker > 0:
        return str_bud
    else:
        str_empty = "list of empty budgets\nThere are no empty budgets"
        return str_empty
               

# Creating a list of numbers that correspond with how many categories there are
def empty_budget_number_list():
    """
    Pulls the data out of the numbers corresponding with the category table and
    records corresponding number of category not in budget table

    :returns: numbers that represent categories not in the budget table
    :rtype: list
    """
    id_list, budget_category, budget_cost = pulling_budgets()
    cate, options_list = pull_categories()
    num_list = []

    num_count = 0
    while len(options_list) > num_count:
        if options_list[num_count] in budget_category:
            pass
        else:
            num_list.append(num_count + 1)
        num_count += 1
    return num_list
   

# Adding budget to the budget table
def add_budget(id, category_number, budget):
    """
    Adds the new budget to the budget table in the database

    :param int id: The unique identify ID 
    :param int category_number: The category number
    :param int budget: The amount set of the new budget
    """
    db = sqlite3.connect('budgets')
    cursor = db.cursor()
    cursor.execute('''INSERT INTO budget(id, category_number, expenses_budget) 
                   VALUES(?,?,?)''', (id, category_number, budget))
    db.commit()
    print("budget has been added to the database\n")
    db.close()


# Updating a budget record in the budget table
def update_budget(id, budget):
    """
    Updates a budget record of the budget table in the database

    :param int id: The unique identify ID of budget getting updated
    :param int budget: The new amount of the updated budget
    """
    db = sqlite3.connect('budgets')
    cursor = db.cursor()
    cursor.execute('''UPDATE budget SET expenses_budget=? WHERE id=?''', 
                   (budget, id))
    db.commit()
    print("budget has been updated in the database\n")
    db.close()


# Organises data from database into seperate lists
def pulling_goals():
    """
    Pulling all the data from the goals table and putting the data in 
    seperate appropriate lists

    :returns: All the goals' ids
    :rtype: list

    :returns: All the goals' category numbers
    :rtype: list

    :returns: All the goals profit amount' limits
    :rtype: list
    """
    # empty lists to put data in them
    id_list = []
    category_num_list = []
    amount_limit = []

    # Reading in information from Database
    db = sqlite3.connect('budgets')
    cursor = db.cursor()
    cursor.execute('''SELECT id, category_number, amount FROM goals ''')
    # Putting data in appropriate lists
    for row in cursor:
        id_list.append(row[0])
        category_num_list.append(row[1])
        amount_limit.append(row[2])
    db.commit()
    db.close()   
    return id_list, category_num_list, amount_limit


# Displays the financial goals from the goals table
def display_goals():
    """
    Displays all the financial goal records from the goal table
    """
    print("list of financial goals")
    st1 = "Category_number"
    st2 = "Amount of profit"
    str_bud =f"ID\t{st1}\t\t{st2}\n"

    # Reading in information from Database
    db = sqlite3.connect('budgets')
    cursor = db.cursor()
    cursor.execute('''SELECT id, category, amount FROM goals 
                   INNER JOIN category ON 
                   category.category_number = goals.category_number''')
    # Displaying data out line by lie
    num_counter = 0
    for row in cursor:
        str_bud += '{0}\t{1}\t\t\t{2}\n'.format(row[0],row[1],row[2])
        num_counter += 1
    db.commit()
    db.close() 
    if num_counter == 0:
        end_str = "There are no financial goal records in this table\n"
        return end_str
    else:
        return str_bud


# Displays the empty financial goals
def display_empty_goals():
    """
    Displays the categories that have no financial goals from the goals table 
    """
    id_list, goal_category, amount_profit = pulling_goals()
    cate, options_list = pull_categories()
    space_for_new_bud = True
    if len(id_list) == len(options_list):
        space_for_new_bud = False

    # Printing out list of empty goals categories
    if(space_for_new_bud == True):
        print("list of empty goals")
        st1 = "Category_number"
        str_bud =f"ID\t{st1}\n"

        num_checker = 0
        num_count = 0
        while len(options_list) > num_count:
            if options_list[num_count] in goal_category:
                pass
            else: 
                num_bud = str(num_count+1)
                str_bud += (f"{num_bud}\t{cate[num_count]}\n")
                num_checker += 1   
            num_count += 1
    # Results
    if num_checker > 0:
        return str_bud
    else:
        str_empty = "list of empty goals\nThere are no empty goals"
        return str_empty
    

# Creating a list of numbers that correspond with how many categories there are
def empty_goals_number_list():
    """
    Pulls the data out of the numbers corresponding with the category table and
    records corresponding number of category not in goals table

    :returns: numbers that represent categories not in the goals table
    :rtype: list
    """
    id_list, goals_category, amount_profit = pulling_goals()
    cate, options_list = pull_categories()
    num_list = []

    num_count = 0
    while len(options_list) > num_count:
        if options_list[num_count] in goals_category:
            pass
        else:
            num_list.append(num_count + 1)
        num_count += 1
    return num_list


# Adding goal to the goals table
def add_goal(id, category_number, amount_profit):
    """
    Adds the new goal to the goals table in the database

    :param int id: The unique identify ID 
    :param int category_number: The category number
    :param int amount_profit: The amount profit from actual expense vs budget
    """
    db = sqlite3.connect('budgets')
    cursor = db.cursor()
    cursor.execute('''INSERT INTO goals(id, category_number, amount) 
                   VALUES(?,?,?)''', (id, category_number, amount_profit))
    db.commit()
    print("goal has been added to the database\n")
    db.close()


# Updating a financial goal record in the goals table
def update_goal(id, amount_profit):
    """
    Updates a financial goals record of the goals table in the database

    :param int id: The unique identify ID of financial goal getting updated
    :param int amount_profit: The new amount of the updated amount_profit
    """
    db = sqlite3.connect('budgets')
    cursor = db.cursor()
    cursor.execute('''UPDATE goals SET amount=? WHERE id=?''', 
                   (amount_profit, id))
    db.commit()
    print("financial goal has been updated in the database\n")
    db.close()


# Displays the financial goals' progress from the goals table
def display_goals_progress():
    """
    Displays all the financial goals' progress records from the goal table
    """
    print("list of financial goals progress")
    st1 = "Category_number"
    st2 = "Amount of profit wanted"
    st3 = "Progress"
    str_bud =f"ID\t{st1}\t\t{st2}\t\t{st3}\n"
    
    # Checking that an expense, budget and goal exists for that category
    cate, num_list = pull_categories()

    num_counter = 0
    num_checker = 1
    num_progress_exists = 0
    while(len(cate) > num_counter):
        if(get_budget(num_checker)>0 and get_expense(num_checker)>0 and 
           get_goal_amount1(num_checker)>0):
            
            # Getting difference between budget and expenses
            prof = get_goal_amount1(num_checker)
            prog_diff = get_budget(num_checker)-get_expense(num_checker)

            # If the user is over budget and in negative not profit
            if prog_diff < 0:
                prog_diff = prog_diff * -1 
                prog_diff = prog_diff + get_goal_amount1(num_checker)
                pro_int = get_goal_amount1(num_checker)/prog_diff
                pro_int = pro_int * 100
            else:
                pro_int = prog_diff/get_goal_amount1(num_checker)
                pro_int = pro_int * 100
            pro = str(pro_int)
            str_bud += f"{num_counter}\t{num_checker}\t\t\t{prof}\t\t\t\t{pro}"
            num_progress_exists += 1

        num_checker += 1
        num_counter += 1

    if num_progress_exists == 0:
        print(f"{str_bud}There are no progress goals")
    else:
        print(str_bud)    


# Gets expenses for a category
def get_expense(category):
    expense_price = 0
    db = sqlite3.connect('budgets')
    cursor = db.cursor()
    cursor.execute('''SELECT id, category_number, price FROM expenses
                   WHERE category_number=? ''', (category,))
    for row in cursor:
        expense_price += row[2]
    db.commit()
    db.close()
    return expense_price  


# Gets goal amount for a category
def get_goal_amount1(category):
    goal_amount = 0
    db = sqlite3.connect('budgets')
    cursor = db.cursor()
    cursor.execute('''SELECT amount FROM goals 
                   WHERE category_number=? ''', (category,))
    for row in cursor:
        goal_amount += row[0]
    db.commit()
    db.close()
    return goal_amount


# Gets set budget amount for a category
def get_budget(category):
    budget_amount = 0
    db = sqlite3.connect('budgets')
    cursor = db.cursor()
    cursor.execute('''SELECT id, category_number, expenses_budget FROM 
                   budget WHERE category_number=? ''', (category,))
    # Putting data in appropriate lists
    for row in cursor:
        budget_amount += row[2]
    db.commit()
    db.close()   
    return budget_amount