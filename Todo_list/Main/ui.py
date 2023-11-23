import os
import time
import sys
import psutil

class TextColor:
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    MAGENTA = '\033[35m'
    RESET = '\033[0m'

class TextStyle:
    BOLD = '\033[1m'
    RESET = '\033[0m'

class Display:
    @staticmethod
    def clear_screen():
        os.system("cls" if os.name == "nt" else "clear")

    @staticmethod
    def update_text(text):
        print(text)

    @staticmethod
    def clear_lines(n):
        for _ in range(n):
            sys.stdout.write("\033[F")
            sys.stdout.write("\033[K")

class Main:
    @staticmethod
    def get_battery_percentage():
        battery = psutil.sensors_battery()
        percent = battery.percent if battery else None
        return percent

    @staticmethod
    def print_header():
        current_time = time.strftime("%m-%d-%Y")
        battery_percent = Main.get_battery_percentage()

        if battery_percent is not None:
            status_icon = Main.get_battery_status_icon(battery_percent)
            print(f"{current_time}\t\t\t  📶 {status_icon}")

            print('='*14,
                TextStyle.BOLD +
                TextColor.MAGENTA + "  TODO LIST  " +
                TextColor.RESET +
                TextStyle.RESET +
                "="*14
            )

    @staticmethod
    def get_battery_status_icon(battery_percent):
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

class Menu:
    @staticmethod
    def print_menu():
        display = Display()
        display.clear_screen()
        Main.print_header()
        print("\n" + TextColor.YELLOW, "  1" + TextColor.RESET + ".Add task")
        print(TextColor.YELLOW, "  2" + TextColor.RESET + ".Remove task")
        print(TextColor.YELLOW, "  3" + TextColor.RESET + ".Display task")
        print(TextColor.YELLOW, "  4" + TextColor.RESET + ".Mark tasks as done")
        print(TextColor.YELLOW, "  5" + TextColor.RESET + ".Update task details ")
        print(TextColor.YELLOW, "  6" + TextColor.RESET + ".Exit ")
