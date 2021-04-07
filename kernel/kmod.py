import os, sys, importlib, shutil, json

def dynamic_import(module):
    return importlib.import_module(module)

sys.path.insert(0, f"./types")
from binary import Binary
from module import Module

def load_modules(modules, lines_l, debug):
    mods = {}
    if debug:
        print(f"{lines_l['load']}")
    
    files = os.listdir(modules)
    sys.path.insert(0, f"{modules}")
    
    for mod in files:
        if mod != "__pycache__" and not os.path.isdir(f"{modules}/{mod}"):
            
            try:
                m = dynamic_import(os.path.splitext(mod)[0])
                
            except Exception as e:
                if debug:
                    print(f"{lines_l['error']} - {type(e).__name__}: {e}")
                
            m = m.__dict__
            for el in m:
                try:
                    if type(m[el]).__name__ == "type":
                        
                        if issubclass(m[el], Module) and m[el] != Module:
                            if debug:
                                print(f"{lines_l['module']}: {el}")
                            mod_temp = m[el]()
                            if mod_temp.info["codename"] in mods:
                                pass
                            else:
                                mods.update( {mod_temp.info["codename"]: mod_temp})
                except Exception as e:
                    if debug:
                        print(e)
                    
    sys.path.pop(0)
    if debug:
        print(f"{lines_l['success']}")
    return mods

def load_binaries(bins, lines_l, debug):
    binaries = {}
    if debug:
        print(f"{lines_l['load']}")
    
    files = os.listdir(bins)
    sys.path.insert(0, f"{bins}")
    
    for binary in files:
        if binary != "__pycache__" and not os.path.isdir(f"{bins}/{binary}"):

            
            try:
                b = dynamic_import(os.path.splitext(binary)[0])
                
            except Exception as e:
                if debug:
                    print(f"{lines_l['error']} - {type(e).__name__}: {e}")
            else:
                b = b.__dict__
                
                for el in b:
                    try:
                        if type(b[el]).__name__ == "type":
                            
                            if issubclass(b[el], Binary) and b[el] != Binary:
                                if debug:
                                    print(f"{lines_l['binary']}: {el}")
                                bin_temp = b[el]()
                                
                                if bin_temp.info["codename"] in binaries:
                                    pass
                                else:
                                    binaries.update( {bin_temp.info["codename"]: bin_temp})
                                    
                    except Exception as e:
                        if debug:
                            print(e)
                    
                
                    
    sys.path.pop(0)
    if debug:
        print(f"{lines_l['success']}")
    return binaries


    
