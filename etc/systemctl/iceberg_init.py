import sys, os, json, importlib

def dynamic_import(module):
    return importlib.import_module(module)

sys.path.insert(0, f"./types")
from binary import Binary

class Iceberg_init:
    def write(basedir, text):
        with open(f"{basedir}/../etc/iceberg/dpkg.json", "w", encoding = "utf-8") as f:
            return json.dump(text, f, indent = 4)
    
    def index(i, basedir):
        binaries = {}
        bins = i[14].info["shbin"]
        files = os.listdir(bins)
        sys.path.insert(0, f"{bins}")

        for binary in files:
            if binary != "__pycache__" and not os.path.isdir(os.path.abspath(f"{i[14].basefs}/{bins}/{binary}".replace("\\", "/"))):
                try:
                    b = dynamic_import(os.path.splitext(binary)[0])
                except Exception as e:
                    print(e)
                else:
                    b = b.__dict__
                    for el in b:
                        try:
                            if type(b[el]).__name__ == "type":
                                if issubclass(b[el], Binary) and b[el] != Binary:
                                    bin_temp = b[el]()
                                    if not type(bin_temp.info["codename"]).__name__  in ("tuple", "list"):
                                        if bin_temp.info["codename"] in binaries:
                                            pass
                                        else:
                                            binaries.update( {bin_temp.info["codename"]: os.path.abspath(f"{i[14].basefs}/{bins}/{binary}".replace("\\", "/"))})
                                    elif type(bin_temp.info["codename"]).__name__  in ("tuple", "list"):
                                            for name in bin_temp.info["codename"]:
                                                if name in binaries:
                                                    pass
                                                else:
                                                    binaries.update( {name: os.path.abspath(f"{i[14].basefs}/{bins}/{binary}".replace("\\", "/"))})                                 
                        except Exception as e:
                            pass
        sys.path.pop(0)

        Iceberg_init.write(basedir, binaries)
def start(i, basedir):
    Iceberg_init.index(i, basedir)
