import VarGlobal

def initOffsets():
    # initialize offsets
    VarGlobal.offsets = []
    for i in range(0,VarGlobal.buffer_size-1):
        VarGlobal.offsets.append(1)

    # initialize max_offsets
    VarGlobal.max_offsets = []
    for i in range(0,VarGlobal.buffer_size-1):
        if(i%2==0):
            VarGlobal.max_offsets.append(VarGlobal.row-1)
        else:
            VarGlobal.max_offsets.append(VarGlobal.col-1)