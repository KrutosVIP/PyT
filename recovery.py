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
                "name": "PyT-RKernel_17-54_090421_userdebug",
                "version": "0.0.1rc2",
                "dependencies": None,
                "module": None,
                "shell": None,
                "shbin": None,
                "debug":  None,
                "custom": False,
                "hname": "recoverypyt2"
        }
        self.cwd = os.getcwd()
        print(f"Starting recovery with kernel {self.info['name']} {self.info['version']}...")
        if self.info["custom"]:
            print("[WARNING] Recovery modified, work at your own risk!")
        self.ram_fs = MemoryFS()
        self.fs = OSFS("../")
        self.startup()
        
    def ramfs_load(self):
        subfs = self.ram_fs.makedir("/lang/")
        with subfs.open('global.json', "w") as mf:
            with open(f"../lang/global_{self.lang}.json", "r") as f:
                mf.write(f.read())
        subfs.close()
        subfs = self.ram_fs.makedir("/var/")
        for file in os.listdir("../var/"):
            with subfs.open(file, "w") as mf:
                with open(f"../var/{file}", "r") as f:
                    mf.write(f.read())
        subfs.close()

    def json_load(self, file):
        with open(file, "r") as f:
            return json.load(f)

    def exit(self):
        self.ram_fs.close()
        self.fs.close()
        sys.exit()

    def startup(self):
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
                        cc.cmds[parse[0]](parse)
                    else:
                        if not u_i.isspace() and not u_i == "":
                            print("[INFO] Unknown command {cmd}".replace("{cmd}", parse[0]))
                except Exception as e:
                    print("[ERROR] Unknown error in command.")
            except KeyboardInterrupt:
                print()
            
class cmds:
    def __init__(self):
        self.cmds = {"update": self.update, "help": self.help, "off": self.off, "chdir": self.chdir, "dir": self.listdir}
        self.help = {"update": "Use update.zip as update.", "help": "Show this message.", "off": "Turn off recovery.", "chdir": "Change dir", "dir": "List directory"}

    def chdir(self, args):
        chdir = "".join(args[1:])
        if os.path.isdir(chdir):
            os.chdir(chdir)

    def listdir(self, args):
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
            
                
    def update(self, args):
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
                shutil.rmtree("./temp")
            else:
                print("[INFO] Nothing to extract, aborting.")
        except Exception as e:
            print(f"[ERROR] - {type(e).__name__}: {e} - Broken package, aborting...")
            
    def help(self, args):
        print("Commands:")
        for cmd in self.help:
            print(f"> {cmd}: {self.help[cmd]}")
            
    def off(self, args):
        sys.exit()

def run():
    d = RecoveryKernel()
