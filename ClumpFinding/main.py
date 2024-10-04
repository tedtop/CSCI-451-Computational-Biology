import sys

# Please do not remove package declarations because these are used by the autograder.

"""
FindClumps(Text, k, L, t)
    Patterns ← an array of strings of length 0
    n ← |Text|
    for every integer i between 0 and n − L
        Window ← Text(i, L)
        freqMap ← FrequencyTable(Window, k)
        for every key s in freqMap
            if freqMap[s] ≥ t
                append s to Patterns
    remove duplicates from Patterns
    return Patterns
"""

# Insert your find_clumps function here, along with any subroutines you need
def find_clumps(genome: str, k: int, l: int, t: int) -> list[str]:
    """Find patterns forming clumps in a genome."""
    patterns = []
    n = len(genome)
    for i in range(n - l + 1):
        window = genome[i:i + l]
        freqMap = FrequencyTable(window, k)
        for s in freqMap:
            if freqMap[s] >= t:
                patterns.append(s)
    patterns = list(set(patterns))
    return patterns

def FrequencyTable(text: str, k: int) -> dict[str, int]:
    """Generate a frequency table of k-mers in a given text."""
    freqMap = {}
    n = len(text)
    k = int(k)
    for i in range(n - k + 1):
        pattern = text[i:i + k]
        if pattern in freqMap:
            freqMap[pattern] += 1
        else:
            freqMap[pattern] = 1
    return freqMap

def main():
    # # Check if the correct number of arguments are provided
    # if len(sys.argv) != 2:
    #     print("Usage: python script.py <file_path>")
    #     sys.exit(1)

    # # Get the file path from the command line argument
    # file_path = sys.argv[1]

    # Initialize variables
    genome = None
    k = l = t = None

    # # Read the file
    # with open(file_path, 'r') as file:
    #     # Read the genome from the first line
    #     genome = file.readline().strip()

    #     # Read the second line and split it into integers
    #     k, l, t = map(int, file.readline().strip().split())

    ## For E. coli
    with open('../E_coli.txt', 'r') as file:
        genome = file.readline().strip()
    k, l, t = 9, 500, 3

    # Call the function with the parameters
    print(*find_clumps(genome, k, l, t))

if __name__ == "__main__":
    main()