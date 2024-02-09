import time
import random

matriks = []

# max value
MAX_VALUE = 0
BUFFER_MAX_VALUE_TOKEN = []
BUFFER_MAX_VALUE_COORDINATE = []

# sequence
list_sequence = []
list_sequenceValue = []

# buffer
buffer_size = 7

# current processing
current_buffer_token = []
current_buffer_coordinate = []
current_coordinate = []

# offset
offsets = []
max_offsets = []

# sequence matching

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
    
# brute
def brute(TotalRow, TotalCol):
    
    BufferMaxValToken = []  
    BufferMaxValCoordinate = []
    MaxVal = 0  
    global offsets
    # global list_buffer_coordinate
    # global list_buffer_token
    # global list_bufferValue
    global current_buffer_token
    global current_buffer_coordinate
    global current_coordinate
    global MAX_VALUE
    global BUFFER_MAX_VALUE_TOKEN
    global BUFFER_MAX_VALUE_COORDINATE
  
    def AppendToken(Matrix, Coordinate):
        global current_buffer_token
        global current_buffer_coordinate
        
        idx_row = Coordinate[0]
        idx_col = Coordinate[1]
        Token = Matrix[idx_row][idx_col]
        current_buffer_token.append(Token)
        current_buffer_coordinate.append(Coordinate.copy())
        # print("AAAAAAAA", Coordinate)
        # print("BBBBBBBB", current_buffer_coordinate)    
        
    def ResetCurrentBuffer():
        global current_buffer_token
        global current_buffer_coordinate
        
        current_buffer_token = []
        current_buffer_coordinate = []
    
    def AppendBuffer(CurrentBufferToken, CurrentBufferCoordinate, BufferMaxCoordinate, BufferMaxToken, MaxValue):
        # global list_buffer_coordinate
        # global list_buffer_token
        # global list_bufferValue
        global n_sequence
    
        # list_buffer_token.append(current_buffer_token)
        # list_buffer_coordinate.append(CurrentBufferCoordinate)
        bufferValue = 0

        # print("HOOOOOOOO",current_buffer_token)
        # print("HOOOOOOOO",SelectedCoordinate)
        # print(list_sequence)
        # print(list_sequenceValue)
        for i in range(0,n_sequence):
            if (isSequenceMatch(CurrentBufferToken,list_sequence[i])):
                bufferValue += list_sequenceValue[i]
            
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
        i = buffer_size - 2
        while (offsets[0] < TotalRow):
            offsets[i] = (offsets[i]+1)
            if (i%2 == 0):
                if (offsets[i] >= TotalRow):
                    offsets[i] = (offsets[i]%TotalRow)+1
                    i-=1
                else:
                    break
            else:
                if (offsets[i] >= TotalCol):
                    offsets[i] = (offsets[i]%TotalCol)+1
                    i-= 1
                else:
                    break
            
    def special_case():
        global row
        global col
        # case ketika matriks hanya memiliki 1 atau 2 baris dan/atau kolom saja
        if len(offsets) == 0 or row <= 2 or col <= 2:
            return True
        return False  
        
    for i in range(0,TotalCol):
        offsets = []
        for j in range(0,buffer_size-1):
            offsets.append(1)
        # print("LESSGO", i)
        while True:
            # print("HUWALAAAAAAAAAA",offsets)
            # print(list_buffer_token)
            # print(list_bufferValue)
            ResetCurrentBuffer()
            current_coordinate = [0,i]
            AppendToken(matriks,current_coordinate)
            Result = AppendBuffer(current_buffer_token, current_buffer_coordinate, BufferMaxValCoordinate, BufferMaxValToken, MaxVal)
            BufferMaxValToken = Result[0]
            BufferMaxValCoordinate = Result[1]
            MaxVal = Result[2]
            
            for j in range(0,len(offsets)):
                if (j%2 == 0):
                    current_coordinate[0] = (current_coordinate[0]+offsets[j])%TotalRow
                    # counter = 0
                    # while (current_coordinate in current_buffer_coordinate) and (counter < TotalRow):
                    #     current_coordinate[0] = (current_coordinate[0]+1)%TotalRow
                    #     counter += 1
                    # print("VERT", current_coordinate)
                    # print(current_buffer_token)
                else:
                    current_coordinate[1] = (current_coordinate[1]+offsets[j])%TotalCol
                    # counter = 0
                    # while (current_coordinate in current_buffer_coordinate) and (counter < TotalCol):
                    #     current_coordinate[1] = (current_coordinate[1]+1)%TotalCol
                    #     counter += 1
                    # print("HORZ", current_coordinate)
                    # print(current_buffer_token) 
                
                if current_coordinate not in current_buffer_coordinate: 
                    AppendToken(matriks, current_coordinate)  
                    Result = AppendBuffer(current_buffer_token, current_buffer_coordinate, BufferMaxValCoordinate, BufferMaxValToken, MaxVal)
                    BufferMaxValToken = Result[0]
                    BufferMaxValCoordinate = Result[1]
                    MaxVal = Result[2]
                else:
                    break
                    
            # AppendBuffer(current_buffer_token, current_buffer_coordinate, BUFFER_MAX_VALUE_COORDINATE)
                
            # AppendBuffer(current_buffer_coordinate, BUFFER_MAX_VALUE_COORDINATE)
            # if offsets == [3,2,1,3,5,5]:
            #     print("OFFSETS",offsets)
            #     print(current_buffer_token)
            #     print("LEN",len(list_buffer_token))
            #     print(current_buffer_coordinate)
            
            # print(current_buffer_coordinate)
            # if offsets == [3,2,1,3,5,5]:
            #     print(list_bufferValue)
            #     print(list_bufferValue[6949])
            #     exit()
            # print("AAAAAAA", offsets)
            # print("BBBBBBB", max_offsets)
            if (offsets == max_offsets) or special_case():
                break
            else:
                UpdateOffsets()
    
    MAX_VALUE = MaxVal
    BUFFER_MAX_VALUE_TOKEN = BufferMaxValToken
    BUFFER_MAX_VALUE_COORDINATE = BufferMaxValCoordinate        
# matriks = []

# # max value
# MAX_VALUE = 0
# BUFFER_MAX_VALUE_TOKEN = []
# BUFFER_MAX_VALUE_COORDINATE = []

# # sequence
# list_sequence = []
# list_sequenceValue = []

# # buffer
# buffer_size = 7

# # current processing
# current_buffer_token = []
# current_buffer_coordinate = []
# current_coordinate = []

# # offset
# offsets = []
# max_offsets = []
            
# MAIN PROGRAM         
print("\033[1;34;40m___  ____ _  _ ___ ____ ____ ____ ____ ____ ____")
print("|__] |__/ |  |  |  |___ |___ |  | |__/ |    |___")
print("|__] |  \ |__|  |  |___ |    |__| |  \ |___ |___") 
print("------------------------------------------------")      
print("\033[1;33;40m")

print("\033[0;33;40mInput Type:")
print("1. Text file (.txt)")
print("2. Manual input (CLI)")

while True:
    try:
        input_type = int(input(">>>\033[1;33;40m "))
    except:
        print("\033[0;31;40mInvalid Type Input\033[0;33;40m")
    else:
        if (input_type == 1) or (input_type == 2):
            break
        else:
            print("\033[0;31;40mInvalid Input\033[0;33;40m")
    
if (input_type == 1):
    pass
else:
    print("\n\033[1;33;40mPlease Complete Below Requirements")
    print("----------------------------------\033[0;33;40m")         

    # jumlah token unik
    while True:
        try:
            n_token_unik = int(input("Jumlah Token Unik : \033[1;33;40m"))
        except:
            print("\033[0;31;40mInvalid Type Input\033[0;33;40m")
        else:
            break
    
    # token unik    
    while True:
        try:
            tokens = input("\033[0;33;40mToken (XX YY ... ZZ) (case insensitive): \033[1;33;40m").upper()
        except:
            print("\033[0;31;40mInvalid Type Input\033[0;33;40m")
        else:
            tokens = tokens.split(" ")
            tokens = list(dict.fromkeys(tokens))
            if (len(tokens) != n_token_unik):
                # invalid
                print("\033[0;31;40mJumlah token unik harus sesuai dengan jumlah token yang telah dimasukkan di atas\033[0;33;40m")
                
            else:
                # loop cek
                valid = True
                for i in range(0,n_token_unik):
                    if (len(tokens[i]) != 2):
                        print("\033[0;31;40mToken harus terdiri dari 2 karakter alfanumerik\033[0;33;40m")
                        valid = False
                        break  
                if valid:
                    break
            
    
    # buffer size
    while True:
        try:
            buffer_size = int(input("\033[0;33;40mBuffer size : \033[1;33;40m"))
        except:
            print("\033[0;31;40mInvalid Type Input\033[0;33;40m")
        else:
            if buffer_size > 0:
                break
            else:
                print("\033[0;31;40mUkuran Buffer harus bernilai positif\033[0;33;40m")
            
    # matriks size
    while True:
        try:
            col, row = [ int(x) for x in input("\033[0;33;40mMatriks size (col row) : \033[1;33;40m").split(" ")]
        except:
            print("\033[0;31;40mInvalid Type Input\033[0;33;40m")
        else:
            if row <= 0:
                print("\033[0;31;40mUkuran baris pada matriks harus bernilai positif\033[0;33;40m")
            if col <= 0:
                print("\033[0;31;40mUkuran kolom pada matriks harus bernilai positif\033[0;33;40m")
            if row > 0 and col > 0:
                matriks = [[(tokens[int(random.randrange(0,n_token_unik))]) for j in range(0,col)] for i in range(0,row)]
                break
    
    # ukuran maks sequence     
    while True:
        try:
            max_sequence_size = int(input("\033[0;33;40mMax sequence size : \033[1;33;40m"))
        except:
            print("\033[0;31;40mInvalid Type Input\033[0;33;40m")
        else:
            if  max_sequence_size < 2:
                print("\033[0;31;40mUkuran minimal sequence adalah 2\033[0;33;40m")
            else:
                break

    # jumlah sequence
    while True:
        try:
            n_sequence = int(input("\033[0;33;40mJumlah sequence : \033[1;33;40m"))
        except:
            print("\033[0;31;40mInvalid Type Input\033[0;33;40m")
        else:
            if n_sequence > 0:
                list_sequence = []
                isPossible = True
                threshold = 100
                for i in range(0,n_sequence):
                    counter_threshold = 0
                    random.seed(time.time())
                    while True:
                        len_seq = int(random.randrange(2,max_sequence_size+1))
                        seq = []
                        
                        for j in range(len_seq):
                            idx = int(random.randrange(0,n_token_unik))
                            seq.append(tokens[idx])
                        
                        if seq not in list_sequence:
                            break
                        else:
                            if counter_threshold == threshold:
                                isPossible = False
                                break
                            else:
                                counter_threshold += 1

                    if isPossible:
                        list_sequence.append(seq)
                    else:
                        break
                
                if isPossible:
                    break
                else:
                    print("\033[0;31;40mJumlah tersebut tidak mungkin menghasilkan sequence yang unik semua, harus lebih kecil\033[0;33;40m")
            else:
                print("\033[0;31;40mJumlah sequence harus bernilai positif\033[0;33;40m")
                
    print()        
    
    # display matriks & sequence
    random.seed(time.time())
    print("\033[1;32;40mGenerated Matriks")
    print("-----------------\033[0;32;40m")
    for i in range(0,row):
        for j in range(0,col):
            if j != col-1:
                print(matriks[i][j], end=" ")
            else:
                print(matriks[i][j])
                
    print()
    
    # list_sequence = [[(tokens[int(random.randrange(0,n_token_unik))]) for j in range(0,int(random.randrange(1,max_sequence_size+1)))] for i in range(0,n_sequence)]

    
    random.seed(time.time())
    list_sequenceValue = [int(random.randrange(-100,101)) for i in range(0,n_sequence)]
    print("\033[1;36;40mGenerated Sequence")
    print("------------------\033[0;36;40m")
    for i in range(0,n_sequence):
        leng = len(list_sequence[i])
        for j in range(0,leng):
            if j != leng-1:
                print(list_sequence[i][j], end=" ")
            else:
                print(list_sequence[i][j],"--->",list_sequenceValue[i])
    print("\033[1;34;40m")

# set offsets
offsets = []
for i in range(0,buffer_size-1):
    offsets.append(1)

# set max_offsets
max_offsets = []
for i in range(0,buffer_size-1):
    if(i%2==0):
        max_offsets.append(row-1)
    else:
        max_offsets.append(col-1)

# # DUMMY
# matriks = [["7A", "55", "E9", "E9", "1C", "55"],["55", "7A", "1C", "7A", "E9", "55"],["55", "1C", "1C", "55", "E9", "BD"],["BD", "1C", "7A", "1C", "55", "BD"],["BD", "55", "BD", "7A", "1C", "1C"],["1C", "55", "55", "7A", "55", "7A"]]
# selected_coordinate = [(0,0)]

# # max value
# MAX_VALUE = 0
# BUFFER_MAX_VALUE_TOKEN = []
# BUFFER_MAX_VALUE_COORDINATE = []

# # sequence
# list_sequence = [["BD", "E9", "1C"],["BD", "7A", "BD"],["BD", "1C", "BD", "55"]]
# list_sequenceValue = [15,20,30]

# # buffer
# buffer_size = 7
# # list_buffer_token = []
# # list_buffer_coordinate = []
# # list_bufferValue = []

# # current processing
# current_buffer_token = []
# current_buffer_coordinate = []
# current_coordinate = []


# # offset
# offsets = [1,1,1,1,1,1]
# max_offsets = [5,5,5,5,5,5]

print("Result")
print("------\033[0;34;40m")

start = time.time()    
brute(len(matriks), len(matriks[0]))

print("MAX VALUE             =", MAX_VALUE)

N = len(BUFFER_MAX_VALUE_TOKEN)
print("TOKEN                 =", end=" ")
if len(BUFFER_MAX_VALUE_TOKEN) == 0:
    print("\033[0;31;40mTidak ada solusi yang menghasilkan value bernilai positif\033[0;34;40m")
else:
    for i in range(0, N):
        print(BUFFER_MAX_VALUE_TOKEN[i],end=" ")

    print()
   
print("COORDINATE (col,row)  =", end=" ")
if len(BUFFER_MAX_VALUE_COORDINATE) == 0:
    print("\033[0;31;40mTidak ada solusi yang menghasilkan value bernilai positif\033[0;34;40m")
else:
    for i in range(0, N):
        print("("+str(BUFFER_MAX_VALUE_COORDINATE[i][1]+1)+","+str(BUFFER_MAX_VALUE_COORDINATE[i][0]+1)+")",end=" ")

end = time.time()

print()
print("\033[0;32;40m")
print("Finished in", end-start," s")
print()

# BufferA = ['7A', 'BD', '7A', 'BD', '1C', 'BD', '55']
# bufferValue = 0
# n_sequence = len(list_sequence)
# # print("HOOOOOOOO",current_buffer_token)
# # print("HOOOOOOOO",SelectedCoordinate)
# # print(list_sequence)
# # print(list_sequenceValue)
# for i in range(0,n_sequence):
#     if (isSequenceMatch(BufferA,list_sequence[i])):
#         bufferValue += list_sequenceValue[i]
#         print(bufferValue)
# list_bufferValue.append(bufferValue)
# print(list_bufferValue)