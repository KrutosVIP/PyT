import sys, json, os, importlib
from colorama import Back, Fore, Style
from colorama import init as cinit
import argparse
sys.path.insert(0, "../types")
cinit()
from binary import Binary

from prompt_toolkit.shortcuts import yes_no_dialog
from PyT.pytconfutils import pytconf, plmconf
class PyTconf(Binary):
    def __init__(self):
        self.info = {
            "name" : "PyT Configure",
            "version" : "v1",
            "codename": "pytconf",
            "dependencies" : [], # Not Supported.
            "description": "PyT Configure",
            "run": self.run,
            "on_load": self.on_load
        }
    
    def json_load(self, file):
        with open(file, "r", encoding="utf-8") as f:
            return json.load(f)

    def on_load(self, info):
        pass

    def json_write(self, file, text):
        with open(file, "w", encoding="utf-8") as f:
            json.dump(text, f, indent=4)

    def write_plmconf(self, kconf, info):
        ksets = self.json_load(f"{info.info[14].basefs}/../var/kernel_sets.json")
        if "invisible" in kconf[0]:
            ksets["plm"]["invisible"] = True
        else:
            ksets["plm"]["invisible"] = False

        ksets["plm"]["plm_type"] = kconf[1]
        
        self.json_write(f"{info.info[14].basefs}/../var/kernel_sets.json", ksets)
        
    def write_pytconf(self, buildp, kconf, info):
        buildp["properties"][0] = kconf[0]
        buildp["properties"][1] = kconf[1]
        if "debug" in kconf[2]:
            buildp["properties"][6] = True
        else:
            buildp["properties"][6] = False

        if "custom" in kconf[2]:
            buildp["properties"][7] = True
        else:
            buildp["properties"][7] = False
        self.json_write(f"{info.info[14].basefs}/../var/build_prop.json", buildp)
        
        ksets = self.json_load(f"{info.info[14].basefs}/../var/kernel_sets.json")
        if "dynamic" in kconf[2]:
            ksets["dynamic_cmd"] = True
        else:
            ksets["dynamic_cmd"] = False
        self.json_write(f"{info.info[14].basefs}/../var/kernel_sets.json", ksets)
        
    def run(self, info, pyt):
        lang = self.json_load(f"{info.info[14].basefs}/../var/kernel_sets.json")["lang"]
        lang = self.json_load(f"{info.info[14].basefs}/../lang/global_{lang}.json")
        build_prop = self.json_load(f"{info.info[14].basefs}/../var/build_prop.json")
        

        kernel_conf = pytconf(
            title=lang["pytconf"]["conf"],
            text=lang["pytconf"]["conf_kernel"],
            ok_text = lang["pytconf"]["conf_button"],
            text2 = lang["pytconf"]["ktext"],
            values2 = [info.info[14].info["name"], info.info[14].info["version"]],
            values=[        ("debug", lang["pytconf"]["options"][0]),
                ("custom", lang["pytconf"]["options"][1]),
                ("dynamic", lang["pytconf"]["options"][2])
            ]
        ).run()
        if kernel_conf != None:
            result = yes_no_dialog(
            title=lang["pytconf"]["conf"],
            text=lang["pytconf"]["write"]).run()
            if result:
                self.write_pytconf(build_prop, kernel_conf, info)

        plm_conf = plmconf(
            title=lang["pytconf"]["plm_conf"],
            text= lang["pytconf"]["plm_graphics"],
            ok_text = lang["pytconf"]["conf_button"],
            values = [ ("invisible", lang["pytconf"]["options"][3])],
            values2 = [(0, lang["pytconf"]["graphics_options"][0]), (1, lang["pytconf"]["graphics_options"][1]), (2, lang["pytconf"]["graphics_options"][2])]
        ).run()
        if plm_conf != None:
            result = yes_no_dialog(
            title=lang["pytconf"]["plm_conf"],
            text=lang["pytconf"]["write"]).run()
            if result:
                self.write_plmconf(plm_conf, info)
