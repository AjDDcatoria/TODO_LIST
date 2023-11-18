import os
import time
import sys
import psutil

# import options module
from option import (
    add_task,
    remove_task,
    display_task,
    mark_task,
    update_task,
    default
)

def get_battery_percentage():
    """
    To obtain the battery percentage, install the psutil module using the command:
    👉 #! pip install psutil 👈 
    in the terminal 💻.

    This function retrieves the battery percentage 🔋.

    Author: Aj R. Dedicatoria ☠️
    Code created: 11-18-2023 📅
    """
    battery = psutil.sensors_battery()
    percent = battery.percent if battery else None
    return percent


def print_header():
    """
    This function prints the current date and battery status of a laptop or desktop 💻
    using the psutil module 👆.

    Author: Aj R. Dedicatoria ☠️
    Code created: 11-18-2023 📅
    """

    # Get the current time
    current_time = time.strftime("%m-%d-%Y")

    # Get the battery percentage
    battery_percent = get_battery_percentage()

    # Print the date and battery status
    if battery_percent is not None:
        status_icon = get_battery_status_icon(battery_percent)
        print(f"{current_time}\t\t  📶 {status_icon}")


def get_battery_status_icon(battery_percent):
    """
    Returns an icon based on the battery percentage range.

    💭Gi add ko ini na feature para dili da basta display
    working gaud siya 💯😎

    Author: Aj R. Dedicatoria ☠️
    Code created: 11-18-2023 📅
    """
    # Constants for battery percentage ranges
    LOW = 20
    MEDIUM = 50
    HIGH = 80

    if battery_percent <= LOW:
        return "▪◻◻◻"
    elif LOW < battery_percent <= MEDIUM:
        return "▪◻◻◼"
    elif MEDIUM < battery_percent <= HIGH:
        return "▪◻◼◼"
    else:
        return "▪◼◼◼"


def clear_screen():
    # Clear the Console
    os.system("cls" if os.name == "nt" else "clear")


def update_text(text):
    # Update the text in Console
    print(text)


def clear_lines(n):
    """
    Clear specific lines in the Console.

    Author: Aj R. Dedicatoria
    Code created: 11-18-2023
    """
    for _ in range(n):
        sys.stdout.write("\033[F")
        sys.stdout.write("\033[K")


def print_menu():
    """
    Design/UI in the Console. Each number represents a menu option.

    Author: AJ R. Dedicatoria ☠️
    Code created: 11-18-2023 📅
    """
    clear_screen()
    print_header()
    print("\n========= TODO LIST =========\n")
    print("    1.Add task")
    print("    2.Remove task")
    print("    3.Display task")
    print("    4.Mark tasks as done")
    print("    5.Update task details ")
    print("    6.Exit ")


def main():
    """
    The main function where all the code runs.
    The exit_flag variable is declared to loop until the user wants to finish the program.

    Author: Aj R. Dedicatoria ☠️
    Code created: 11-18-2023 📅
    """

    exit_flag = False
    while not exit_flag:
        print_menu()
        choice = input("\nEnter your choice ➜ :")
        switch_choice = {  # switch statement where all cases are functions
            "1": add_task,
            "2": remove_task,
            "3": display_task,
            "4": mark_task,
            "5": update_task
        }
        clear_lines(8)
        if choice == "6":  # if the user enters number 6, stop the program
            clear_screen()
            exit_flag = True
        else:  # if the user enters between 1 to 5, print the options
            options = switch_choice.get(choice, default)()
            update_text(options)
            time.sleep(2)
            clear_screen()


if __name__ == "__main__":
    main()
