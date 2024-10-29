def read_input():
    # Read the hidden path
    path = input().strip()

    # Skip the separator line
    input()

    # Read states
    states = input().strip().split()

    # Skip the separator line
    input()

    # Skip the header line with state labels
    header = input().strip().split()

    # Read transition matrix
    transition_matrix = {}
    for i in range(len(states)):
        row = input().strip().split()
        state = row[0]
        probabilities = {states[j]: float(row[j+1]) for j in range(len(states))}
        transition_matrix[state] = probabilities

    return path, states, transition_matrix

def calculate_path_probability(path, states, transition_matrix):
    # Initialize probability with 1/|states| for the first state
    probability = 1.0 / len(states)

    # Multiply by transition probabilities for each subsequent state
    for i in range(len(path) - 1):
        current_state = path[i]
        next_state = path[i + 1]
        probability *= transition_matrix[current_state][next_state]

    return probability

def main():
    # Read input
    path, states, transition_matrix = read_input()

    # Calculate probability
    result = calculate_path_probability(path, states, transition_matrix)

    # Print result
    print(result)

if __name__ == "__main__":
    main()