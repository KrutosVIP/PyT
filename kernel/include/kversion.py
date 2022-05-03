# Define version
import os

PYT_KAPI = 0
PYT_KMAJOR = 0
PYT_KMINOR = 0
PYT_KMICRO = 1
PYT_KRELEASE = "DEBUG"
PYT_KLOCALVERSION = "-test"

# Also, all here in strings because environ.
os.environ["__PYT_KAPI"] = str(PYT_KAPI) # Define Kernel API
os.environ["__PYT_KERNEL_MAJOR"] = str(PYT_KMAJOR) # Kernel major version
os.environ["__PYT_KERNEL_MINOR"] = str(PYT_KMINOR) # Kernel minor version
os.environ["__PYT_KERNEL_MICRO"] = str(PYT_KMICRO) # Kernel micro version
os.environ["__PYT_KERNEL_RELEASE"] = str(PYT_KRELEASE) # Kernel release type

# Predefine class
class KVersion:
    api = PYT_KAPI
    major = PYT_KMAJOR
    minor = PYT_KMINOR
    micro = PYT_KMICRO
    release = PYT_KRELEASE

    full = f"{PYT_KMAJOR}.{PYT_KMINOR}.{PYT_KMICRO}{PYT_KLOCALVERSION}"

    # Check if debug
    def is_debug():
        if PYT_KRELEASE in ["DEBUG"]:
            return True
        return False

    # Is release in good type
    def is_ok():
        if PYT_KRELEASE in ["DEBUG", "RELEASE"]:
            return True
        return False
