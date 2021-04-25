import sys, importlib, os

def dynamic_import(module):
    return importlib.import_module(module)

def execute(self, file):
    try:
        sys.path.append(os.path.dirname(file))
        m = dynamic_import(os.path.basename(file))
        return sys.path.pop()
    except ModuleNotFoundError:
        pass

def executable(self, file):
    if os.path.isdir(file) and os.path.splitext(file)[1] == ".py":
        return file, True
    else:
        if os.path.isfile(os.path.abspath(self.fs[1].replace("\\", "/") + "/" + file.replace("\\", "/"))) and os.path.splitext(file)[1] == ".py":
            return os.path.abspath(self.fs[1].replace("\\", "/") + "/" + file.replace("\\", "/")), True
        else:
            if os.path.isfile(os.path.abspath(file)) and os.path.splitext(file)[1] == ".py":
                return os.path.abspath(file), True
            else:
                return None, False
