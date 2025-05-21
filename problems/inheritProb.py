from itertools import product

# Initialize probability and ask user for sample sizes
prob = 0.0
k = int(input("How many specimens have the homozygous dominant genotypes? "))
m = int(input("How many specimens have the heterozygous dominant genotypes? "))
n = int(input("How many specimens have the homozygous recessive genotypes? "))

# Dictionary to hold the genotypes
genotypes = {
    "AA": k,
    "Aa": m,
    "aa": n
}

# Dictionary to hold the dominance chances of each possible mating pair
dominantChance = {
    ("AA", "AA"): 1.00,
    ("AA", "Aa"): 1.00,
    ("AA", "aa"): 1.00,
    ("Aa", "AA"): 1.00,
    ("Aa", "Aa"): 0.75,
    ("Aa", "aa"): 0.50,
    ("aa", "AA"): 1.00,
    ("aa", "Aa"): 0.50,
    ("aa", "aa"): 0.00
}

# Function to find the dominance probability of the selected pair
def mateProb(firstMate, secondMate):
    # total genotypes
    total = sum(genotypes.values())
    # probability formula in case both mates are the same genotypes
    if firstMate == secondMate:
        return (genotypes[firstMate] / total) * ((genotypes[secondMate] - 1) / (total - 1))
    # probability formula for eveyr other case where the genotypes are not the same
    else:
        return (genotypes[firstMate] / total) * (genotypes[secondMate] / (total - 1))

# Loop for calculating the probability of all mates from the same sample after asking the user of sample sizes
for firstMate, secondMate in product(["AA", "Aa", "aa"], repeat=2):
    p_pair = mateProb(firstMate, secondMate)
    p_dom = dominantChance[(firstMate, secondMate)]
    prob += p_pair * p_dom

# Print results
print(f"Probability of dominant phenotype: {prob:.5f}")
