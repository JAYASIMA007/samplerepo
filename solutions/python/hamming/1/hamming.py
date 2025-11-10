def distance(strand1, strand2):
    if len(strand1) != len(strand2):
        raise ValueError("Strands must be of equal length.")

    diff = 0
    for i in range(len(strand1)):
        if strand1[i] != strand2[i]:
            diff = diff + 1

    return diff
