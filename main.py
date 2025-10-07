import time
import os
import sys
from pathlib import Path
from getpass import getpass
os.system("cls")

rpw = "Korinth"

print("sys: booting as callboot")
time.sleep(2)

pw = getpass("Password:")

if rpw == pw:
    print("Logged In As Allable User")
    time.sleep(1)
    sys.path.append(str(Path(__file__).parent / "resources" / "Functions" / "bootup"))
    import boot
else:    
    import wrongpw