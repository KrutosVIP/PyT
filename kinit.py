import json, os, sys, importlib


def dynamic_import(module):
    return importlib.import_module(module)

def main():
    if os.path.isfile("./var/build_prop.json"):
        with open("./var/build_prop.json", "r") as f:
            d = json.load(f)
    if os.path.isfile("./var/boot.json"):
        with open("./var/boot.json", "r") as f:
            b = json.load(f)["boot"]
            if b == "recovery":
                try:
                    r = dynamic_import("recovery")
                except:
                    print("Emergency: No recovery!!!")
                else:
                    r.run()
                    sys.exit()
            elif b == "os":
                boot_os()
            else:
                print("Emergency: Booting recovery.")
                try:
                    r = dynamic_import("recovery")
                except:
                    print("Emergency: No recovery!!!")
                else:
                    r.run()
                    sys.exit()
    else:
        print("Emergency: Booting recovery - No JSON file")
        try:
            r = dynamic_import("recovery")
        except:
            print("Emergency: No recovery!!!")
        else:
            r.run()
            sys.exit()
        

def boot_os():
    from kernel import kernel
    with open("./var/build_prop.json", "r") as f:
        d = json.load(f)
    os.chdir("./kernel")
    kernel.BaseKernel(d["properties"])

main()
