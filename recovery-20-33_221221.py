import json, os, sys, shutil, zipfile, importlib
from fs.memoryfs import MemoryFS
from fs.osfs import OSFS

def unzip_folder(zip_folder, destination):
        with zipfile.ZipFile(zip_folder) as zf:
            zf.extractall(destination)
def dynamic_import(module):
    return importlib.import_module(module)

class RecoveryKernel:
    def __init__(self):
        self.info = {
                "name": "PyT-RKernel_20-33_221221_userdebug",
                "version": "0.0.1rc9",
                "dependencies": None,
                "module": None,
                "shell": None,
                "shbin": None,
                "debug":  None,
                "custom": False,
                "hname": "recovery-pyt2"
        }
        self.uname = {
            "kname": "PyT-Zen",
            "version": self.info["version"],
            "distrotype": "PyT-Recovery",
            "name": self.info["name"],
            "ktype": "PyZen-PyT"
        }

        self.basefs = os.getcwd()
        
        self.ksets = {
                "expm": False,
                "danger": False,
                "autologin": {
                    "active": False,
                    "account": {
                        "name": "root",
                        "password": "root"
                    }
                },
                "accounts": {
                    "root": "root"
                },
                "account_options": {
                    "root": {
                        "root_acc": True
                    }
                }
            }
        self.boot_opt = {"boot": "recovery", "safe_mode": True}

        print(f"Starting recovery with kernel {self.info['name']} {self.info['version']}...")
        if self.info["custom"]:
            print("[WARNING] Recovery modified, work at your own risk!")

        if self.ksets["danger"]:
            print("[WARNING] !!! Kernel/Recovery dangerous/developer functions enabled, don`t except security and stable performance!")

          

        

    def login(self, user, passwd):
        accs = self.ksets["accounts"]
        if user in accs:
            if accs[user] == None:
                self.user = user
                return user       
        if not user in accs:
            self.user = None
            return None
        else:
            if accs[user] != passwd:
                self.user = None
                return None
            elif accs[user] == passwd:
                self.user = user
                return user

    def json_load(self, file):
        with open(file, "r", encoding = "utf-8") as f:
            return json.load(f)

    def close(self):
        return
    def exit(self):
        self.close()
        sys.exit()

    def panic(self, reason):
        print("!!!KERNEL PANIC!!!" + "\n" + "[EMERGENCY]", reason)
        if self.info["custom"]:
            print("!!! [WARNING] Kernel modified, don`t send report! !!!",)
        try:
            while True:
                pass
        except KeyboardInterrupt:
            pass
    
    def startup(self):
        self.user = "root"
        
        i = list(self.info.values())
        i.append(self)

        print("[INFO] Starting Recovery Terminal")
        EXIT = False
        cc = cmds()
        while not EXIT:
            self.cwd = os.getcwd()
            try:
                u_i = input(f"{self.cwd}> ")
                try:
                    parse = u_i.split(" ")
                    if parse[0] in cc.cmds:
                        cc.cmds[parse[0]](parse, self)
                    else:
                        if not u_i.isspace() and not u_i == "":
                            print("[INFO] Unknown command {cmd}".replace("{cmd}", parse[0]))
                except Exception as e:
                    print("[ERROR] Unknown error in command.")
            except KeyboardInterrupt:
                print()
            
class cmds:
    def __init__(self):
        self.cmds = {"update": self.update, "help": self.help, "off": self.off, "chdir": self.chdir, "dir": self.listdir, "uname": self.uname, "ls": self.listdir, "changelog": self.changelog}
        self.help = {"update": "Use update.zip as update.", "help": "Show this message.", "off": "Turn off recovery.", "chdir": "Change dir", "dir": "List directory", "ls": "List directory", "uname": "Get Unix Name", "changelog": "Get Recovery changelog."}
        self.chlog = [
"> Changelog 22.12.21 Experimental:",
"> Implemented uname, changelog.",
"> Dir got alias to ls",
"> update command fixed.",
"> Recovery can start up on Normal Kernel",
"> Also some kernel patches"
        ]

    def chdir(self, args, kernel):
        chdir = "".join(args[1:])
        if os.path.isdir(chdir):
            os.chdir(chdir)

    def listdir(self, args, kernel):
        d = {}
        ldir = "".join(args[1:])
        if not os.path.isdir(ldir):
            ldir = "."
        print(f"List of files/directories in directory {ldir}:")
        ldir = os.listdir(ldir)

        for filedir in sorted(ldir):
            if os.path.isdir(filedir):
                print(f"{filedir} - Directory")
            else:
                print(f"{filedir} - File")
            
                
    def update(self, args, kernel):
        print("[INFO] Trying to find update.zip...")
        try:
            if os.path.isdir("./temp"):
                    shutil.rmtree("./temp")
            if not os.path.isdir("./temp"):
                os.mkdir("./temp")
            if os.path.isfile("./update.zip"):
                unzip_folder("./update.zip", "./temp")
                try:
                    script = dynamic_import("temp.script")
                    print("[INFO] Executing update script...")
                    script.run()
                except Exception as e:
                    print(f"[ERROR] - {type(e).__name__}: {e} - Broken package, aborting...")
                shutil.rmtree("./temp")
            else:
                print("[INFO] Nothing to extract, aborting.")
        except Exception as e:
            print(f"[ERROR] - {type(e).__name__}: {e} - Broken package, aborting...")
            
    def help(self, args, kernel):
        print("Commands:")
        for cmd in self.help:
            print(f"> {cmd}: {self.help[cmd]}")
            
    def off(self, args, kernel):
        sys.exit()

    def uname(self, args, kernel):
        sets = kernel.uname
        print(" ".join(list(sets.values())))

    def changelog(self, args, kernel):
        print("\n".join(self.chlog))

def run():
    kernel = RecoveryKernel()
    print(f"Starting with Python {sys.version}")
    kernel.startup()
