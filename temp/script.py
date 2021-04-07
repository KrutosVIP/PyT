import os, importlib, json, sys

def run():
    print("Hello World!")
    reboot()
    sys.exit()

def reboot():
    sys.path.append(os.getcwd())
    try:
        with open("var/boot.json", "r") as f:
            b = json.load(f)
            b["boot"] = "os"
            with open("var/boot.json", "w") as f:
                json.dump(b, f)
    except:
        pass
    for f in dir():
        if f not in ["importlib"]:
            del f
    def dynamic_import(module):
        return importlib.import_module(module)
    r = dynamic_import("kinit").main()

run()
