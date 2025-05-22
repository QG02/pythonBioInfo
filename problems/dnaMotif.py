def motif(seq, subSeq):

    # Initializes empty list to hold location ints
    locations = []

    # Loops through the indices
    # in the range of the original length subtracted
    # from the length of the sub_sequence
    # so the search never goes out of bounds
    for i in range(len(seq) - len(subSeq) + 1):
        # If the subsequence is found in the range
        # of the search index to the length of sub-sequence
        # it adds the index to the location list
        if seq[i:i+len(subSeq)] == subSeq:
            locations.append(i + 1)
    # Converts the location ints to string to be printed with spaces in between
    print(" ".join(map(str, locations)))

# Ask user for inputs
string = input("What is the original sequence? ").upper().strip()
subString = input("What is the motif you are trying to locate? ").upper().strip()
# Pass inputs into function
motif(string,subString)
