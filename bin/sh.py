import traceback, os, sys
class Exit(Exception):
    pass
class Commands:
    def __init__(self):
        self.cmds = {
            "help": [["man"], "Show this message.", self.help],
            "cd": [["chdir"], "CD to another dir.", self.cd],
            "ls": [[], "List Dir", self.ls],
            "exit": [["poweroff", "off"], "Exit", self.exit]
        }
        self.aliases = {}
        for cmd in self.cmds:
            for cmd2 in self.cmds[cmd][0]:
                self.aliases.update({cmd2: self.cmds[cmd][2]})

    def help(self, args):
        t = ""
        print("Help:", end = "")
        for i in self.cmds:
            t+= f"\n{i} - Aliases: {', '.join(self.cmds[i][0])}" + "\n" + f"{self.cmds[i][1]}"
        print(t)

    def cd(self, args):
        global cwd
        if os.path.isdir(os.path.abspath(cwd.replace("\\", "/") + "/" + "".join(args[0].split(" ")[1:]).replace("\\", "/"))):
            cwd = os.path.abspath(cwd.replace("\\", "/") + "/" + "".join(args[0].split(" ")[1:]).replace("\\", "/"))
        else:
            return

    def ls(self, args):
        global cwd
        i, l = 0, ""
        if os.path.isdir(cwd):
            for d in os.listdir(cwd):
                if i == 6:
                    i == 1
                    l += "\n"
                l += f"{d} "
                i += 1
            print(l)

    def exit(self, args):
        raise Exit("Console interrupt.")
class Shell:
    def __init__(self):
        self.cmds = Commands().cmds
        self.aliases = Commands().aliases
        
    def system(self, args):
        if len(args[0].split("||")) > 1:
            for i in args[0].split("||"):
                if i.split(" ")[0].isspace() or i.split(" ")[0] == "":
                    i = i.split(" ")
                    del i[0]
                    i = " ".join(i)
                
                if i.split(" ")[0] in self.cmds:
                    try:
                        self.cmds[i.split(" ")[0]][2]([i, args[1]])
                    except Exit:
                        raise Exit("Console stopped.")
                    except:
                        traceback.print_exc()
                elif i.split(" ")[0] in self.aliases:
                    try:
                        self.aliases[i.split(" ")[0]]([i, args[1]])
                    except Exit:
                        raise Exit("Console stopped.")
                    except:
                        traceback.print_exc()
                else:
                    return print(f"[INFO] Unknown command {i.split(' ')[0]}!")
        if len(args[0].split("||")) == 1:
            if args[0].split(" ")[0] in self.cmds:
                try:
                    self.cmds[args[0].split(" ")[0]][2]([args[0], args[1]])
                except Exit:
                    raise Exit("Console stopped.")
                except:
                    traceback.print_exc()
                return
            elif args[0].split(" ")[0] in self.aliases:
                try:
                    self.aliases[args[0].split(" ")[0]]([args[0], args[1]])
                except Exit:
                    raise Exit("Console stopped.")
                except:
                    traceback.print_exc()
            else:
                return print(f"[INFO] Unknown command {args[0].split(' ')[0]}!")
            
    def startup(self, args):
        global cwd
        cwd = os.path.abspath(os.getcwd() + "/../")
        args2 = " ".join(args[0].info[15].split(" ")[1:])
        if len(args2.split(" ")) > 1: return self.system([args2, args])

        while True:
            symb = "$"
            if args[1].accs_o[args[1].info["user"]]["root_acc"]:
                symb = "#"
            user = input(f"{cwd} {symb} ")
            self.system([user, args])

from colorama import Back, Fore, Style
from colorama import init as cinit
sys.path.insert(0, "../types")
cinit()
from binary import Binary
#class Binary:
#    pass
class sh(Binary):
    def __init__(self):
        self.info = {
            "name" : "Shell",
            "version" : "v1",
            "codename": ["sh"],
            "dependencies" : [], # Not Supported.
            "description": "Shell",
            "run": self.run
        }


    def run(self, info, pyt):
        shell = Shell()
        shell.startup([info, pyt])
        
            
            
        
        
