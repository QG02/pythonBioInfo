# Get DNA sequence from user
DNAseq = input("Please enter the DNA sequence:\n")

#initialize variables
aBase = 0
tBase = 0
gBase = 0
cBase = 0

# condition for inputs
valid_bases = {'A','C','T','G'}

# read the sequence for base coutns
if any(base not in valid_bases for base in DNAseq):
    print("Please enter a valid DNA sequence: ")
else:
    aBase = DNAseq.count('A')
    tBase = DNAseq.count('T')
    cBase = DNAseq.count('C')
    gBase = DNAseq.count('G')

# total base count and calculating CG content percentage
totalBases = aBase + tBase + cBase + gBase
cgContent = ((cBase + gBase)/totalBases)*100

#print results
print(f"""
A = {aBase}
T = {tBase}
C = {cBase}
G = {gBase}
Total Bases = {totalBases}
The CG content is {round(cgContent,2)}%
""")
