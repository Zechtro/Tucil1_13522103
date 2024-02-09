import random
import time
import VarGlobal

def CLI_Input():
    
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
            VarGlobal.buffer_size = int(input("\033[0;33;40mBuffer size : \033[1;33;40m"))
        except:
            print("\033[0;31;40mInvalid Type Input\033[0;33;40m")
        else:
            if VarGlobal.buffer_size > 0:
                break
            else:
                print("\033[0;31;40mUkuran Buffer harus bernilai positif\033[0;33;40m")
            
    # matriks size
    while True:
        try:
            VarGlobal.col, VarGlobal.row = [ int(x) for x in input("\033[0;33;40mMatriks size (col row) : \033[1;33;40m").split(" ")]
        except:
            print("\033[0;31;40mInvalid Type Input\033[0;33;40m")
        else:
            if VarGlobal.row <= 0:
                print("\033[0;31;40mUkuran baris pada matriks harus bernilai positif\033[0;33;40m")
            if VarGlobal.col <= 0:
                print("\033[0;31;40mUkuran kolom pada matriks harus bernilai positif\033[0;33;40m")
            if VarGlobal.row > 0 and VarGlobal.col > 0:
                VarGlobal.matriks = [[(tokens[int(random.randrange(0,n_token_unik))]) for j in range(0,VarGlobal.col)] for i in range(0,VarGlobal.row)]
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
            VarGlobal.n_sequence = int(input("\033[0;33;40mJumlah sequence : \033[1;33;40m"))
        except:
            print("\033[0;31;40mInvalid Type Input\033[0;33;40m")
        else:
            if VarGlobal.n_sequence > 0:
                VarGlobal.list_sequence = []
                isPossible = True
                threshold = 100
                for i in range(0, VarGlobal.n_sequence):
                    counter_threshold = 0
                    random.seed(time.time())
                    while True:
                        len_seq = int(random.randrange(2,max_sequence_size+1))
                        seq = []
                        
                        for j in range(len_seq):
                            idx = int(random.randrange(0,n_token_unik))
                            seq.append(tokens[idx])
                        
                        if seq not in VarGlobal.list_sequence:
                            break
                        else:
                            if counter_threshold == threshold:
                                isPossible = False
                                break
                            else:
                                counter_threshold += 1

                    if isPossible:
                        VarGlobal.list_sequence.append(seq)
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
    print("\033[1;35;40mGenerated Matriks")
    print("-----------------\033[0;35;40m")
    for i in range(0,VarGlobal.row):
        for j in range(0,VarGlobal.col):
            if j != VarGlobal.col-1:
                print(VarGlobal.matriks[i][j], end=" ")
            else:
                print(VarGlobal.matriks[i][j])
    time.sleep(1)
                
    print()
    
    random.seed(time.time())
    VarGlobal.list_sequenceValue = [int(random.randrange(-100,101)) for i in range(0, VarGlobal.n_sequence)]
    print("\033[1;36;40mGenerated Sequence")
    print("------------------\033[0;36;40m")
    for i in range(0,VarGlobal.n_sequence):
        leng = len(VarGlobal.list_sequence[i])
        for j in range(0,leng):
            if j != leng-1:
                print(VarGlobal.list_sequence[i][j], end=" ")
            else:
                print(VarGlobal.list_sequence[i][j],"--->",VarGlobal.list_sequenceValue[i])
    time.sleep(1)
    print("\033[1;34;40m")