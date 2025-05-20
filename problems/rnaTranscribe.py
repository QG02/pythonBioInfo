#Get DNA sequence from user
DNAseq = input("Please enter the DNA chain to be transcribed: ")

#initialize empty RNA string
RNAseq = str("")

#loop through every character to construct the RNA string
for base in DNAseq:
    if base == 'A':
        RNAseq += 'U'
    elif base == 'T':
        RNAseq+= 'A'
    elif base == 'C':
        RNAseq += 'G'
    elif base == 'G':
        RNAseq += 'C'
    else:
        RNAseq += '?'

#print results
print(f"""Transcribed sequence: {RNAseq}""")
