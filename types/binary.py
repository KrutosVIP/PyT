class Binary(object):
    def __init__(self):
        self.info = {
            "name" : "undefined",
            "version" : "undefined",
            "codename": "undefined",
            "dependencies" : [],
            "run": self.run,
            "on_load": self.on_load
        }
    
    def on_load(self, info):
        pass

    def run(self, info, pyt):
        pass
