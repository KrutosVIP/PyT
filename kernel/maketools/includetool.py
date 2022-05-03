# Tools for make scripts. Need to include manually.
import importlib.util, random, os, pathlib, shutil

def include_module(path):
    if os.path.exists(path):
        spec = importlib.util.spec_from_file_location(f"included-{random.randint(0, 999999)}", path)

        if not spec:
            return 

        module = importlib.util.module_from_spec(spec)

        
        spec.loader.exec_module(module)
        
        return module
    return os.path.exists(path)

def log(*args, **kwargs):
    print("make:", *args, **kwargs)

def error(*args, **kwargs):
    print("make: ended up with error:", *args, **kwargs)

def cleantool():
  for root, dirs, files in os.walk("."):
      for dir in dirs:
          if dir == "__pycache__":
              shutil.rmtree(os.path.join(root, dir))

