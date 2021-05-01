import json, os, sys, importlib
from fs.memoryfs import MemoryFS
from fs.osfs import OSFS
from fs.mountfs import MountFS

sys.path.append("./kernel")
from kmod import load_modules, load_binaries, load_binaries_dynamic
from ksystemctl import SystemCTL
class BaseKernel:
    def __init__(self, info: list):
        """
    Example info:
    [
        "my kernel",
        "v1",
        [],
        "./module",
        "pyt2",
        "./bin",
        True,
        False,
        "pyt2"
    ]
    """
        self.info = {
                "name": info[0],
                "version": info[1],
                "dependencies": info[2],
                "module": info[3],
                "shell": info[4],
                "shbin": info[5],
                "debug": info[6],
                "custom": info[7],
                "hname": info[8]
        }
        debug = self.info['debug']

        self.uname = {
            "kname": "PyT-Zen",
            "version": self.info["version"],
            "distrotype": "PyT-v2",
            "name": self.info["name"],
            "ktype": "PyZen-PyT"
        }

        self.basefs = os.getcwd()
        if not os.path.isdir(f"{self.basefs}/../data"):
            os.mkdir(f"{self.basefs}/../data")
        if debug:
            print("DEBUG: Reading language...")
        self.lang = self.json_load("../var/kernel_sets.json")["lang"]
        
        if debug:
            print("DEBUG: Reading language files...")
        try:
            self.lines = self.json_load(f"../lang/global_{self.lang}.json")
        except FileNotFoundError:
            print("[WARNING] Language " + self.lang + " doesn't exists! Setting language to en...")
            self.lines = self.json_load(f"../lang/global_en.json")

        if debug:
            print(f"{self.lines['kernel']['kstart_0_debug']} {self.info['name']} {self.info['version']} {self.lines['kernel']['kstart_1']} {self.info['shell']}")
        else:
            print(f"{self.lines['kernel']['kstart_0']} {self.info['name']} {self.info['version']} {self.lines['kernel']['kstart_1']} {self.info['shell']}")

        if self.info["custom"]:
            print(self.lines['kernel']['kernel_mod'])

        if debug:
            print(f"{self.lines['kernel']['interpretator']} {sys.version}")
        if debug:
            print(self.lines['kernel']['os_mem_fs_start'])
        
        if debug:
            print(f"DEBUG: {self.lines['debug']['osfs_c']}")
        self.mount_all()
        if debug:
            print(self.lines['kernel']['load_mod_bin'])
        self.modules = load_modules(self.info["module"], self.lines['modules'], debug)
        
        if debug:
            print(self.lines['kernel']['startup'])
        
        self.startup()
        

    def login(self, user, passwd):
        with open(f"{self.basefs}/../var/kernel_sets.json", "r") as f:
            d = f.read()
            accs = json.loads(d)["accounts"]
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

    def mount_all(self):
        self.fs = OSFS("../")

    def exit(self):
        self.sctl.end()
        self.fs.close()
        sys.exit()

    def panic(self, reason):
        print(self.lines['kernel']['kpanic'] + "\n" + self.lines['kernel']["kpanic_1"], reason)
        if self.info["custom"]:
            print(self.lines['pyt']['kmodify_kpanic'])
        try:
            while True:
                pass
        except KeyboardInterrupt:
            pass
    
    def startup(self):
        debug = self.info['debug']
        self.user = None
        e = 0
        for d in self.info["dependencies"]:
            if not d in self.modules:
                print(self.lines['kernel']["startup_error_0"].replace("%s", d))
                e = 1
        if e == 1:
            print(self.lines['kernel']["startup_error_1"])
            self.exit()
        
        i = list(self.info.values())
        i.append(self.modules); i.append(None)
        i.append(self.lines); i.append(self.fs); i.append("[REMOVED FEATURE]"); i.append(self)
        
        self.sctl = SystemCTL()
        self.sctl.start(f"{self.basefs}/../var/events/", i)

        dcmd = self.json_load("../var/kernel_sets.json")["dynamic_cmd"]
        if dcmd:
            self.binaries = load_binaries_dynamic(self.info["shbin"], self.lines['binary'], debug)
        else:
            self.binaries = load_binaries(self.info["shbin"], self.lines['binary'], debug)

        i = list(self.info.values())
        i.append(self.modules); i.append(self.binaries)
        i.append(self.lines); i.append(self.fs); i.append("[REMOVED FEATURE]"); i.append(self)
        
        for mod in self.modules:
            self.modules[mod].info["on_load"](i)
            
        self.sctl = SystemCTL()
        self.sctl.start(f"{self.basefs}/../var/events/", i)

        dcmd = self.json_load("../var/kernel_sets.json")["dynamic_cmd"]
        if dcmd:
            self.binaries = load_binaries_dynamic(self.info["shbin"], self.lines['binary'], debug)
        else:
            self.binaries = load_binaries(self.info["shbin"], self.lines['binary'], debug)
        
        if "plm" in self.modules:
            if self.modules["plm"].info["login-manager"]:
                self.user = self.modules["plm"].run(i)
        if "console" in self.modules[self.info["shell"]].info.keys():
            if self.modules[self.info["shell"]].info["console"]:
                self.modules[self.info["shell"]].run(i)


            
        
        
