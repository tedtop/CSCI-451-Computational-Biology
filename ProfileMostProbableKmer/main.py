import sys

# Please do not remove package declarations because these are used by the autograder.

# Insert your profile_most_probable_kmer function here, along with any subroutines you need.

def profile_most_probable_kmer(text: str, k: int, profile: list[dict[str, float]]) -> str:
    """Identifies the most probable k-mer according to a given profile matrix.

    The profile matrix is represented as a list of columns, where the i-th element is a map
    whose keys are strings ("A", "C", "G", and "T") and whose values represent the probability
    associated with this symbol in the i-th column of the profile matrix.
    """
    kmers_and_probs = dict()
    for i in range(len(text) - k + 1):
        kmer = text[i:i+k]
        kmer_probability = 1

        for j in range(len(kmer)):
            nucleotide = kmer[j]
            nucleotide_probability = profile[j][nucleotide]
            # print(nucleotide, nucleotide_probability)
            kmer_probability = kmer_probability * nucleotide_probability
        # print(kmer, kmer_probability)
        kmers_and_probs[kmer] = kmer_probability # make a map of all k-mer windows and their probabilities

    # find the key with the highest value
    most_probable_kmer = max(kmers_and_probs, key=kmers_and_probs.get)
    return most_probable_kmer


def main():
    profile = [{"A": 0.2, "C": 0.4, "G": 0.3, "T": 0.1},
               {"A": 0.2, "C": 0.3, "G": 0.3, "T": 0.2},
               {"A": 0.3, "C": 0.1, "G": 0.5, "T": 0.1},
               {"A": 0.2, "C": 0.5, "G": 0.2, "T": 0.1},
               {"A": 0.3, "C": 0.1, "G": 0.4, "T": 0.2}]
    text = 'ACCTGTTTATTGCCTAAGTTCCGAACAAACCCAATATAGCCCGAGGGCCT'
    k = 5
    print(profile_most_probable_kmer(text, k, profile))

if __name__ == "__main__":
    main()