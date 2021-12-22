import os, json, shutil

def get_prop(info):
    try:
        while True:
            result = input(f"{info}?> ")
            return result
    except:
        print("Cancelled.")
        return None

def ask(info):
    types = {
    "Y": True, "N": False, "YES": True, "NO": True
    }
    try:
        while True:
            result = input(f"{info} (Y/N/Yes/No)?> ")
            if types.get(result.upper()) == None:
                print("Unknown answer.")
            else:
                return types.get(result.upper())
    except:
        print("Cancelled.")
        return None
    
def configure_check(info, pyt, package):
    config = os.path.join(package, "config.json")
    
    if os.path.isfile(config):
        with open(config, "r", encoding="utf-8") as f:
            try:
                config = json.loads(config)
                if not "ro.pyt.package" in config: raise ValueError()
            except:
                print("Broken config. Package cannot be installed.")
                return False
            
    print("Getting PyT Version... ", end="")
    print(info.info[1])
    print("Getting Kernel Version... ", end="")
    print(info.info[0])

def configure(info, pyt, package):
    config = os.path.join(package, "config.json")

    if os.path.isfile(config):
        with open(config, "r", encoding="utf-8") as f:
            try:
                config = json.loads(config)
                if not "ro.pyt.package" in config: raise ValueError()
            except:
                print("Broken config. Restart pkg_build.")
                os.remove(os.path.join(package, "config.json"))
                return
    else:
        name = get_prop("Name")
        version = get_prop("Version")
        author = get_prop("Author")
        ver_static = ask("Works only on this version")
        
        config = {
            "ro.pyt.version": None,
            "ro.pyt.kernel": None,

            "ro.pyt.package": {
                "package.name": name,
                "package.version": version,
                "package.author": author
            },

            "ro.pyt.package.version_depend": ver_static
        }

    print("Generating config...")

    config["ro.pyt.version"] = info.info[1]
    config["ro.pyt.kernel"] = info.info[0]

    print("Writing config...")

    with open(os.path.join(package, "config.json"), "w", encoding="utf-8") as f:
        json.dump(config, f, indent=4)
