from prompt_toolkit import PromptSession, prompt
from colorama import Back, Style, init
import sys
init()
def run():
    sizes = PromptSession().output.get_size()
    if sizes[0] < 20 or sizes[1] < 20:
        print("Not enough terminal size!")
        return
    LightServer()

class LightServer:
    def __init__(self):
        self.sizes = PromptSession()

        self.screen_base = self.color_screen()
        while True:
            self.screen_base = "".join(self.__cursor(self.color_screen()))
            sys.stdout.write(self.screen_base)

    def __prerender(self, map):
        for i in range(0, len(map)-1):
            map[i] = "".join(map[i])
        return map
    def __cursor(self, map):
        self.cursor = [0, 0]

        map[self.cursor[0]][self.cursor[1]] =  Back.WHITE + " " + Style.RESET_ALL
        map = self.__prerender(map)
        print(map, "d")
        return map
        
    def color_screen(self):
        d = [str(Back.BLUE + " " + Style.RESET_ALL)] * self.sizes.output.get_size()[1]
        print(d)
        d.append("\n")
        d = [d] * self.sizes.output.get_size()[0]
        print(d)

        return d

        
run()
