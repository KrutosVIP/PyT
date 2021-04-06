class Module(object):
    def __init__(self):
        self.info = {
            "name" : "undefined",
            "version" : "undefined",
            "codename": "undefined",
            "dependencies" : [],
            "on_load" : self.on_load
        }
    
    def on_load(self, info):
        """
Info:
[
    #default kinfo 0-6
    modules 7
    binaries 8
    lines 9
        """
        pass
