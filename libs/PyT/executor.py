import sys, importlib, os

def dynamic_import(module):
    return importlib.import_module(module)
def shexecute(self, file):
    try:
        with open(file) as f:
            base = f.read()
            for cmd in base.split("\n"):
                self.system(cmd)
    except FileNotFoundError:
        pass
    return 

def shexecutable(self, file):
    if os.path.isfile(file) and os.path.splitext(file)[1] == ".sh":
        return file, True
    else:
        if os.path.isfile(os.path.abspath(self.fs[1].replace("\\", "/") + "/" + file.replace("\\", "/"))) and os.path.splitext(file)[1] == ".sh":
            return os.path.abspath(self.fs[1].replace("\\", "/") + "/" + file.replace("\\", "/")), True
        else:
            if os.path.isfile(os.path.abspath(file)) and os.path.splitext(file)[1] == ".sh":
                return os.path.abspath(file), True
            else:
                return None, False
def execute(self, file):
    try:
        sys.path.append(os.path.dirname(file))
        base = os.getcwd()
        os.chdir(os.path.dirname(file))
        m = dynamic_import(os.path.basename(file))

    except ModuleNotFoundError:
        pass
    os.chdir(base)
    return sys.path.pop()

def executable(self, file):
    if os.path.isfile(file) and os.path.splitext(file)[1] == ".py":
        return file, True
    else:
        if os.path.isfile(os.path.abspath(self.fs[1].replace("\\", "/") + "/" + file.replace("\\", "/"))) and os.path.splitext(file)[1] == ".py":
            return os.path.abspath(self.fs[1].replace("\\", "/") + "/" + file.replace("\\", "/")), True
        else:
            if os.path.isfile(os.path.abspath(file)) and os.path.splitext(file)[1] == ".py":
                return os.path.abspath(file), True
            else:
                return None, False
