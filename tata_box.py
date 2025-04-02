
import re
file = open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa','r')
name=[]
seq=[]
gene_seq=''
i=0
for line in file:
    #remove \n of the line
    line=line.strip()
    if line[0]=='>':
        #save sequence when new gene detected
        if gene_seq!='':
            seq.append(gene_seq)
        gene_seq=''
        gene=re.search(r'gene:([^ ]+)',line)
        gene_name=gene.group(1)
        name.append(gene_name)
    else:
        gene_seq = gene_seq+line
#save the last sequence
seq.append(gene_seq)
pattern=r'TATA[AT]A[AT]'
file2 = open('tata_genes.fa','w')
for sequence in seq:
    if re.search(pattern,sequence):
        file2.write('>'+name[i]+'\n')
        file2.write(sequence+'\n')
    i+=1
file.close()
file2.close()