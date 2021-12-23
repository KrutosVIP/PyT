import json, os, sys, importlib, traceback


def dynamic_import(module): # Function to import modules
    return importlib.import_module(module)

def json_load(file):
    with open(file, "r", encoding = "utf-8") as f:
        return json.load(f)

def main() -> None:
    if os.path.isfile("./var/boot.json"): # Check if boot config exists.
        with open("./var/boot.json", "r") as f: # Get boot config
            b = json.load(f)["boot"] # Get boot type
            if b == "recovery": # If boot - recovery - start it.
                boot_recovery()
                
            elif b == "os": # If os - start os
                boot_os()
                
            else: # If unknown boot type.
                print("Emergency: Booting recovery.") 
                boot_recovery()
                    

    else: # If no JSON:
        print("Emergency: Booting recovery - No JSON file")
        boot_recovery()
        
def boot_recovery(file: str = "recovery", kernel = None) -> None: # Recovery starter. File - is recovery module. Kernel - a kernel to boot with.
    try:
        r = dynamic_import(file)
    except:
        print("Emergency: No recovery!!! Something is really wrong!")
    else:
        if kernel == None:
            r.run()
        else:
            print("Another kernel found. Trying to patch it...")
            recoveryKernel = r.RecoveryKernel() # Init Recovery Kernel, but NOT START!
            kernel.startup = r.RecoveryKernel.startup # Change PyT2 Kernel Startup function to Recovery Startup
            
            try:
                ksets = json_load("var/kernel_sets.json") # Load Kernel Settings
                boot_opt = json_load("var/boot.json") # Load Boot Settings
                with open("./var/build_prop.json", "r") as f: # Load build properties
                    data = json.load(f)["properties"]
                    
            except: # If some config not found:
                print("Emergency: No configs found. Starting with premade recovery configs")
                ksets = recoveryKernel.ksets # Get Kernel Settings from Recovery Kernel
                boot_opt = recoveryKernel.boot_opt # Get Boot Options from Recovery Kernel
                data = list(recoveryKernel.info.values()) # Get Build Properties from Recovery Kernel.
            kernel = kernel(data) # Init patched kernel with selected build prop
            kernel.ksets = ksets; kernel.boot_opt = boot_opt # Setup Kernel Settings and Boot Options 
 
            kernel.startup() # Start Recovery
            
    sys.exit()
    
def boot_os(fallback: bool = False) -> None: # If fallback - start fallback hooks to start Recovery with base kernel in recovery mode.
    os.environ["__PYT_OS_ROOT"] = os.getcwd() # Set OS Root to this root.

    scripts = ["etc" + os.path.sep + "init_scripts" + os.path.sep + "normal" + os.path.sep + "init.py", "etc" + os.path.sep + "init_scripts" + os.path.sep + "fallback" + os.path.sep + "init.py"]
    
    try:
        kernel = dynamic_import("kernel.kernel") # Trying to import kernel
    except: 
        print("Emergency: No Kernel found!") # Boot Recovery without kernel
        boot_recovery()
        
    with open("./var/build_prop.json", "r") as f: # Loading build data
        data = json.load(f) 

    # If there is normal scripts and we don`t want to use fallback
    if os.path.exists(scripts[0]) and not fallback: # etc\init_scripts\normal\init.py
        init = dynamic_import("etc.init_scripts.normal.init")
        print("Using normal init...")

    # Fallback
    elif os.path.exists(scripts[1]): # etc\init_scripts\normal\init.py
        init = dynamic_import("etc.init_scripts.fallback.init")
        print("Emergency: Using fallback init...")
        
    else: # If no scripts, start recovery
        print("Emergency: No init scripts?! Trying to boot Recovery with stock (?) kernel")
        boot_recovery(kernel = kernel.BaseKernel)

    try:
        os.environ["__PYT_KERNEL_ROOT"] = os.path.join(os.getcwd() + os.path.sep + "kernel") # Set Kernel root.
        init.init(dynamic_import, "kernel.kernel", data) # start Init, with - dynamic_import function, kernel package and data.

    except SystemExit: # if exit - exit ?)
        sys.exit()
    
    except:
        traceback.print_exc() # If error, print it.

        os.chdir(os.environ["__PYT_OS_ROOT"]) # Change dir to OS Root
        
        if not fallback:# If no fallback was used, start it using fallback
            print("Emergency: Error while using normal startup, use fallback scripts.")
            boot_os(fallback=True)
            
        else: # If Fallback was used, start recovery mode
            print("Emergency: Starting recovery!")
            boot_recovery(kernel = kernel.BaseKernel)


if __name__ == "__main__":
    main()
