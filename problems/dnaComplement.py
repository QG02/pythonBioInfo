#Get DNA sequence to be complemented
dnaSeq = input("Please enter the DNA sequence to be complemented: ")
#initialize empty complement string
dnaComp = ""

#Check the entered DNA sequence to construct complement
for base in dnaSeq:
    if base == 'A':
        dnaComp += 'T'
    elif base == 'T':
        dnaComp += 'A'
    elif base == 'C':
        dnaComp += 'G'
    elif base == 'G':
        dnaComp += 'C'
    else:
        dnaComp += '?'

#reverse constructed string and print final result
reversedDNA = ''.join(reversed(dnaComp))
print(reversedDNA)
