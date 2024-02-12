import flet as ft


            # TOKEN INPUT
            tokens = ft.TextField(label="Possible Alphanumeric Tokens", hint_text="X1 Y2 ZZ")
            ft.Text("*Any duplicate token will be ignored", color=Light_Black)
            tokens.upper()

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
                    else:
                        if (tokens[i][0] not in VarGlobal.alfanumerik) or (tokens[i][1] not in VarGlobal.alfanumerik):
                            print("\033[0;31;40mToken harus terdiri dari 2 karakter alfanumerik\033[0;33;40m")
                            valid = False
                            break
                if valid:
                    break   