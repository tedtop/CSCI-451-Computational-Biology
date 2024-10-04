import sys

# Please do not remove package declarations because these are used by the autograder.

# Insert your pattern_matching function here, along with any subroutines you need
def pattern_matching(pattern: str, genome: str) -> list[int]:
    """Find all occurrences of a pattern in a genome."""
    locations = list()
    for i in range(len(genome) - len(pattern) + 1):
        if genome[i:i + len(pattern)] == pattern:
            locations.append(i)
    return locations


def main():
    filename = "../Vibrio_cholerae.txt"
    try:
        with open(filename, 'r') as file:
            genome = file.read()
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")

    print(*pattern_matching("CTTGATCAT", genome))

if __name__ == "__main__":
    main()