seq = 'ATGCAAGTGGTGTGTCTGTTCTGAGAGGGCCTAA'
#from forward to back
for i in range(len(seq)-2):
    if seq[i:i+2]=='GT':
        GT=i
        break
    else:
        GT=-1
#from back to forward
for j in range(len(seq)-2,0,-1):
    if seq[j:j+2]=='AG':
        AG=j
        break
    else:
        AG=-1
len = AG-GT+2
if len>2:
    print("Length is:",len)
else:
    print('None')
