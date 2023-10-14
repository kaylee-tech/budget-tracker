from budget_tracking_functions import *

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
                         7. Set or update a budget for a category 
                         8. View all budgets
                         9. View budget for a category
                         10. Set financial goals
                         11. View progress towards financial goals
                         12. Quit
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
            print(f"Adding an expense for {category_list[id_category-1]}")
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
        print("\nWhich category do you want to view your expenses from?")
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

    # Allows user to add their income
    elif menu == 4:
        print("Exising Categories")
        print(display_categories())

        # Seeing if the user wants to add a new category or use existing one
        menu_4_bool = False
        while menu_4_bool == False:
            menu_for_4 = value_err('''Select one of the following options
                                1. Add income with an existing category
                                2. Add income with a new category
                                : ''')
            if menu_for_4 == 1 or menu_for_4 == 2:
                menu_4_bool = True
            
            else:
                print("\nPlease only enter 1 or 2")

        # Adding income with existing category       
        if menu_for_4 == 1:
            print("")
            print("Which Category do you want to add your income to?")
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
            cate_obj = category_list[menu_cate-1]
            print(f"\nAdding an income from {cate_obj}")
            amount = value_err(f"Please enter how you earn from {cate_obj}: ")
            id_list, category_num_list, amount_list = pulling_income()
            id = len(id_list) + 1
            # Adding income to income table
            add_income(id, menu_cate, amount)

        # Adding new Category to category table & income to income table
        elif menu_for_4 == 2:
            print("\nCreating a new income category")
            category_list = pull_categories()
            new_category = input("Enter the name of the new category: ")

            # Making sure the category doesnt already exist
            while(category_exists(new_category, category_list) == True):
                print("\nPlease enter a name that does not already exist")
                new_category = input("Enter the name of the new category: ")
            
            # Adding the category to the Category Table
            id_category = len(category_list) + 1
            add_category(id_category, new_category)

            # Adding income to income table
            category_list = pull_categories()
            cate_obj = category_list[id_category-1]
            print(f"Adding an income from {cate_obj}")
            id_list, category_num_list, amount_list = pulling_income()
            id = len(id_list) + 1
            amount = value_err(f"Please enter how you earn from {cate_obj}: ")
            add_income(id, id_category, amount)

    # Allows user to view their incomes
    elif menu == 5:
        display_income()

    # Allows user to select what incomes they want to view
    elif menu == 6:
        # Selecting the category
        print("\nWhich category do you want to view your income from?")
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
        display_some_incomes(menu_cate)

    # Set their budget for a selected category
    elif menu == 7:
        print(display_budgets())

        id_list, budget_category, budget_cost = pulling_budgets()
        options_list = category_number_list()
        space_for_new_bud = True
        if len(id_list) == len(options_list):
            space_for_new_bud = False

        # Seeing if the user wants to add a new category or use existing one
        menu_7_bool = False
        while menu_7_bool == False:
            if(space_for_new_bud == True):
                menu_for_7 = value_err('''Select one of the following options
                                1. Set budget for a category
                                2. Update a budget for a category
                                : ''')
            else:
                menu_for_7 = value_err('''Select one of the following options
                            1. Option not available because all budgets exist
                            2. Update a budget for a category
                            : ''')
            if menu_for_7 == 1 and space_for_new_bud == True:
                menu_7_bool = True
            
            elif menu_for_7 == 2:
                menu_7_bool = True
            
            else:
                print("\nPlease only enter 1 or 2") 
            
        # Adding budget for a category
        if menu_for_7 == 1:
            print("")
            print("Which Category do you want to add a budget for?")
            s1 = """Select the number of the category\n"""
            menu_cate = value_err(f'''{s1}{display_empty_budgets()}: ''')

            # Making sure user selected an existing option
            user_bool = False
            options_list = empty_budget_number_list()
            while(user_bool == False):
                # Checking that the category exists
                if(menu_cate in options_list):
                    user_bool = True
                else:
                    print("\nPlease only select a number from the options")
                    menu_cate = value_err(f'''{s1}{display_empty_budgets()}: ''')

            # Getting info from user to add to database
            category_list = pull_categories()
            print(f"\nAdding a budget for {category_list[menu_cate-1]}")
            budget = value_err("Please enter what the limit should be: ")
            id_l, cate_num_l, bud_limit = pulling_budgets()
            id = len(id_l) + 1

            # Adding budget to budget table
            add_budget(id, menu_cate, budget)

        # Updating budget for a category
        if menu_for_7 == 2:
            id_list, cate_num_bud, budget_amount = pulling_budgets()

            # Checking to see if anything can be updated
            if len(id_list) == 0:
                print("Can't update anything - There is nothing to update\n")
            else:
                print("\nWhich budget do you want to update?")
                s1 = """Select the Id of the category\n"""
                menu_cate = value_err(f'''{s1}{display_budgets()}: ''')

                # Making sure user selected an existing option
                user_bool = False
                while(user_bool == False):
                    if(menu_cate in id_list):
                        user_bool = True
                    else:
                        print("\nPlease only select a number from the options")
                        menu_cate = value_err(f'''{s1}{display_budgets()}: ''')
                print("") 

                # Updating a budget record
                new_budget = value_err("Enter the amount of the new budget: ")
                update_budget(menu_cate, new_budget)      

    # View all their budgets
    elif menu == 8:
        print(display_budgets())

    # Allows user to see their budget for a selected category
    elif menu == 9:
        # Selecting the category
        print("\nWhich category do you want to view your budgets from?")
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
        display_some_budgets(menu_cate)

    # Allows user to set finacial goals 
    elif menu == 10:
        print(display_goals())

        id_list, goal_category, amount_profit = pulling_goals()
        options_list = category_number_list()
        space_for_new_bud = True
        if len(id_list) == len(options_list):
            space_for_new_bud = False

        # Seeing if the user wants to add to a new category or use existing one
        menu_10_bool = False
        while menu_10_bool == False:
            if(space_for_new_bud == True):
                menu_for_10 = value_err('''Select one of the following options
                                1. Set financial goals for a category
                                2. Update financial goals for a category
                                : ''')
            else:
                menu_for_10 = value_err('''Select one of the following options
                            1. Option not available because all goals exist
                            2. Update financial goals for a category
                            : ''')
            if menu_for_10 == 1 and space_for_new_bud == True:
                menu_10_bool = True
            
            elif menu_for_10 == 2:
                menu_10_bool = True
            
            else:
                print("\nPlease only enter 1 or 2") 
            
        # Adding financial goals for a category
        if menu_for_10 == 1:
            print("")
            print("Which Category do you want to add financial goals for?")
            s1 = """Select the number of the category\n"""
            menu_cate = value_err(f'''{s1}{display_empty_goals()}: ''')

            # Making sure user selected an existing option
            user_bool = False
            options_list = empty_goals_number_list()
            while(user_bool == False):
                # Checking that the category exists
                if(menu_cate in options_list):
                    user_bool = True
                else:
                    print("\nPlease only select a number from the options")
                    menu_cate = value_err(f'''{s1}{display_empty_goals()}: ''')

            # Getting info from user to add to database
            category_list = pull_categories()
            cate_type = category_list[menu_cate-1]
            print(f"\nAdding a goal for {cate_type}")
            sentence = f"""What difference do you want between the budget 
            and actual expenses for {cate_type}: """
            amount = value_err(sentence)
            id_l, cate_num_l, bud_limit = pulling_goals()
            id = len(id_l) + 1

            # Adding budget to budget table
            add_goal(id, menu_cate, amount)

        # Updating budget for a category
        if menu_for_10 == 2:
            id_list, cate_num, amount_profit = pulling_goals()

            # Checking to see if anything can be updated
            if len(id_list) == 0:
                print("Can't update anything - There is nothing to update\n")
            else:
                print("\nWhich goal do you want to update?")
                s1 = """Select the Id of the category\n"""
                menu_cate = value_err(f'''{s1}{display_goals()}: ''')

                # Making sure user selected an existing option
                user_bool = False
                while(user_bool == False):
                    if(menu_cate in id_list):
                        user_bool = True
                    else:
                        print("\nPlease only select a number from the options")
                        menu_cate = value_err(f'''{s1}{display_goals()}: ''')
                print("") 

                # Updating a financial goal record
                new_amount = value_err("""Enter new amount of the difference
                                   between the budget and actual expenses: """)
                update_goal(menu_cate, new_amount) 

    # Allows user to view their progress towords their finacial goals
    elif menu == 11:
        category_list = pull_categories()
        id_list, goal_category, amount_profit = pulling_goals()
        id_list, bud_category, budget_amount = pulling_budgets()
        if(len(category_list) == len(goal_category) == len(bud_category)):
            print("All your categories have budgets and financial goals")
        else:
            print("""To see all your financial goals' progress please enter all
                  your budgets and goals for each category""")
            
        display_goals_progress()

    # Exits the program
    elif menu == 12:
        print("Goodbye!")
        exit()

    # Lets user know they have made an invalid choice
    else:
        print("\nYou have entered an invalid number, Please try again")
