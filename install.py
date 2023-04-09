import os
from get_path import vpath

print("Start Install...")
print("Check if Vemo already installed...")
with open(".installed","r") as f:
    content = f.readline()
    if content[0] == "1":
        print('\033[1;91m'+"ERROR: Vemo is already installed"+'\033[m')
        exit()
print("Get the absulute path of vemo.py...")


#add alias to bashrc
print("Make command valid...")
os.system(f"echo 'alias vemo=\"python {vpath}\"' >>  ~/.bashrc")

with open('.installed','w') as f:
    f.write("1")

print("Install successful!")
