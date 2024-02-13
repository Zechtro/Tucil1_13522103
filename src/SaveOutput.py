import os
import VarGlobal

def saveSolution(path):
    file = open(path, "w")
    for i in range(0,4):
        if i == 0:
            writeThis = str(VarGlobal.MAX_VALUE) + "\n"
        elif i == 1:
            writeThis = " ".join(VarGlobal.BUFFER_MAX_VALUE_TOKEN) + "\n"
        elif i == 2:
            if len(VarGlobal.BUFFER_MAX_VALUE_COORDINATE) == 0:
                writeThis = ("Tidak ada solusi yang menghasilkan value bernilai positif")
            else:
                N = len(VarGlobal.BUFFER_MAX_VALUE_TOKEN)
                for j in range(0, N):
                    writeThis = (str(VarGlobal.BUFFER_MAX_VALUE_COORDINATE[j][1]+1)+","+str(VarGlobal.BUFFER_MAX_VALUE_COORDINATE[j][0]+1)+"\n")
                    if j != N-1:
                        file.write(writeThis)
        else:
            writeThis = "\n" + str(VarGlobal.time_processing) + " ms\n"
        file.write(writeThis)
    file.close() 

def wantToSave():
    print("\033[0;33;40mDo you want to save the solution? (y/n)")
    isSaved = False

    while True:
        
        inp = input("\033[0;33;40m>>> \033[1;33;40m")
        
        if inp == "y":
            while True:
                filename = input("\033[0;33;40mInsert File Name (.txt): \033[1;33;40m")
                
                if ".txt" not in filename:
                    print("\033[0;31;40mOnly .txt file can be saved\033[0;33;40m")
                else:
                    break
            
            try:
                path = os.path.dirname(__file__) 
                os.chdir(path)
                os.chdir("../")
                path = os.getcwd()
                path = os.path.join(path,"test",filename)

                file = open(path, "x")
            except:
                print("File already exist, do you want to overwrite it? (y/n)")
                while True:
                    inp2 = input("\033[0;33;40m>>> \033[1;33;40m")
                    if inp2 == "y":
                        # SAVE
                        saveSolution(path)
                        isSaved = True
                        break
                    elif inp2 == "n":
                        print("\033[0;33;40mDo you want to save the solution? (y/n)")
                        break
                    else:
                        print("\033[0;31;40mInvalid Input")
                        
            else:
                # SAVE
                saveSolution(path)
                isSaved = True 
                
        elif inp == "n":
            print()
            break
            
        else:
            print("\033[0;31;40mInvalid Input")
            
        if isSaved:
            print()
            print("\033[1;32;40mFile successfully saved")
            print()
            break
