def first_double_peak(sequence):

    for i in range(len(sequence) - 1):
        if sequence[i - 2] < sequence[i] and sequence[i - 1] < sequence[i] and sequence[i + 2] < sequence[i] and sequence[i + 1] < sequence[i]:
            return i
        
    return -1

print(first_double_peak([1.2, 2.4, 3.1, 2.9, 3.6, 2.3, 1.9, 2.4]))