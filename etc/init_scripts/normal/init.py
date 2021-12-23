import json, os, sys, importlib
from fs.memoryfs import MemoryFS
from fs.osfs import OSFS
from fs.mountfs import MountFS

from shutil import copyfile

sys.path.append("./kernel")
from kmod import load_modules, load_binaries, load_binaries_dynamic
from ksystemctl import SystemCTL

import os
def init(dimport, kernel, data):
    os.chdir("./kernel")

    kernel = dimport(kernel).__kernel # Use passed import function and import kernel, we need this because of some modules
    
    kernel.startup = KernelFunctions.startup
    kernel.early_hooks = KernelFunctions.early_hooks

    kernel = kernel(data["properties"])
    params()
    kernel.startup()

def params():
    os.environ["__PYT_OS_FALLBACK"] = "TRUE"

class KernelFunctions:
    def startup(self):
        self.early_hooks()
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
        if not self.boot_opt["safe_mode"]:
            self.sctl = SystemCTL()
            self.sctl.start(f"{self.basefs}/../var/events/", i)
        dcmd = self.json_load("../var/kernel_sets.json")["dynamic_cmd"]
        if dcmd:
            self.binaries = load_binaries_dynamic(self.info["shbin"], self.lines['binary'], debug)
        else:
            if self.boot_opt["safe_mode"]:
                self.binaries = load_binaries_dynamic(self.info["shbin"], self.lines['binary'], debug)
            else:
                self.binaries = load_binaries(self.info["shbin"], self.lines['binary'], debug)
        i = list(self.info.values())
        i.append(self.modules); i.append(self.binaries)
        i.append(self.lines); i.append(self.fs); i.append("[REMOVED FEATURE]"); i.append(self)
        if not self.boot_opt["safe_mode"]:
            for mod in self.modules:
                self.modules[mod].info["on_load"](i)
        if not self.boot_opt["safe_mode"]:
            if "plm" in self.modules:
                if self.modules["plm"].info["login-manager"]:
                    self.user = self.modules["plm"].run(i)
        if "console" in self.modules[self.info["shell"]].info.keys():
            if self.modules[self.info["shell"]].info["console"]:
                self.modules[self.info["shell"]].run(i)

    def early_hooks(self):
        debug = self.info['debug']
        if not os.path.isdir("../etc/"):
            os.mkdir("../etc/")
        if not os.path.isdir("../etc/systemctl"):
            os.mkdir("../etc/systemctl")
        if not os.path.isdir("../etc/iceberg"):
            os.mkdir("../etc/iceberg")

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
        self.ksets = self.json_load(f"{self.basefs}/../var/kernel_sets.json")
        self.boot_opt = self.json_load(f"{self.basefs}/../var/boot.json")

        
        if self.boot_opt["safe_mode"]:
            if os.path.exists(f"{self.basefs}/../etc/kbackup/safe.lock"):
                try:
                    os.remove(f"{self.basefs}/../etc/kbackup/safe.lock")
                    copyfile(f"{self.basefs}/../etc/kbackup/kernel_sets.json", f"{self.basefs}/../var/kernel_sets.json")
                    copyfile(f"{self.basefs}/../etc/kbackup/build_prop.json", f"{self.basefs}/../var/build_prop.json")
                except:
                    pass
                self.safe_boot()
            else:
                self.safe_boot()

        if debug:
            print(f"{self.lines['kernel']['kstart_0_debug']} {self.info['name']} {self.info['version']} {self.lines['kernel']['kstart_1']} {self.info['shell']}")
        else:
            print(f"{self.lines['kernel']['kstart_0']} {self.info['name']} {self.info['version']} {self.lines['kernel']['kstart_1']} {self.info['shell']}")

        if self.info["custom"]:
            print(self.lines['kernel']['kernel_mod'])

        if self.ksets["danger"]:
            print(self.lines['kernel']['kernel_danger'])

        if self.ksets["expm"]:
            print(self.lines['kernel']['kernel_expm'])
          
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

