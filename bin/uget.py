import sys, json, os, importlib, requests
from colorama import Back, Fore, Style
from colorama import init as cinit
import argparse
from progress.bar import Bar
from progress.spinner import Spinner
sys.path.insert(0, "../types")
from binary import Binary
class UGet(Binary):
    def __init__(self):
        self.info = {
            "name" : "Download file from the Internet",
            "version" : "v1.1.1",
            "codename": "uget",
            "dependencies" : [], # Not Supported.
            "run": self.run,
            "on_load": self.load
        }

    def load(self, info):
        pass

    def run(self, info, pyt):
        args = info.info[15].split(" ")[1:]
        if len(args) < 2: return print("No URLs or file path provided.")
        print("Downloading file from " + args[0])
        url = args[0]
        path = args[1]
        r = requests.get(url, stream=True)
        if "content-length" in r.headers:
            size = r.headers["content-length"]
        else:
            size = False
        if size:
            p = Bar(f'{path}>', max=int(size), fill = "#", suffix='%(percent)d%%')
        else:
            p = Spinner(f'### {path}')
            
        with open(path, 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024*50):
                if chunk: # filter out keep-alive new chunks
                    p.next(len(chunk))
                    f.write(chunk)

        p.finish()
        print("\rFile downloaded")



