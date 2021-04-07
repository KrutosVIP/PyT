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
                "name": "PyT-RKernel_21-17_050321_userdebug",
                "version": "0.0.1a0",
                "dependencies": None,
                "module": None,
                "shell": None,
                "shbin": None,
                "debug": True
        }
        self.ram_fs = MemoryFS()
        self.fs = OSFS("../")
        print(f"Starting recovery with kernel {self.info['name']} {self.info['version']}...")
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
        print("[INFO] Trying to find update.zip...")
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


        self.exit()
def run():
    d = RecoveryKernel()
