import sys, json, os, importlib
from colorama import Back, Fore, Style
from colorama import init as cinit
import argparse
import psutil
sys.path.insert(0, "../types")
cinit()
from binary import Binary
class free(Binary):
    def __init__(self):
        self.info = {
            "name" : "Get ram",
            "version" : "v1.1.0",
            "codename": "free",
            "dependencies" : [], # Not Supported.
            "run": self.run
        }

        self._standart_args = ["percent", "block"] # Use percent and blocky print.
        self.parser = {"-h": "human-read", "--human": "human-read",
                       "-p": "percent", "--percent": "percent",
                       "--block": "block",
                       "-b": "bytes", "--bytes": "bytes",
                       "--si": "1000",
                       #"-s": "RETURN::NUM::seconds", "--seconds": "RETURN::NUM::seconds"
                       #"-c":"RETURN::NUM::count", "--count": "RETURN::NUM::count",
                       }
        # Arguments:
        # -h, --human: Human-readable
        # -p, --percent: Print in percents
        # --block: Print in blocks type,
        # -b, --bytes: Print in bytes,
        # --si: Print all in power of 1000 instead of power of 1024,
        # -s, --seconds: Print continuosly result with delay seconds apart.
        # -c, --count: Display the result count times. Requires -s option.
        
        
    def parse_args(self, args):
        return self._standart_args

    def count_percent(self, percent, all):
        return round(100/(all/percent)) 
    def get_progress(self, percent):
        blocks = round(percent / 10)
        not_busy_blocks = 10-blocks
        progress = (blocks * "█" * 10) + (not_busy_blocks * "░" *10)
        return progress, str(percent) + "%"

    def json_load(self, file):
        with open(file, "r") as f:
            return json.load(f)

    def run(self, info, pyt):
        lang = self.json_load(f"{info.info[14].basefs}/../var/kernel_sets.json")["lang"]
        if os.path.isfile(f"{info.info[14].basefs}/../lang/free_{lang}.json"):
            with open(f"{info.info[14].basefs}/../lang/free_{lang}.json", "r") as f:
                lang = json.load(f)
        else:
            lang = {
                    "vram": "vRAM:"
                }
        args = info.info[15].split(" ")[1:]
        if len(args) > 0:
            self.parse_args(args)
        else:
            args = self._standart_args

        # Get PSUtil vmem
        mem = psutil.virtual_memory()
        # Get all RAM
        all_ram = mem.total
        # Get used RAM
        busy_ram = mem.used
        # Count and print.
        print(lang["vram"])
        percent = self.count_percent(busy_ram, all_ram)
        print(" ".join(self.get_progress(percent)))
        
