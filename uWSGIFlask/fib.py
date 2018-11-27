def getfib(number):
    print(number)
    sequence = [0, 1]
    while sequence[-1] < number:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence
