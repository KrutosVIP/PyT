import json, os, sys, importlib
from fs.memoryfs import MemoryFS
from fs.osfs import OSFS
from fs.mountfs import MountFS

sys.path.append("./kernel")
from kmod import load_modules, load_binaries
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
        
        if debug:
            print("DEBUG: Reading language...")
        self.lang = self.json_load("../var/kernel_sets.json")["lang"]
        
        if debug:
            print("DEBUG: Reading language files...")
        self.lines = self.json_load(f"../lang/global_{self.lang}.json")
    
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
            print(f"DEBUG: {self.lines['debug']['mfs_c']}")
        self.ram_fs = MemoryFS()
        
        if debug:
            print(f"DEBUG: {self.lines['debug']['osfs_c']}")
        self.fs = OSFS("../")

        if debug:
            print(f"DEBUG: {self.lines['debug']['mfs_c_2']}")
        self.ramfs_load()
        if debug:
            print(self.lines['kernel']['load_mod_bin'])
        self.modules = load_modules(self.info["module"], self.lines['modules'], debug)
        self.binaries = load_binaries(self.info["shbin"], self.lines['binary'], debug)
        if debug:
            print(self.lines['kernel']['startup'])
        
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
        e = 0
        for d in self.info["dependencies"]:
            if not d in self.modules:
                print(self.lines['kernel']["startup_error_0"].replace("%s", d))
                e = 1
        if e == 1:
            print(self.lines['kernel']["startup_error_1"])
            self.exit()
        for mod in self.modules:
            i = list(self.info.values())
            i.append(self.modules); i.append(self.binaries)
            i.append(self.lines); i.append(self.fs); i.append(self.ram_fs); i.append(self)
            self.modules[mod].info["on_load"](i)

        if "console" in self.modules[self.info["shell"]].info.keys():
            if self.modules[self.info["shell"]].info["console"]:
                self.modules[self.info["shell"]].run(i)


            
        
        
