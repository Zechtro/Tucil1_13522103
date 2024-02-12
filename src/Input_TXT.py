import os
import re
import time
import VarGlobal

def TXT_Input():
    finished = False
    while True:
        filename = input("\033[0;33;40mInsert File Name : \033[1;33;40m").lower()
        if not filename.endswith(".txt"):
            print("\033[0;31;40mOnly .txt file can be loaded\033[0;33;40m")
            continue
        try:
            path = os.path.dirname(__file__) 
            os.chdir(path)
            os.chdir("../")
            path = os.getcwd()
            path = os.path.join(path,"test",filename)

            file = open(path, "r")
        except:
            print("\033[0;31;40mFile not Found\033[0;33;40m")
        else:
            if os.stat(path).st_size==0:
                print("\033[0;31;40mFile is empty")
                print("\033[1;33;40mPlease input non-empty file name")
                continue
            print("\033[1;33;40mLoading file...")
            time.sleep(1)
            line_count = 0
            isValid = True
            for line in file:
                if line_count == 0:
                    try:
                        VarGlobal.buffer_size = int(line)
                    except:
                        isValid = False
                        print("\033[0;31;40mInvalid buffer size")
                        break
                    else:
                        if VarGlobal.buffer_size <= 0:
                            isValid = False
                            print("\033[0;31;40mInvalid buffer size")
                            break
                        else:
                            print("\033[0;32;40m✔ Buffer Size")
                            time.sleep(0.3)
                    
                elif line_count == 1:
                    m_size = line.split(" ")
                    try:
                        VarGlobal.col = int(m_size[0])
                        VarGlobal.row = int(m_size[1])
                    except:
                        isValid = False
                        print("\033[0;31;40mInvalid matrix size")
                        break
                    else:
                        if VarGlobal.col > 0 and VarGlobal.row >0: 
                            last_row_line = 1 + VarGlobal.row
                            print("\033[0;32;40m✔ Matrix Size")
                            time.sleep(0.3)
                        else:
                            isValid = False
                            print("\033[0;31;40mInvalid matrix size")
                            break
                            
                elif 2 <= line_count <= last_row_line:
                    line = re.split('\n| ', line)
                    line.pop()
                
                    if len(line) != VarGlobal.col:
                        isValid = False
                        print("\033[0;31;40mInvalid matrix")
                        break
                    else:  
                        for i in range(0,VarGlobal.col):
                                line[i] = (line[i])
                                if len(line[i]) != 2:
                                    isValid = False
                                    print("\033[0;31;40mInvalid token in matriks detected")
                                    break
                                else:
                                    if (line[i][0] not in VarGlobal.alfanumerik) or (line[i][1] not in VarGlobal.alfanumerik):
                                        print("\033[0;31;40mInvalid token in matriks detected")
                                        isValid = False
                                        break
                        if not isValid:
                            break
                        else:
                            VarGlobal.matriks.append(line)
                            print("\033[0;32;40m✔ Matrix Row", line_count-2)
                            time.sleep(0.3)
                
                        
                elif line_count == (1+last_row_line):
                    try:
                        VarGlobal.n_sequence = int(line)
                    except:
                        isValid = False
                        print("\033[0;31;40mInvalid jumlah sequence")
                        break
                    else:
                        if VarGlobal.n_sequence <= 0:
                            isValid = False
                            print("\033[0;31;40mInvalid jumlah sequence")
                            break
                        else:
                            last_line = 1 + (2*VarGlobal.n_sequence)
                            print("\033[0;32;40m✔ Jumlah Sequence")
                            time.sleep(0.3)
                        
                elif ((line_count-last_row_line)%2 == 0) and (line_count-last_row_line <= last_line):
                    line = re.split('\n| ', line)
                    line.pop()
                    n = len(line)
                    for i in range(0,n):
                            line[i] = (line[i])
                            if len(line[i]) != 2:
                                isValid = False
                                print("\033[0;31;40mInvalid token in sequence detected")
                                break
                            else:
                                if (line[i][0] not in VarGlobal.alfanumerik) or (line[i][1] not in VarGlobal.alfanumerik):
                                    print("\033[0;31;40mInvalid token in sequence detected\033[0;33;40m")
                                    isValid = False
                                    break
                    if not isValid:
                        # print("\033[0;31;40mInvalid token in sequence detected")
                        break
                    else:
                        VarGlobal.list_sequence.append(line)
                        print("\033[0;32;40m✔ Sequence",(line_count-last_row_line)//2)
                        time.sleep(0.3)
                
                elif ((line_count-last_row_line)%2 == 1) and ((line_count-last_row_line) <= last_line):
                    try:
                        value = int(line)
                    except:
                        isValid = False
                        print("\033[0;31;40mInvalid sequence reward")
                        break
                    else:
                        VarGlobal.list_sequenceValue.append(value)
                        print("\033[0;32;40m✔ Sequence",(line_count-last_row_line)//2, "Reward")
                        time.sleep(0.3)
                    if (line_count-last_row_line) == last_line:
                        finished = True
                        break
                
                # else:
                #     finished = True
                #     break
                    
                line_count += 1
            
            if not isValid:
                print("\033[1;31;40mFile Process Terminated\033[0;37;40m\n")
                break
            else:
                if finished:
                    print("\033[1;32;40mData successfully loaded\033[1;32;40m")
                    time.sleep(0.3)
                    
                    print()
                    
                    # display matriks & sequence
                    print("\033[1;35;40mMatriks")
                    print("-------\033[0;35;40m")
                    for i in range(0,VarGlobal.row):
                        for j in range(0,VarGlobal.col):
                            if j != VarGlobal.col-1:
                                print(VarGlobal.matriks[i][j], end=" ")
                            else:
                                print(VarGlobal.matriks[i][j])
                    time.sleep(1)            
                    
                    print()
                    
                    print("\033[1;36;40mSequence")
                    print("--------\033[0;36;40m")
                    for i in range(0,VarGlobal.n_sequence):
                        leng = len(VarGlobal.list_sequence[i])
                        for j in range(0,leng):
                            if j != leng-1:
                                print(VarGlobal.list_sequence[i][j], end=" ")
                            else:
                                print(VarGlobal.list_sequence[i][j],"--->",VarGlobal.list_sequenceValue[i])
                    time.sleep(1)
                    print("\033[1;34;40m")
                    break
                else:
                    print("\033[0;31;40mInvalid file content")
                    print("\033[1;31;40mFile Process Terminated\033[0;37;40m\n")
            file.close()