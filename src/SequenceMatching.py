def isSequenceMatch(Buffer, Sequence):
    if len(Buffer) < len(Sequence):
        return False
    def isSequenceFound(Buffer,Sequence):
        n = len(Sequence)
        for i in range(0,n):
            if (Sequence[i] != Buffer[i]):
                return False
        return True
    
    n = len(Buffer) - len(Sequence) + 1
    for i in range(0,n):
        if (Buffer[i] == Sequence[0]):
            if isSequenceFound(Buffer[i:],Sequence):
                return True
    return False