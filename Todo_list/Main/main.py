from option import Options
from ui import Display,Menu,TextColor,TextStyle,Main


class MainProcessor:
    @staticmethod
    def main():
        Display.clear_screen()
        options = Options()
        exit_flag = False
        while not exit_flag:
            Main.print_header()
            options.notif()
            print('='*14,
                TextStyle.BOLD +
                TextColor.MAGENTA + "  TODO LIST  " +
                TextColor.RESET +
                TextStyle.RESET +
                "="*14
            )
            Menu.print_menu()
            choice = input("\nEnter your choice ➜ :")
            switch_choice = {
                "1": options.add_task,
                "2": options.remove_task,
                "3": options.display_task,
                "4": options.mark_task,
                "5": options.update_task
            }
            Display.clear_lines(9)
            
            if choice == "6":
                Display.clear_screen()
                exit_flag = True
            else:
                selected_option = switch_choice.get(choice, options.default)
                options_result = selected_option()
                Display.update_text(options_result)
                input("\n\tPress Enter ...")
                Display.clear_screen()


if __name__ == "__main__":
    MainProcessor.main()
