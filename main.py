import time
import os
import sys
from pathlib import Path
os.system("cls")

print("sys: booting as callboot")
time.sleep(2)
os.system("cls")

sys.path.append(str(Path(__file__).parent / "resources" / "Functions" / "Errors"))
import booterror