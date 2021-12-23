import json, os, sys, importlib
from fs.memoryfs import MemoryFS
from fs.osfs import OSFS
from fs.mountfs import MountFS

from shutil import copyfile

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
        
        self.uname = {
            "kname": "PyT-Zen",
            "version": self.info["version"],
            "distrotype": "PyT-v2",
            "name": self.info["name"],
            "ktype": "PyZen-PyT"
        }
        

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

    def close(self):
        self.boot_opt = self.json_load(f"{self.basefs}/../var/boot.json")
        if not self.boot_opt["safe_mode"]:
            self.sctl.end()
        if self.boot_opt["safe_mode"]:
            try:
                copyfile(f"{self.basefs}/../etc/kbackup/kernel_sets.json", f"{self.basefs}/../var/kernel_sets.json")
                copyfile(f"{self.basefs}/../etc/kbackup/build_prop.json", f"{self.basefs}/../var/build_prop.json")
            except:
                pass

            try:
                os.remove(f"{self.basefs}/../etc/kbackup/safe.lock")
            except:
                pass
        self.boot_opt["safe_mode"] = False
        with open(f"{self.basefs}/../var/boot.json", "w", encoding="utf-8") as f:
            json.dump(self.boot_opt, f)
        self.fs.close()

    def exit(self):
        self.close()
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
    


    def safe_boot(self):
            if not os.path.isdir("../etc/kbackup"):
                os.mkdir("../etc/kbackup")
            print(self.lines['kernel']['kernel_safe'])
            copyfile("../var/build_prop.json", "../etc/kbackup/build_prop.json")
            copyfile("../var/kernel_sets.json", "../etc/kbackup/kernel_sets.json")
            brop = self.json_load("../var/build_prop.json")
            brop["properties"][6] = True; brop["properties"][7] = False # Enable Debug, disable Mod Kernel
            self.info["custom"] = False; self.info["debug"] = True
            with open("../var/build_prop.json", "w", encoding="utf-8") as f:
                json.dump(brop, f, indent = 4)

            ksts = self.json_load("../var/kernel_sets.json")
            ksts["expm"] = False; ksts["danger"] = False # Disable experimental features and kernel danger.
            ksts["lang"] = "en"; ksts["plm"]["plm_type"] = 0
            if os.path.isfile("../etc/iceberg/dpkg.json"):
                ksts["dynamic_cmd"] = True
            else:
                if not os.path.isdir("../etc/iceberg"):
                    os.mkdir("../etc/iceberg")
                ksts["dynamic_cmd"] = False
                
            with open("../var/kernel_sets.json", "w", encoding="utf-8") as f:
                json.dump(ksts, f, indent = 4)
                
            self.ksets = self.json_load(f"{self.basefs}/../var/kernel_sets.json")
            self.boot_opt = self.json_load(f"{self.basefs}/../var/boot.json")

            with open("../etc/kbackup/safe.lock", "w", encoding="utf-8") as f:
                f.write("0")


# Settings 
__kernel = BaseKernel
        
        
