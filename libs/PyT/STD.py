from colorama import Back, Fore, Style
from colorama import init as cinit

class STDLib:
    def __init__(self, info):
        self.info = info
    def color(self, text):
        """
Colors to language text or smth,

Background:
{back.black},
{back.blue},
{back.cyan},
{back.green},
{back.lightblack_ex},
{back.lightblue_ex},
{back.lightcyan_ex},
{back.lightgreen_ex},
{back.lightmagenta_ex},
{back.lightred_ex},
{back.lightwhite_ex},
{back.lightyellow_ex},
{back.magenta},
{back.red},
{back.reset},
{back.white},
{back.yellow}

Foreground:
{fore.black},
{fore.blue},
{fore.cyan},
{fore.green},
{fore.lightblack_ex},
{fore.lightblue_ex},
{fore.lightcyan_ex},
{fore.lightgreen_ex},
{fore.lightmagenta_ex},
{fore.lightred_ex},
{fore.lightwhite_ex},
{fore.lightyellow_ex},
{fore.magenta},
{fore.red},
{fore.reset},
{fore.white},
{fore.yellow}

Style:
{style.bright},
{style.dim},
{style.normal},
{style.reset_all}
        """
        text = text.replace('{back.black}', Back.BLACK).replace('{back.blue}', Back.BLUE).replace('{back.cyan}', Back.CYAN).replace('{back.green}', Back.GREEN).replace('{back.lightblack_ex}', Back.LIGHTBLACK_EX).replace('{back.lightblue_ex}', Back.LIGHTBLUE_EX).replace('{back.lightcyan_ex}', Back.LIGHTCYAN_EX).replace('{back.lightgreen_ex}', Back.LIGHTGREEN_EX).replace('{back.lightmagenta_ex}', Back.LIGHTMAGENTA_EX).replace('{back.lightred_ex}', Back.LIGHTRED_EX).replace('{back.lightwhite_ex}', Back.LIGHTWHITE_EX).replace('{back.lightyellow_ex}', Back.LIGHTYELLOW_EX).replace('{back.magenta}', Back.MAGENTA).replace('{back.red}', Back.RED).replace('{back.reset}', Back.RESET).replace('{back.white}', Back.WHITE).replace('{back.yellow}', Back.YELLOW)
        text = text.replace('{fore.black}', Fore.BLACK).replace('{fore.blue}', Fore.BLUE).replace('{fore.cyan}', Fore.CYAN).replace('{fore.green}', Fore.GREEN).replace('{fore.lightblack_ex}', Fore.LIGHTBLACK_EX).replace('{fore.lightblue_ex}', Fore.LIGHTBLUE_EX).replace('{fore.lightcyan_ex}', Fore.LIGHTCYAN_EX).replace('{fore.lightgreen_ex}', Fore.LIGHTGREEN_EX).replace('{fore.lightmagenta_ex}', Fore.LIGHTMAGENTA_EX).replace('{fore.lightred_ex}', Fore.LIGHTRED_EX).replace('{fore.lightwhite_ex}', Fore.LIGHTWHITE_EX).replace('{fore.lightyellow_ex}', Fore.LIGHTYELLOW_EX).replace('{fore.magenta}', Fore.MAGENTA).replace('{fore.red}', Fore.RED).replace('{fore.reset}', Fore.RESET).replace('{fore.white}', Fore.WHITE).replace('{fore.yellow}', Fore.YELLOW)
        text = text.replace('{style.bright}', Style.BRIGHT).replace('{style.dim}', Style.DIM).replace('{style.normal}', Style.NORMAL).replace('{style.reset_all}', Style.RESET_ALL)
        return text
