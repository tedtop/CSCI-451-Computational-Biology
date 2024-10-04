import sys
import argparse

# Please do not remove package declarations because these are used by the autograder.

# Insert your frequent_words function here, along with any subroutines you need
def frequent_words(text: str, k: int) -> list[str]:
    """Find the most frequent k-mers in a given text."""
    frequentPatterns = []
    freqMap = FrequencyTable(text, k)
    max = MaxMap(freqMap)
    for key in freqMap:
        if freqMap[key] == max:
            frequentPatterns.append(key)
    return frequentPatterns

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

def MaxMap(freqMap: dict[str, int]) -> int:
    """Find the maximum value in a frequency map."""
    maxCount = 0
    for key in freqMap:
        if freqMap[key] > maxCount:
            maxCount = freqMap[key]
    return maxCount

def main(file_path: str):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        text = lines[0].strip()
        k = int(lines[1].strip())  # Convert the second line to an integer

    # Call the frequent_words function
    print (frequent_words(text, k))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Find the most frequent k-mers in a given text.')
    parser.add_argument('file_path', type=str, help='Path to the input file')

    args = parser.parse_args()

    main(args.file_path)