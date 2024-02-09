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
        # print("AAAAAAAA", Coordinate)
        # print("BBBBBBBB", VarGlobal.current_buffer_coordinate)    
        
    def ResetCurrentBuffer():
        
        VarGlobal.current_buffer_token = []
        VarGlobal.current_buffer_coordinate = []
    
    def AppendBuffer(CurrentBufferToken, CurrentBufferCoordinate, BufferMaxCoordinate, BufferMaxToken, MaxValue):
        # global list_buffer_coordinate
        # global list_buffer_token
        # global list_bufferValue
        global n_sequence
    
        # list_buffer_token.append(VarGlobal.current_buffer_token)
        # list_buffer_coordinate.append(CurrentBufferCoordinate)
        bufferValue = 0

        # print("HOOOOOOOO",VarGlobal.current_buffer_token)
        # print("HOOOOOOOO",SelectedCoordinate)
        # print(list_sequence)
        # print(VarGlobal.list_sequenceValue)
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
        # list_bufferValue.append(bufferValue)
        
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
        # print("LESSGO", i)
        while True:
            # print("HUWALAAAAAAAAAA",VarGlobal.offsets)
            # print(list_buffer_token)
            # print(list_bufferValue)
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
                    # counter = 0
                    # while (VarGlobal.current_coordinate in VarGlobal.current_buffer_coordinate) and (counter < TotalRow):
                    #     VarGlobal.current_coordinate[0] = (VarGlobal.current_coordinate[0]+1)%TotalRow
                    #     counter += 1
                    # print("VERT", VarGlobal.current_coordinate)
                    # print(VarGlobal.current_buffer_token)
                else:
                    VarGlobal.current_coordinate[1] = (VarGlobal.current_coordinate[1]+VarGlobal.offsets[j])%TotalCol
                    # counter = 0
                    # while (VarGlobal.current_coordinate in VarGlobal.current_buffer_coordinate) and (counter < TotalCol):
                    #     VarGlobal.current_coordinate[1] = (VarGlobal.current_coordinate[1]+1)%TotalCol
                    #     counter += 1
                    # print("HORZ", VarGlobal.current_coordinate)
                    # print(VarGlobal.current_buffer_token) 
                
                if VarGlobal.current_coordinate not in VarGlobal.current_buffer_coordinate: 
                    AppendToken(VarGlobal.matriks, VarGlobal.current_coordinate)  
                    Result = AppendBuffer(VarGlobal.current_buffer_token, VarGlobal.current_buffer_coordinate, BufferMaxValCoordinate, BufferMaxValToken, MaxVal)
                    BufferMaxValToken = Result[0]
                    BufferMaxValCoordinate = Result[1]
                    MaxVal = Result[2]
                else:
                    break
                    
            # AppendBuffer(VarGlobal.current_buffer_token, VarGlobal.current_buffer_coordinate, BUFFER_MAX_VALUE_COORDINATE)
                
            # AppendBuffer(VarGlobal.current_buffer_coordinate, BUFFER_MAX_VALUE_COORDINATE)
            # if VarGlobal.offsets == [3,2,1,3,5,5]:
            #     print("VarGlobal.offsets",VarGlobal.offsets)
            #     print(VarGlobal.current_buffer_token)
            #     print("LEN",len(list_buffer_token))
            #     print(VarGlobal.current_buffer_coordinate)
            
            # print(VarGlobal.current_buffer_coordinate)
            # if VarGlobal.offsets == [3,2,1,3,5,5]:
            #     print(list_bufferValue)
            #     print(list_bufferValue[6949])
            #     exit()
            # print("AAAAAAA", VarGlobal.offsets)
            # print("BBBBBBB", max_VarGlobal.offsets)
            if (VarGlobal.offsets == VarGlobal.max_offsets) or special_case():
                break
            else:
                UpdateOffsets()
    
    VarGlobal.MAX_VALUE = MaxVal
    VarGlobal.BUFFER_MAX_VALUE_TOKEN = BufferMaxValToken
    VarGlobal.BUFFER_MAX_VALUE_COORDINATE = BufferMaxValCoordinate        