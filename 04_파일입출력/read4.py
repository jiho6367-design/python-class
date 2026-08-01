from pathlib import Path
import os
print("before : ",Path.cwd())

file_dir = Path(__file__).parent
os.chdir(file_dir)
print("After : ",Path.cwd())
f=open("새파일.txt","r",encoding="utf-8")
for i in f :
    print(i,end="")
f.close()


