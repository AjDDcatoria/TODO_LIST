""" #! IMPORTANT 
    To connect data base need to install 
    pip install mysql-connector-python  👈 this

    to install open terminal then type 👆

    data base we used mysql (XAMPP)
"""
import mysql.connector
from datetime import datetime,timedelta

from deadline import DeadlineTracker
from ui import Main,Display,TextColor,TextStyle

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
            # print("Connected to the database!")
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
        Coded : 11-18-2023 📅

        """
        cursor = self.connector.con.cursor()

        # Execute SQL query to add a task
        sql = "INSERT INTO todo_test4 (`title`, `description`, `deadline`, `mark`) VALUES (%s, %s, %s, %s)"
        values = (task_name, description, deadline_str, False)

        try:
            cursor.execute(sql, values)
            # Commit the changes to the database
            self.connector.con.commit()

            return '\n\t\tTask Added ✔️'

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
        Coded: 11-18-2023 to 11-19-2023 📅
        """

        print('\t       - Add Tasks -\n')
        task_name = input('   Enter Title       : ')
        description = input('   Enter Description : ')
        deadline_str = input('   Enter Deadline MM-DD-YY: ')

        # Check if the inputs are empty
        if not task_name or not description or not deadline_str:
            return '\n   Please input all the requirements'

        try:
            parsed_date = datetime.strptime(deadline_str, "%m-%d-%Y")

            if parsed_date < datetime.now():
                choice = input('The deadline you provided is already past.\nPlease enter "YES" or "NO" if you want to continue: ')
                
                # check if the user enters "no" then skip the insertion
                if choice.upper() != 'YES':
                    return '\tTask not added. Deadline is past.'
                else:
  
                  return  self.insert_task(task_name,description,deadline_str)

            return self.insert_task(task_name,description,deadline_str)

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
           DSA Project| Final project|  12-13-2023  |   1
           Assignment1| Math         |  11-28-2023  |   0
           Activity 1 | PE           |  11-15-2023  |   1
            
                  R  C                  C = column  R = row
        task_list[1][1] == Math         // description
        task_list[0][1] == Assignment   // title
        task_list[3][0] == 1            // mark

        Author : AJ R. Dedicatoria
        Coded : 11-19-2023
        """

        cursor = self.connector.con.cursor()

        try:
            sql = 'SELECT * FROM todo_test4'
            cursor.execute(sql)

            result = cursor.fetchall()

            task_list = [list(row) for row in result]

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
        return '\tTask Remove ✔️'
    
    def remaining_days_text(self, deadline_str):
        """
        Formats the remaining days based on the difference between the deadline date and the current date.

        Args:
            deadline_str (str): Deadline in MM-DD-YY format.

        Returns:
            str: Formatted text indicating the remaining days.
        """
        if deadline_str == '0':
            return "Special case for 0"  # Handle it as needed
        else:
            try:
                deadline_date = datetime.strptime(deadline_str, "%m-%d-%Y").date()
                current_date = datetime.now().date()
                days_left = (deadline_date - current_date).days

                if days_left == 0:
                    return TextColor.GREEN + "Today" + TextColor.RESET
                elif days_left > 0:
                    return f"{days_left} days left"
                else:
                    return TextColor.RED +"Missing"+ TextColor.RESET # Deadline has passed

            except ValueError:
                return "Invalid date format"

    def display_filtered_tasks(self, tasks, filter=None):
        """
        Displays tasks based on the specified filter.

        Args:
            tasks (list): List of tasks to display.
            filter (str): Filter option, either 'showTodo' or 'showDone'. Defaults to None.

        Author: AJ R. Dedicatoria
        Coded: 11-23-2023
        """
        Display.clear_screen()
        Main.print_header()
        self.notif()
        print('='*14,
            TextStyle.BOLD +
            TextColor.MAGENTA + "  TODO LIST  " +
            TextColor.RESET +
            TextStyle.RESET +
            "="*14
        )
        print(TextStyle.BOLD,TextColor.YELLOW,'{:<16} {:<10} {:<20}'.format('   Title', ' Mark', 'Deadline'),TextStyle.RESET,TextColor.RESET)
        print('=' * 42)
        
        for count, task in enumerate(tasks, start=1):
            title_text = task[0]
            mark_value = task[3]
            day_value = self.remaining_days_text(task[2])

            # Convert mark to (Todo) or (Done)
            mark_text = "(" + TextColor.YELLOW + "Todo" + TextColor.RESET + ")" if mark_value == 0 else "(" + TextColor.GREEN + "Done" + TextColor.RESET + ")"

            # Apply filter
            if filter == 'showTodo' and mark_value != 0:
                continue
            elif filter == 'showDone' and mark_value != 1:
                continue

            print(f"{count}. {title_text:<15} {mark_text:<18} {day_value:<20}")


    def display_task(self):
        main = Main()
        display = Display()
        """
        Fetches all tasks from the database, calculates the number of days remaining before the deadlines,
        sorts the tasks by the remaining days, and displays them in a formatted manner.

        Author: Aj R. Dedicatoria
        Coded: 11-20-2023
        """
        tasks = self.get_all_tasks()
        track = DeadlineTracker(tasks)
        track.sort_by_days_left()
        sorted_tasks = track.get_task()

        go_back = False
        while not go_back:
            self.display_filtered_tasks(sorted_tasks)
            choice = input("\nEnter 'showTodo', 'showDone', or 'Back': ")

            if choice.upper() == 'BACK':
                go_back = True
            elif choice.upper() == "SHOWTODO":
                display.clear_screen()
                main.print_header()
                print('='*14,
                TextStyle.BOLD +
                TextColor.MAGENTA + "  TODO LIST  " +
                TextColor.RESET +
                TextStyle.RESET +
                "="*14
                )
                self.display_filtered_tasks(sorted_tasks, filter='showTodo')
                input("\nPress Enter to go back...")
                display.clear_screen()
                main.print_header()
            elif choice.upper() == "SHOWDONE":
                display.clear_screen()
                main.print_header()
                print('='*14,
                TextStyle.BOLD +
                TextColor.MAGENTA + "  TODO LIST  " +
                TextColor.RESET +
                TextStyle.RESET +
                "="*14
                )
                self.display_filtered_tasks(sorted_tasks, filter='showDone')
                input("\nPress Enter ...")
                display.clear_screen()
                main.print_header()
            else:
                display.clear_screen()
                main.print_header()
                print("\n\t      Invalid choice.")
                input("\n\t      Press Enter...")
                display.clear_screen()
                main.print_header()

        display.clear_screen()
        main.print_header()
        return '\n\n\t Back to the main Menu'  
     
    def mark_task(self):
        # TODO: Code to mark the task from the database / edit 🔨
        sorted_tasks = self.get_all_tasks()
        """ #? IDEA for building this function
            The mark value in database is BOOLEAN
            0 = False == TODO
            1 = True == DONE

            You can use the get_all_task() function to display the task
            and then ask the user for input on which task they want to mark.
            You can decide on the specific implementation details.
        """
        self.display_filtered_tasks(sorted_tasks,'showTodo')
        return ''

    def update_task(self):
        """
            Update tasks in the TODO list.

            Displays a list of tasks and allows the user to choose a 
            task to update.
            
            The user can choose to update the title, description, deadline, 
            or mark.

            Handles user input and ensures the correctness of the entered values.

            Author: AJ R. Dedicatoria
            Coded : 11-25-2023
        """
        print(f"\t\t{'Update task'} \n{'=' * 42}\n")

        try:
            task_list = self.get_all_tasks()
            # Print all task
            for count, task_data in enumerate(task_list, start=1):
                print(f"{'':<2}{count}.{task_data[0]}")

            task_choice = int(input('\nEnter your Choice :')) - 1
            if task_choice > len(task_list) or task_choice < 0:
                Display.clear_lines(len(task_list) + 3)
                print(f'\n\tNumber {task_choice} not found!!!')
            else:
                Display.clear_lines(len(task_list) + 3)
                print(f"\n{'':<2}{'1.Title'}\n{'':<2}{'2.Description'}\n{'':<2}{'3.Deadline'}\n{'':<2}{'4.Mark'}\n")

                task_value = int(input('Enter your choice :')) - 1
                edited_value = None

                if task_value > 3:
                    print("\n\tSomething went wrong")
                else:
                    task_as_ID = task_list[task_choice][0]
                    if task_value == 0:
                        Display.clear_lines(1)
                        edited_value = str(input('Enter new Title: '))
                        self.edit_task(edited_value,task_as_ID,task_value)
                    elif task_value == 1:
                        Display.clear_lines(1)
                        edited_value = str(input('Enter new Description: '))
                        self.edit_task(edited_value,task_as_ID,task_value)
                    elif task_value == 2:
                        edited_value = str(input('Enter new Deadline (MM-DD-YY): '))

                        try:
                            parsed_date = datetime.strptime(edited_value,"%m-%d-%Y")

                            if parsed_date < datetime.now():
                                choice = input('The deadline you provide is already past\nPlease enter "YES" or "NO" if you want to continue:')

                                if choice.upper() != "YES":
                                    return '\n\t Deadline will not Update'
                                else:
                                    # insert the updated value to data base
                                    self.edit_task(edited_value,task_as_ID,task_value)  
                            else:
                                self.edit_task(edited_value,task_as_ID,task_value)  

                        except ValueError:
                            return '\n     Invalid datee format. Please use MM-DD-YY.'

                    elif task_value == 3:
                        Display.clear_lines(1)
                        mark_input = input('Enter new Mark("done" or "Todo"): ')

                        # Convert user input to mark value
                        if(mark_input.lower() == "done" 
                           or mark_input.lower() == 'todo'):

                            edited_value = 1 if mark_input.lower() == "done" else 0

                            self.edit_task(edited_value,task_as_ID,task_value)
                        else:
                            Display.clear_lines(1)
                            print('\tPlease Enter ("done" or "Todo")')

        except ValueError:
            Display.clear_screen()
            Main.print_header()
            self.notif()
            print('=' * 14,
                TextStyle.BOLD +
                TextColor.MAGENTA + "  TODO LIST  " +
                TextColor.RESET +
                TextStyle.RESET +
                "=" * 14
                )
            print(f"\t\t{'Update task'} \n{'=' * 42}\n")
            print('\t\n\nPlease Enter a Number ...\n')
        return ''
    
    def default(self):
        return 'Not in the options. Please try again!'
    
    def notif(self):

        """
            Check and notify upcoming deadlines within a specific time range.

            Retrieves all tasks, sorts them by days left until the deadline, and
            notifies about the first upcoming deadline that meets certain criteria.

            Criteria:
            - Deadline is today or in the past.
            - Deadline is within the next 3 days.

            Prints a notification message with the task title and days left if applicable.

            Author : Aj R. Dedicatoria
            Coded : 11-22-2023
        """
        tasks = self.get_all_tasks()
        track = DeadlineTracker(tasks)
        track.sort_by_days_left()
        sorted_tasks = track.get_task()
        notif_task = None

        for task in sorted_tasks:
            try:
                deadline_date = datetime.strptime(task[2], "%m-%d-%Y")  # Parse date string to datetime object
                days_left = (deadline_date - datetime.now()).days  # Calculate days left until the deadline
            except ValueError:
                print(f"Error: Unable to convert '{task[2]}' to a valid date for task '{task[0]}'. Skipping task.")
                continue

            if days_left == -1 or days_left == 0 and task[3] == 0:
                notif_task = task[0]  # Return the title
                print(f"📅 {TextColor.RED}{notif_task}{TextColor.RESET} Upcoming Deadline: Today")
                break
            elif 0 < days_left <= 3 and task[3] == 0:
                notif_task = task[0]  # Return the title
                print(f"📅 {TextColor.RED}{notif_task}{TextColor.RESET} Upcoming Deadline: {days_left} Day{'s' if days_left != 1 else ''} left")
                break

    def edit_task(self,edited_value,task_as_ID,task_value):
        """
            This function use to edit the task value base on task_as_ID
            to find the value in database table
        """

        cursor = self.connector.con.cursor()
        try:
            # Update the selected task in the database
            query = f"UPDATE todo_test4 SET {['title', 'description', 'deadline', 'mark'][task_value]} = %s WHERE title = %s"
            cursor.execute(query, (edited_value, task_as_ID))
            self.connector.con.commit()
            print('\n    Task Updated successfully!!!')
        except mysql.connector.Error as e:
            print(f"Error updating task: {e}")

