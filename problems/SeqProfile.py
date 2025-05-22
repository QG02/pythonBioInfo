def seqProcess(sequences):

    # Check if every sequence has the same length as the first one (index 0)
    if not all(len(seq) == len(sequences[0]) for seq in sequences):
        print("All sequences must be the same length.")
        return

    # Obtain the length of the first sequence
    length = len(sequences[0])

    # A dictionary that creates columns
    # depending on the length of the first sequence
    # with a zero as an initial placeholder
    # i.e. If length = 5 --> 'A' : [0,0,0,0,0]
    profile = {
        'A': [0] * length,
        'C': [0] * length,
        'G': [0] * length,
        'T': [0] * length
    }

    # List of the 4 possible bases
    valid_bases = {'A', 'C', 'T', 'G'}

    # This loops over each DNA sequence
    for seq in sequences:

        # Check if the sequences contain any bases that are not in the valid_bases list
        if any(base not in valid_bases for base in seq):
            print(f"Invalid sequence found: {seq}")
            return

        # Loops over each sequence and matches the base to its index column in the profile matrix
        for i, base in enumerate(seq):
            profile[base][i] += 1

    # Prints out the final matrix
    for base in "ACGT":
        # Turns the count ints to strings to print with space in between
        counts = " ".join(map(str, profile[base]))
        print(f"{base}: {counts}")

    # Build consensus sequence
    consensus = ""

    # Loop through every line to finds which base occurs
    # most frequently at position i across all sequences
    for i in range(length):
        max_base = max("ACGT", key = lambda b: profile[b][i])
        consensus += max_base

    print(f"Consensus: {consensus}")

# Ask user for sequence inputs
sequences = input('Enter 10 sequences separated by spaces: ').split()

# Checks if input is valid and start the function
if len(sequences) == 10:
    seqProcess(sequences)
else:
    print("please enter exactly 10 sequences.")
