# Importing external libraries
import sqlite3

try:
    # Creating and connecting the database
    db = sqlite3.connect('budgets')
    cursor = db.cursor()

    # Creating expense table, if it doesn't exist
    cursor.execute('''CREATE TABLE IF NOT EXISTS expenses(id INTEGER PRIMARY 
                   KEY, ) ''')
    db.commit()
    cursor = db.cursor()

    # Creating income table, if it doesn't exist
    cursor.execute('''CREATE TABLE IF NOT EXISTS income(id INTEGER PRIMARY KEY,
                       ) ''')
    db.commit()
    cursor = db.cursor()

    # Creating financial goals table, if it doesn't exist
    cursor.execute('''CREATE TABLE IF NOT EXISTS goals(id INTEGER PRIMARY KEY,
                       ) ''')
    db.commit()
    cursor = db.cursor()

except Exception as error_msg:
        # Roll back any changes if something goes wrong.
        db.rollback()
        raise error_msg

# Closes database
finally:
    db.close()