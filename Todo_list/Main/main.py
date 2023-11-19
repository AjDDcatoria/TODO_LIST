import os
import time
import sys
import psutil


from option import Options


class TextColor:
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    MAGENTA = '\033[35m'
    RESET = '\033[0m'

class TextStyle:
    BOLD = '\033[1m'
    RESET = '\033[0m'

class Main:

    def get_battery_percentage(self):
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


    def print_header(self):
        """
        This function prints the current date and battery status of a laptop or desktop 💻
        using the psutil module 👆.

        Author: Aj R. Dedicatoria ☠️
        Code created: 11-18-2023 📅
        """

        # Get the current time
        current_time = time.strftime("%m-%d-%Y")

        # Get the battery percentage
        battery_percent = self.get_battery_percentage()

        # Print the date and battery status
        if battery_percent is not None:
            status_icon = self.get_battery_status_icon(battery_percent)
            print(f"{current_time}\t\t  📶 {status_icon}")


    def get_battery_status_icon(self,battery_percent):
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


    def clear_screen(self):
        # Clear the Console
        os.system("cls" if os.name == "nt" else "clear")


    def update_text(self,text):
        # Update the text in Console
        print(text)


    def clear_lines(self,n):
        """
        Clear specific lines in the Console.

        Author: Aj R. Dedicatoria
        Code created: 11-18-2023
        """
        for _ in range(n):
            sys.stdout.write("\033[F")
            sys.stdout.write("\033[K")


    def print_menu(self,):
        """
        Design/UI in the Console. Each number represents a menu option.

        Author: AJ R. Dedicatoria ☠️
        Code created: 11-18-2023 📅
        """
        self.clear_screen()
        self.print_header()
        print(
            "\n============ " +
            TextStyle.BOLD +
            TextColor.MAGENTA + "TODO LIST" +
            TextColor.RESET + 
            TextStyle.RESET +
            " ============\n"
            )
        print(TextColor.YELLOW , "  1" + TextColor.RESET + ".Add task")
        print(TextColor.YELLOW , "  2" + TextColor.RESET +".Remove task")
        print(TextColor.YELLOW , "  3" + TextColor.RESET + ".Display task")
        print(TextColor.YELLOW , "  4" + TextColor.RESET + ".Mark tasks as done")
        print(TextColor.YELLOW , "  5" + TextColor.RESET + ".Update task details ")
        print(TextColor.YELLOW , "  6" + TextColor.RESET + ".Exit ")


    def main(self):
        options = Options()
        exit_flag = False
        while not exit_flag:
            self.print_menu()
            choice = input("\nEnter your choice ➜ :")
            switch_choice = {
                "1": options.add_task,
                "2": options.remove_task,
                "3": options.display_task,
                "4": options.mark_task,
                "5": options.update_task
            }
            self.clear_lines(8)

            if choice == "6":
                self.clear_screen()
                exit_flag = True
            else:
                selected_option = switch_choice.get(choice, options.default)
                options_result = selected_option()
                self.update_text(options_result)
                time.sleep(2)
                self.clear_screen()

if __name__ == "__main__":
    main = Main()
    main.main()


