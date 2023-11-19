"""
    To connect data base need to install 
    pip install mysql-connector-python  👈 this

    to install open terminal then type 👆

    data base we used mysql (XAMPP)
"""

from main import (
    clear_screen,
    clear_lines
)
import mysql.connector

from datetime import datetime

current_date = datetime.now().date()

class Connector: # DataBase Connector translated from java
    def __init__(self):
        self.con = None
        self.pst = None

    def connect(self):
        try:
            self.con = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="test"
            )
            print("Connected to the database!")
        except mysql.connector.Error as err:
            print(f"Error: {err}")

connector = Connector()
connector.connect()

def add_task():
    """
    This block of code inserts values into the database.

    Before inserting the deadlines if the user provide is 
    already past ask if he/she wants to continue if yes
    then insert the value into database

    Author: AJ R. Dedicatoria ☠️
    Code created: 11-18-2023 to 11-19-2023 📅
    """

    print('\t - Add Tasks -\n')
    task_name = input('Enter Title       : ')
    description = input('Enter Description : ')
    deadline_str = input('Enter Deadline MM-DD-YY: ')

    #! Check if the inputs are empty
    if not task_name or not description or not deadline_str:
        return 'Please input all the requirements'

    cursor = None  # Initialize cursor to None

    try:
        parsed_date = datetime.strptime(deadline_str, "%m-%d-%Y")

        if parsed_date < datetime.now():
            choice = input('The deadline you provided is already past.\nPlease enter "YES" or "NO" if you want to continue: ')
            
            # check if the user enter no then skip the insertion
            if choice.upper() != 'YES':
                return '\tTask not added. Deadline is past.'
            else:
                cursor = connector.con.cursor()
                # Execute SQL query to add a task
                sql = "INSERT INTO todo_test (`title`, `description`, `deadlines`, `mark`) VALUES (%s, %s, %s, %s)"
                values = (task_name, description, parsed_date, False)
                cursor.execute(sql, values)

                # Commit the changes to the database
                connector.con.commit()

                return '\n\t  Task Added ✔️'

    except ValueError:
        return 'Invalid date format. Please use MM-DD-YY.'

    except mysql.connector.Error as err:
        return f"Error adding task: {err}"

    finally:
        # Close the cursor if it's not None
        if cursor:
            cursor.close()

def remove_task():
    # TODO : Code to remove the task from the database 🔨

    """ #? IDEA for building this function

        You can use display_task() function to display the task
        and delete by user input 

        ikaw na bahala if gusto mo nan lahi na way pag display
    
    """
    print('\t- Remove Tasks -\n')
    return '\t  Task Remove ✔️'


def display_task():
    # TODO : Code to display the task from the database 🔨

    """ #? IDEA for building this function
                                            yyyy mm dd
        The deadline value in data base ex. 2023-11-20

        before displaying the task calculate how many
        days remaining before the deadlines. Sort them
        by the remaining days ex. below

        display the task look like this

            ============ TODO LIST ============ 

                1.Assignment#1 (TODO) 2 days left
                2.Assignment#2 (TODO) 5 days left
                3.Activity#1 (DONE) 9 days left
        
        addition the mark in data base is boolean 
        0 = False == TODO
        1 = True == DONE

        Add feature print all TODO or Done task base user wants
        before printing make sure to clear text in console using

           ( clear_screen, ) = clear entire text
           ( clear_lines ) = clear specific line bottom to top 

           example in main.py file
    """

    return 'displayTask'


def mark_task():
    # TODO :Code to mark the task from the database / edit 🔨

    """ #? IDEA for building this function

        the mark value in data base is BOOLEAN
        0 = False == TODO
        1 = True == DONE

        You can use display_task() function to display the task
        then ask the user input that he/she wants to mark

        ikaw bahala kung gusto mo nan lahi na way pag display
    """
    return 'markTask'


def update_task():
    # TODO :Code to update or change the value of a task in the database 🔨

    """ #? IDEA for building this function

        display the task then ask user want the task
        he/she wants to update

        once the maka pili na siya nan task mag ask if uno iya otrohon
        example

            ============ TODO LIST ============
                
                1. Title
                2. Description
                3. Mark
                4. DeadLine

            Enter your choise : // user input
        
        then uno iya piliOn amoy editon sa data base 
    """
    return 'updateTask'


def default():
    return 'Not in the options. Please try again!'
