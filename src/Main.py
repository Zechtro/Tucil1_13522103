from VarInit import *
from Input_TXT import *
from Input_CLI import *
from Process import *
from SaveOutput import *

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
    print()
    TXT_Input()
elif (input_type == 2):
    CLI_Input()
else:
    print("\033[0;31;40mInvalid Input\033[0;33;40m")

initOffsets()
DisplayResult()
wantToSave()
print("\033[1;34;40m==============================================")
print(" _____ _  _   _   _  _ _  ____   _____  _   _")
print("|_   _| || | /_\ | \| | |/ /\ \ / / _ \| | | |")
print("  | | | __ |/ _ \| .` | ' <  \ V / (_) | |_| |")
print("  |_| |_||_/_/ \_\_|\_|_|\_\  |_| \___/ \___/ ")
print("==============================================")

print("\033[0;37;40m")