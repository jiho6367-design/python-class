def caesar(word,key):
   #alpa = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    result = ""
    for i in word:
        off = ord(i)-ord('A')
        off_enc= (off + key) % 26
        enc = chr(ord('A') + off_enc) 
        result += enc
    return result

print(caesar('PYTHON',3))

