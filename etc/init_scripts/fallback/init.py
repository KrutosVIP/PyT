import os
def init(kernel, data):
    os.chdir("./kernel")

    kernel = kernel(data["properties"])
    kernel.startup()
