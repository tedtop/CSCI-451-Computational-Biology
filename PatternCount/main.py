import sys
import argparse

# Please do not remove package declarations because these are used by the autograder.

# Insert your PatternCount function here, along with any subroutines you need
def pattern_count(text: str, pattern: str) -> int:
    count = 0
    for i in range(len(text) - len(pattern) + 1):
        if text[i:i + len(pattern)] == pattern:
            count += 1
    return count

def main(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

        # Extract the first and second lines
        text = lines[0].strip()
        pattern = lines[1].strip()

        # Call the pattern_count function
        result = pattern_count(text, pattern)

        print(f"Pattern '{pattern}' occurs {result} times in the text.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Count occurrences of a pattern in a text.')
    parser.add_argument('file_path', type=str, help='Path to the input file')

    args = parser.parse_args()

    main(args.file_path)