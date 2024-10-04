def min_skew(genome):
    skew = [0]
    min_skew_positions = []

    for nucleotide in genome:
        if nucleotide == 'G':
            skew.append(skew[-1] + 1)
        elif nucleotide == 'C':
            skew.append(skew[-1] - 1)
        else:
            skew.append(skew[-1])

    min_value = min(skew)

    for i, value in enumerate(skew):
        if value == min_value:
            min_skew_positions.append(i)

    return min_skew_positions