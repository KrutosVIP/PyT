import sys, os, json, importlib, shutil, gc


def dynamic_import(mod):
    return importlib.import_module(os.path.splitext(mod)[0])

# DO NOT CREATE SMTH WITH THIS OK?! It will not load! This is only for dynamic binary realisation, it is full auto

class DBinary(object):
    def __init__(self, file, name, Binary):
        self.info = {
            "name" : "undefined",
            "file": file,
            "version" : "undefined",
            "codename": name,
            "dependencies" : [],
            "run": self.run
        }
        self.binary = Binary
        self.get_info()

    def refresh(self):
        gc.collect()

    def get_info(self):
        file_exc, execute_var = self.executable(self.info["file"])
        if execute_var:
            try:
                sys.path.append(os.path.dirname(self.info["file"]))
                m = dynamic_import(os.path.basename(self.info["file"]))
                m = self.get_class(m)
                self.info["version"] = m.info["version"]
                self.info["name"] = m.info["name"]
                self.info["dependencies"] = m.info["dependencies"]
                return sys.path.pop()
            except ModuleNotFoundError:
                pass
        else:
            return
        pass

    def run(self, info, pyt):
        file_exc, execute_var = self.executable(self.info["file"])
        if execute_var:
            try:
                sys.path.append(os.path.dirname(self.info["file"]))
                self.refresh()
                m = dynamic_import(os.path.basename(self.info["file"]))
                try:
                    importlib.reload(m)
                except:
                    pass
                m = self.get_class(m)
                info2 = m.info["run"](info, pyt)
                del sys.modules[os.path.basename(self.info["file"])[:-3]]
                del m
                sys.path.pop()
                return info2
            except ModuleNotFoundError:
                pass
        else:
            return
        pass

    def get_class(self, b):
        binaries = {}
        sys.path.insert(0, os.path.dirname(f"{self.info['file']}"))
        b = b.__dict__            
        for el in b:
            try:
                if type(b[el]).__name__ == "type":
                    if issubclass(b[el], self.binary) and b[el] != self.binary:
                        bin_temp = b[el]()
                        if not type(bin_temp.info["codename"]).__name__  in ("tuple", "list"):
                            if bin_temp.info["codename"] == self.info["codename"]:
                                        return bin_temp
                            else:
                                pass               
                        elif type(bin_temp.info["codename"]).__name__  in ("tuple", "list"):
                            for name in bin_temp.info["codename"]:
                                if name == self.info["codename"]:
                                    return bin_temp
                                else:
                                    pass
            except Exception as e:
                print(e)

    def executable(self, file):
        if os.path.isfile(file) and os.path.splitext(file)[1] == ".py":
            return file, True
        else:
            if os.path.isfile(os.path.abspath(file.replace("\\", "/"))) and os.path.splitext(file)[1] == ".py":
                return os.path.abspath(file.replace("\\", "/")), True
            else:
                if os.path.isfile(os.path.abspath(file)) and os.path.splitext(file)[1] == ".py":
                    return os.path.abspath(file), True
                else:
                    return None, False
