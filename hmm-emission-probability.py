def read_input():
    # Read the emitted string
    emission_string = input().strip()
    
    # Skip the separator line
    input()
    
    # Read alphabet
    alphabet = input().strip().split()
    
    # Skip the separator line
    input()
    
    # Read the hidden path
    hidden_path = input().strip()
    
    # Skip the separator line
    input()
    
    # Read states
    states = input().strip().split()
    
    # Skip the separator line
    input()
    
    # Skip the header line with emission labels
    header = input().strip().split()
    
    # Read emission matrix
    emission_matrix = {}
    for i in range(len(states)):
        row = input().strip().split()
        state = row[0]
        probabilities = {alphabet[j]: float(row[j+1]) for j in range(len(alphabet))}
        emission_matrix[state] = probabilities
    
    return emission_string, alphabet, hidden_path, states, emission_matrix

def calculate_emission_probability(emission_string, hidden_path, emission_matrix):
    # Initialize probability to 1
    probability = 1.0
    
    # For each position, multiply by the probability of emitting the symbol from the corresponding state
    for i in range(len(emission_string)):
        emitted_symbol = emission_string[i]
        state = hidden_path[i]
        probability *= emission_matrix[state][emitted_symbol]
    
    return probability

def main():
    # Read input
    emission_string, alphabet, hidden_path, states, emission_matrix = read_input()
    
    # Verify that the lengths match
    if len(emission_string) != len(hidden_path):
        raise ValueError("The emission string and hidden path must have the same length")
    
    # Calculate probability
    result = calculate_emission_probability(emission_string, hidden_path, emission_matrix)
    
    # Print result
    print(result)

if __name__ == "__main__":
    main()
