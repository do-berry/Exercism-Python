def distance(strand_a, strand_b):
    if len(strand_a) == len(strand_b):
        return sum(1 for i,j in zip(strand_a, strand_b) if i != j)
    else:
        raise ValueError("String are not the same length!")
