from pathlib import Path
import os
file_dir = Path(__file__).parent
os.chdir(file_dir)

with open("강지호.txt","r",encoding="utf-8") as f :
    for i in f :
        print(i,end="")
print(f.closed)

