def make_table(key) :
    alpa = [chr(i) for i in range(ord('A'),ord('Z')+1)]
    alpa = [chr( i + ord('A')) for i in range(0,26)]
    tbl = {}
    for i in alpa :
        off = ord(i) - ord('A')
        off_enc = (off + key) % 26
        enc_char = chr(off_enc + ord('A'))
        tbl[i]=enc_char

    return tbl

table = make_table(2)

def caesar(word,tbl):
    
   #alpa = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    result = ""
    for i in word:
        result += tbl[i]
    return result

print(caesar('PYTHON',table))

