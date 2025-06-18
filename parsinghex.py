import re
import sys

for line in sys.stdin:

    match = re.findall(r"0[xX][a-fA-F0-9]{1,8}", line.rstrip())
    for m in match:
        print(f"{m} {int(m, 16)}")