import sys, json, os, importlib
from colorama import Back, Fore, Style
from colorama import init as cinit
import argparse
sys.path.insert(0, "../types")
cinit()
from binary import Binary
from prompt_toolkit.shortcuts import checkboxlist_dialog
from PyT.rebootgui import reboot_gui

class Reboot(Binary):
    def __init__(self):
        self.info = {
            "name" : "Reboot.",
            "version" : "v1",
            "codename": "reboot",
            "dependencies" : [], # Not Supported.
            "description": "Reboot. Args - os/recovery",
            "run": self.run
        }
    
    def json_load(self, file):
        with open(file, "r") as f:
            return json.load(f)


    def safe_mode(self, lang):
        session = True
        while session:
            answer = input(lang["yes_no"])
            if answer.lower() in ["yes", "yse", "ys", "y", "ye", "es", "s", "e"]:
                return True
            if answer.lower() in ["no", "n", "o", "on"]:
                return False            

    def run(self, info, pyt):
        lang = self.json_load(f"{info.info[14].basefs}/../var/kernel_sets.json")["lang"]
        if os.path.isfile(f"{info.info[14].basefs}/../lang/reboot_{lang}.json"):
            with open(f"{info.info[14].basefs}/../lang/reboot_{lang}.json", "r") as f:
                lang = json.load(f)
        else:
            print("No lang file, using default En translation.")
            lang = {
	"boot_option": ["[Success] Installed {args} boot option", "[Success] Installed os boot option"],
	"unknown_boot": "[Error] Unknown boot option.",
	"no_file": "[Error] No /var/boot.json!",
	"config": "Configure reboot",
	"reboot": "Reboot", 
	"boot_os": "Boot OS",
	"boot_recovery": "Boot Recovery mode",
	"yes_no": "Input Yes or No> ",
	"options": "Reboot | Options",
	"safemode": "Safe Mode",
	"safety": "Safe mode enabled."
            }
        args = info.info[15].split(" ")[1:]
        if len(args) > 0:
            args = args[0]
            if os.path.isfile(f"{info.info[14].basefs}/../var/boot.json"):
                with open(f"{info.info[14].basefs}/../var/boot.json", "r") as f:
                    b = json.load(f)
                if args in ["recovery", "os"]:
                    b["boot"] = args

                    print(lang["boot_option"][0].replace("{args}", args))
                    if args == "os":
                        if not info.info[14].boot_opt["safe_mode"]:
                            b["safe_mode"] = self.safe_mode(lang)
                        else:
                            b["safe_mode"] = False
                    if b["safe_mode"]:
                        print(lang["safety"])
                    with open(f"{info.info[14].basefs}/../var/boot.json", "w") as f:
                        json.dump(b, f)
                    reboot(self, info)
                elif args == "gui":
                    options = reboot_gui(
                    title=lang["options"],
                    text= lang["config"],
                    ok_text = lang["reboot"],
                    values2 = [ ("os", lang["boot_os"]), ("recovery", lang["boot_recovery"])],
                    values = [("safe_mode", lang["safemode"])]
                    ).run()
                    
                    b["boot"] = options[0]
                    if "safe_mode" in options[1]:
                        if not info.info[14].boot_opt["safe_mode"]:
                            b["safe_mode"] = True
                        else:
                            b["safe_mode"] = True
                    else:
                        b["safe_mode"] = False
                    with open(f"{info.info[14].basefs}/../var/boot.json", "w") as f:
                        json.dump(b, f)
                    print(lang["boot_option"][0].replace("{args}", args))
                    if b["safe_mode"]:
                        print(lang["safety"])
                    reboot(self, info)
                else:
                    return
            else:
                print(lang["no_file"])
        else:
            if os.path.isfile(f"{info.info[14].basefs}/../var/boot.json"):
                with open(f"{info.info[14].basefs}/../var/boot.json", "r") as f:
                    b = json.load(f)
                options = reboot_gui(
                title=lang["options"],
                text= lang["config"],
                ok_text = lang["reboot"],
                values2 = [ ("os", lang["boot_os"]), ("recovery", lang["boot_recovery"])],
                values = [("safe_mode", lang["safemode"])]
                ).run()
                    
                b["boot"] = options[0]
                if "safe_mode" in options[1]:
                    b["safe_mode"] = True
                else:
                    b["safe_mode"] = False
                with open(f"{info.info[14].basefs}/../var/boot.json", "w") as f:
                    json.dump(b, f)
                print(lang["boot_option"][0].replace("{args}", "os"))
                if b["safe_mode"]:
                    print(lang["safety"])
                reboot(self, info)

def reboot(self, info):
    boot = self.json_load(f"{info.info[14].basefs}/../var/boot.json")
    boot2 = boot.copy()
    boot2["safe_mode"] = False
    with open(f"{info.info[14].basefs}/../var/boot.json", "w") as f:
        json.dump(boot2, f)
    if not info.info[14].boot_opt["safe_mode"]:
        info.info[14].close()
    with open(f"{info.info[14].basefs}/../var/boot.json", "w") as f:
        json.dump(boot, f)
    os.chdir(f"{info.info[14].basefs}/..")
    for f in dir():
        if f not in ["importlib", "info"]:
            del f
    def dynamic_import(module):
        return importlib.import_module(module)
    
    r = dynamic_import("kinit").main()
    sys.exit()
