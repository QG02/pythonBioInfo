#Define a function to compare 2 DNA strands
def compare(seq1, seq2):
    # check length similarity
    if len(seq1) != len(seq2):
        print("Sequences are not of the same length!")
        return
    # add 1 to similarBases variable if the index character is the same in both strands
    similarBases = sum(1 for a,b in zip(seq1,seq2) if a == b)
    # find count of different bases by removeing the count of simialr bases from total amount
    diffBases = len(seq1) - similarBases
    # print results
    print(f"The sequences have {similarBases} bases in common and differ by {diffBases} bases.")

# ask user for inputs
firstSeq = input("What is the first strand of DNA? ").upper().strip()
secondSeq = input("What is the second strand of DNA? ").upper().strip()

#pass the inputs into the comparison function
compare(firstSeq, secondSeq)
