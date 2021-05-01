import os, sys, importlib, shutil, json

def dynamic_import(module):
    return importlib.import_module(module)

sys.path.insert(0, f"./types")


class SystemCTL:
    def json_load(self, file):
        with open(file, "r", encoding = "utf-8") as f:
            return json.load(f)
        
    def end(self):
        basedir = f"{self.info[14].basefs}/../etc/systemctl"
        sys.path.insert(0, basedir)
        for config in self.configure["on_end"]:
#            try:
                m = dynamic_import(config["file"])
                if config["function"] in vars(m):
                    vars(m)[config["function"]](self.info, self.info[14].basefs)
#            except:
#                pass
        sys.path.pop()
    
    def start(self, basedir, info):
        self.basedir = basedir
        self.info = info
        self.configure = self.configs(basedir)
        self.services = self.__init_on_load()

    def configs(self, basedir):
        configs = {"on_load": [], "on_end": []}
        configs_tmp = os.listdir(basedir)
        for file in configs_tmp:
            try:
                service = self.json_load(f"{basedir}/{file}")
                if "type" in service:
                    if service["type"] in configs:
                        configs[service["type"]].append(service)
            except:
                pass

        return configs
            
    def __init_on_load(self):
        basedir = f"{self.info[14].basefs}/../etc/systemctl"
        sys.path.insert(0, basedir)
        for config in self.configure["on_load"]:
#            try:
                m = dynamic_import(config["file"])
                if config["function"] in vars(m):
                    vars(m)[config["function"]](self.info, self.info[14].basefs)
#            except:
#                pass
        sys.path.pop()
