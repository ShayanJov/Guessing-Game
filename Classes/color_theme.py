from colorama import Fore, Style

class ColorTheme:
    def __init__(self, theme_dict):
        self.theme_dict = theme_dict

    def color_print(self, text, theme_key, style=Style.NORMAL):
        theme_color = self.theme_dict.get(theme_key, Fore.WHITE)
        return f"{style}{theme_color}{text}{Style.RESET_ALL}"

# Define a custom color theme for the entire project
PROJECT_THEME = ColorTheme({
    'menu_title': Fore.BLUE + Style.BRIGHT,
    'input_prompt': Style.BRIGHT,
    'warning': Fore.RED + Style.BRIGHT,
    'success': Fore.GREEN + Style.BRIGHT,
})
