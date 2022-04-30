# Init make
# ! --- DO NOT CALL THIS FILE IN YOUR MAKE FILES --- !
import sys, pathlib, os
os.chdir(pathlib.Path(__file__).parent.parent.resolve())

sys.path.append(str(pathlib.Path("./maketools").resolve()))

