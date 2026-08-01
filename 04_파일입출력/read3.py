from pathlib import Path
file_path = Path(__file__).parent / "강지호.txt"
f=open(file_path,"r",encoding="utf-8")
print(file_path)
print(__file__)
for i in f :
    print(i,end="")
f.close()


