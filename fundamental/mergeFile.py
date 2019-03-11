import glob2
from datetime import datetime

info = glob2.glob("*.txt")
with open(datetime.now().strftime("%Y-%m-%d-%H-%M-%S-%f")+".txt", "w") as info2:
    for x in info:
        with open(x, "r") as f:
            info2.write(f.read() + "\n")

 