# Importing external libraries
import sqlite3

try:
    # Creating and connecting the database
    db = sqlite3.connect('budgets')
    cursor = db.cursor()

    # Creating category table, if it doesn't exist
    cursor.execute('''CREATE TABLE IF NOT EXISTS category(category_number 
                   INTEGER, category TEXT, 
                   PRIMARY KEY(category_number,category)) ''')
    db.commit()
    cursor = db.cursor()
    print("The category table was made")

    #category list
    category_list = [(1, "Rent"), (2, "Clothes"), (3, "Food"), (4, "Transport") 
                     , (5, "Going out Fund"), (6, "Gifts")]

    # Populating category
    cursor.executemany('''INSERT OR REPLACE INTO category(category_number, 
                       category) VALUES(?,?)''',category_list)
    db.commit()
    print("The categories were added to the table")  

    # Creating expense table, if it doesn't exist
    cursor.execute('''CREATE TABLE IF NOT EXISTS expenses(id INTEGER PRIMARY 
                   KEY, category_number INTEGER, price INTEGER,
                   recurring_cost BOOLEAN DEFAULT 0) ''')
    db.commit()
    cursor = db.cursor()
    print("The expense table was made")

    # Creating income table, if it doesn't exist
    cursor.execute('''CREATE TABLE IF NOT EXISTS income(id INTEGER PRIMARY KEY,
                   category_number INTEGER, amount INTEGER, recurring_cost 
                   BOOLEAN DEFAULT 0) ''')
    db.commit()
    cursor = db.cursor()
    print("The income table was created")

    # Creating budget table, if it doesn't exist
    cursor.execute('''CREATE TABLE IF NOT EXISTS budget(id INTEGER PRIMARY KEY,
                    category_number INTEGER, expenses_budget INTEGER, 
                    actual_expenses INTEGER, budget_exceeded BOOLEAN DEFAULT 0)
                    ''')
    db.commit()
    cursor = db.cursor()
    print("The budget table was created")

    # Creating financial goals table, if it doesn't exist
    cursor.execute('''CREATE TABLE IF NOT EXISTS goals(id INTEGER,
                    date_set DATE, what_is_goal Text, progress INTEGER,
                    goal_met BOOLEAN DEFAULT 0)
                    ''')
    db.commit()
    cursor = db.cursor()
    print("The financial goal table was created")

except Exception as error_msg:
        # Roll back any changes if something goes wrong.
        db.rollback()
        raise error_msg

# Closes database
finally:
    db.close()