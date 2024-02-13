import VarGlobal
from SequenceMatching import *

def brute(TotalRow, TotalCol):
    BufferMaxValToken = []  
    BufferMaxValCoordinate = []
    MaxVal = 0  

    def AppendToken(Matrix, Coordinate):
        
        idx_row = Coordinate[0]
        idx_col = Coordinate[1]
        Token = Matrix[idx_row][idx_col]
        VarGlobal.current_buffer_token.append(Token)
        VarGlobal.current_buffer_coordinate.append(Coordinate.copy())   
        
    def ResetCurrentBuffer():
        
        VarGlobal.current_buffer_token = []
        VarGlobal.current_buffer_coordinate = []
    
    def AppendBuffer(CurrentBufferToken, CurrentBufferCoordinate, BufferMaxCoordinate, BufferMaxToken, MaxValue):
        global n_sequence
        bufferValue = 0
        for i in range(0,VarGlobal.n_sequence):
            if (isSequenceMatch(CurrentBufferToken, VarGlobal.list_sequence[i])):
                bufferValue += VarGlobal.list_sequenceValue[i]
            
        if (MaxValue < bufferValue) or ((MaxValue == bufferValue) and (len(CurrentBufferCoordinate) < len(BufferMaxCoordinate))):
            NewMaxValue = bufferValue
            
            nBuffer = len(CurrentBufferToken)
            
            NewBufferMaxValToken = []
            for j in range(0,nBuffer):
                NewBufferMaxValToken.append(CurrentBufferToken[j])
                
            NewBufferMaxValCoordinate = []
            for j in range(0,nBuffer):
                NewBufferMaxValCoordinate.append(CurrentBufferCoordinate[j])

        else:
            NewMaxValue = MaxValue
            NewBufferMaxValToken = BufferMaxToken
            NewBufferMaxValCoordinate = BufferMaxCoordinate
                     
        return [NewBufferMaxValToken, NewBufferMaxValCoordinate, NewMaxValue]
        
    def UpdateOffsets():
        global offsets
        i = VarGlobal.buffer_size - 2
        while (VarGlobal.offsets[0] < TotalRow):
            VarGlobal.offsets[i] = (VarGlobal.offsets[i]+1)
            if (i%2 == 0):
                if (VarGlobal.offsets[i] >= TotalRow):
                    VarGlobal.offsets[i] = (VarGlobal.offsets[i]%TotalRow)+1
                    i-=1
                else:
                    break
            else:
                if (VarGlobal.offsets[i] >= TotalCol):
                    VarGlobal.offsets[i] = (VarGlobal.offsets[i]%TotalCol)+1
                    i-= 1
                else:
                    break
            
    def special_case():
        global row
        global col
        # case ketika VarGlobal.matriks hanya memiliki 1 atau 2 baris dan/atau kolom saja
        if len(VarGlobal.offsets) == 0 or VarGlobal.row <= 2 or VarGlobal.col <= 2:
            return True
        return False  
        
    for i in range(0,TotalCol):
        VarGlobal.offsets = []
        for j in range(0,VarGlobal.buffer_size-1):
            VarGlobal.offsets.append(1)
        while True:
            ResetCurrentBuffer()
            VarGlobal.current_coordinate = [0,i]
            AppendToken(VarGlobal.matriks,VarGlobal.current_coordinate)
            Result = AppendBuffer(VarGlobal.current_buffer_token, VarGlobal.current_buffer_coordinate, BufferMaxValCoordinate, BufferMaxValToken, MaxVal)
            BufferMaxValToken = Result[0]
            BufferMaxValCoordinate = Result[1]
            MaxVal = Result[2]
            
            for j in range(0,len(VarGlobal.offsets)):
                if (j%2 == 0):
                    VarGlobal.current_coordinate[0] = (VarGlobal.current_coordinate[0]+VarGlobal.offsets[j])%TotalRow
                else:
                    VarGlobal.current_coordinate[1] = (VarGlobal.current_coordinate[1]+VarGlobal.offsets[j])%TotalCol
                
                if VarGlobal.current_coordinate not in VarGlobal.current_buffer_coordinate: 
                    AppendToken(VarGlobal.matriks, VarGlobal.current_coordinate)  
                    Result = AppendBuffer(VarGlobal.current_buffer_token, VarGlobal.current_buffer_coordinate, BufferMaxValCoordinate, BufferMaxValToken, MaxVal)
                    BufferMaxValToken = Result[0]
                    BufferMaxValCoordinate = Result[1]
                    MaxVal = Result[2]
                else:
                    break
                    
            if (VarGlobal.offsets == VarGlobal.max_offsets) or special_case():
                break
            else:
                UpdateOffsets()
    
    VarGlobal.MAX_VALUE = MaxVal
    VarGlobal.BUFFER_MAX_VALUE_TOKEN = BufferMaxValToken
    VarGlobal.BUFFER_MAX_VALUE_COORDINATE = BufferMaxValCoordinate        