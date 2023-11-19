""" #! IMPORTANT 
    To connect data base need to install 
    pip install mysql-connector-python  👈 this

    to install open terminal then type 👆

    data base we used mysql (XAMPP)
"""
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

class Options:
    def __init__(self):
        self.connector = Connector()
        self.connector.connect()

    def insert_task(self, task_name, description, deadline_str):
        """
        Inserts a task into the database.

        :param task_name: Title of the task
        :param description: Description of the task
        :param deadline_str: Deadline in MM-DD-YY format
        :return: Message indicating the success or failure of the operation

        Author : Aj R. Dedicatoria ☠️
        Code created : 11-18-2023 📅

        """
        cursor = self.connector.con.cursor()

        # Execute SQL query to add a task
        sql = "INSERT INTO todo_test (`title`, `description`, `deadlines`, `mark`) VALUES (%s, %s, %s, %s)"
        values = (task_name, description, deadline_str, False)

        try:
            cursor.execute(sql, values)
            # Commit the changes to the database
            self.connector.con.commit()

            return '\n\t  Task Added ✔️'

        except mysql.connector.Error as err:
            return f"Error adding task: {err}"

        finally:
            # Close the cursor
            cursor.close()

    def add_task(self):
        """
        This block of code inserts values into the database.
        Before inserting. check the deadlines if the user provides is 
        already past, ask if they want to continue. If yes,
        then insert the value into the database.

        Author: AJ R. Dedicatoria ☠️
        Code created: 11-18-2023 to 11-19-2023 📅
        """

        print('\t - Add Tasks -\n')
        task_name = input('Enter Title       : ')
        description = input('Enter Description : ')
        deadline_str = input('Enter Deadline MM-DD-YY: ')

        # Check if the inputs are empty
        if not task_name or not description or not deadline_str:
            return 'Please input all the requirements'

        try:
            parsed_date = datetime.strptime(deadline_str, "%m-%d-%Y")

            if parsed_date < datetime.now():
                choice = input('The deadline you provided is already past.\nPlease enter "YES" or "NO" if you want to continue: ')
                
                # check if the user enters "no" then skip the insertion
                if choice.upper() != 'YES':
                    return '\tTask not added. Deadline is past.'
                else:
  
                  return  self.insert_task(task_name,description,parsed_date)

            return self.insert_task(task_name,description,parsed_date)

        except ValueError:
            return 'Invalid date format. Please use MM-DD-YY.'

        except mysql.connector.Error as err:
            return f"Error adding task: {err}"

    def get_all_tasks(self):
        """
        Fetching all data from database and 
        insert to 2D array

        retrive data from 2d array?

        example: # Database table

           ==================================================
             title    |  description |  deadlines   |  mark
           ==================================================
            title#1   |    des#1     |  2023-11-20  |   1
            title#2   |    des#2     |  2023-12-20  |   0
            title#3   |    des#3     |  2023-13-20  |   1
            title#4   |    des#4     |  2023-14-20  |   0
            title#5   |    des#5     |  2023-15-20  |   1
                 
            
                  R  C               C = column  R = row
        task_list[1][5] == des#5     // description
        task_list[0][1] == title#1   // title
        task_list[3][0] == 1         // mark

        Author : AJ R. Dedicatoria
        Code created : 11-19-2023
        """

        cursor = self.connector.con.cursor()

        try:
            sql = 'SELECT * FROM todo_test'
            cursor.execute(sql)

            result = cursor.fetchall()

            task_list = [list(row) for row in zip(*result)]

            return task_list

        except mysql.connector.Error as err:
            print(f"Error fetching tasks:{err}")
        finally:
            cursor.close()

    def remove_task(self):
        # TODO: Code to remove the task from the database 🔨

        """ #? IDEA for building this function
            You can use get_all_task() function to display the task
            and delete by user input
            You can decide on the specific implementation details.
        """
        print('\t- Remove Tasks -\n')
        return '\t  Task Remove ✔️'

    def display_task(self):
        # TODO: Code to display the task from the database 🔨

        """ #? IDEA for building this function
            The deadline value in the database is in the format ex. 2023-11-20
            Before displaying the task, calculate how many
            days remaining before the deadlines. Sort them
            by the remaining days ex. below

            Display the task as follows:

            ============== TODO LIST ==============
                 Title       Mark       Day left
            =======================================

            1.Assignment#1   (Todo)   2 days left
            2.Assignment#2   (Todo)   5 days left
            3.Activity#1     (Done)   9 days left
        """
        return 'displayTask'

    def mark_task(self):
        # TODO: Code to mark the task from the database / edit 🔨

        """ #? IDEA for building this function
            The mark value in database is BOOLEAN
            0 = False == TODO
            1 = True == DONE

            You can use the get_all_task() function to display the task
            and then ask the user for input on which task they want to mark.
            You can decide on the specific implementation details.
        """
        return 'markTask'

    def update_task(self):
        # TODO: Code to update or change the value of a task in the database 🔨

        """ #? IDEA for building this function
            Display the task and ask the user which task
            they want to update.

            Once the user selects a task, ask them what they want to update.
            For example:

            ============ TODO LIST ============
            
            1. Title
            2. Description
            3. Mark
            4. DeadLine

            Enter your choice: // user input

            Then update the selected task in the database.
        """
        return 'updateTask'

    def default(self):
        return 'Not in the options. Please try again!'

