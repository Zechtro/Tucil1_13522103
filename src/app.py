import flet as ft
import flet.canvas as cv
import os
import time
import VarGlobal
import VarInit
import re
import BruteForce
import random
alfanumerik = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","0","1","2","3","4","5","6","7","8","9"]

def main(page: ft.Page):
    page.title = "Brute Force"
    h = 800
    w = 1500
    page.window_height = h
    page.window_width = w
    page.window_resizable = False
    
    page.fonts = {
        "Glitch" : "/fonts/glitch-font/GlitchGoblin-2O87v.ttf",
    }
    White = "#FFFFFF"
    Black = "#252525"
    Blue = "#0E49B5"
    Light_Black = "#393E46"
    
    isValid = False
    
    page.theme = ft.theme.Theme(color_scheme_seed=Blue)
    page.update
    
    row_title = ft.Row(
        alignment="center",
        controls=[
            ft.Text("BRUTE FORCE",size=50,color=Blue,font_family="Glitch")
        ]
    )
    
    def makeListEmpty(List):
        List.clear()
    
    def resetProblem():
        save_file_textfield.disabled=True
        save_button.disabled=True
        VarGlobal.buffer_size = 0
        VarGlobal.row = 0
        VarGlobal.col = 0
        VarGlobal.n_sequence = 0
        VarGlobal.MAX_VALUE = 0
        txt_savefile.color=Black
        save_file_textfield.error_text=""
        save_file_textfield.helper_text=""
        save_file_textfield.value=""
        save_file_textfield.hint_style={"color":Black}
        makeListEmpty(VarGlobal.BUFFER_MAX_VALUE_COORDINATE)
        makeListEmpty(VarGlobal.BUFFER_MAX_VALUE_TOKEN)
        makeListEmpty(VarGlobal.current_buffer_coordinate)
        makeListEmpty(VarGlobal.current_buffer_token)
        makeListEmpty(VarGlobal.max_offsets)
        makeListEmpty(VarGlobal.current_coordinate)
        makeListEmpty(sequence_datarows)
        makeListEmpty(widget_matrix_row_list)
        makeListEmpty(VarGlobal.list_sequence)
        makeListEmpty(VarGlobal.list_sequenceValue)
        makeListEmpty(VarGlobal.offsets)
        makeListEmpty(VarGlobal.matriks)
        makeListEmpty(unique_tokens)
        page.update()
        
    def resetPartial():
        save_file_textfield.disabled=True
        save_file_textfield.hint_style={"color":Black}
        save_button.disabled=True
        VarGlobal.MAX_VALUE = 0
        VarGlobal.MAX_VALUE = 0
        txt_savefile.color=Black
        save_file_textfield.error_text=""
        save_file_textfield.helper_text=""
        save_file_textfield.value=""
        makeListEmpty(VarGlobal.BUFFER_MAX_VALUE_COORDINATE)
        makeListEmpty(VarGlobal.BUFFER_MAX_VALUE_TOKEN)
        makeListEmpty(VarGlobal.current_buffer_coordinate)
        makeListEmpty(VarGlobal.current_buffer_token)
        makeListEmpty(VarGlobal.max_offsets)
        makeListEmpty(VarGlobal.current_coordinate)
        makeListEmpty(sequence_datarows)
        makeListEmpty(widget_matrix_row_list)
        makeListEmpty(solution_path)
    
    def solve(e):
        reward_text.value ="Reward : processing..."
        page.update()
        makeListEmpty(x_move_list)
        makeListEmpty(y_move_list)
        makeListEmpty(solution_path)
        if VarGlobal.row >= VarGlobal.col:
            container_cell_size = float(400/VarGlobal.row)
            text_token_size = float(container_cell_size/4)
        else:
            container_cell_size = float(400/VarGlobal.col)
            text_token_size = float(container_cell_size/4)
        cell_size = float(0.8*container_cell_size)
        paint_canvas.stroke_width= float(0.1*container_cell_size)
        page.update()
        VarInit.initOffsets()
        start=time.time()
        BruteForce.brute(VarGlobal.row,VarGlobal.col)
        end=time.time()
        VarGlobal.time_processing=int((end-start)*1000)
        reward_text.value = f"Reward : {VarGlobal.MAX_VALUE}"

        n = len(VarGlobal.BUFFER_MAX_VALUE_COORDINATE)
        for i in range(0,len(VarGlobal.BUFFER_MAX_VALUE_COORDINATE)):
            coordinate = VarGlobal.BUFFER_MAX_VALUE_COORDINATE[i]
            if i > 0:
                prev_coordinate = VarGlobal.BUFFER_MAX_VALUE_COORDINATE[i-1]
            if i < (n-1):
                next_coordinate = VarGlobal.BUFFER_MAX_VALUE_COORDINATE[i+1]
            # X
            center_x = float(0.5*container_cell_size+((500-(VarGlobal.col*container_cell_size))/(2*VarGlobal.col))) + float((coordinate[1])*(container_cell_size+(2*((500-(VarGlobal.col*container_cell_size))/(2*VarGlobal.col)))))
            if i > 0:
                if prev_coordinate[1] < coordinate[1]:
                    x = center_x - float(0.5*container_cell_size)
                elif prev_coordinate[1] > coordinate[1]:
                    x = center_x + float(0.5*container_cell_size)
                else:
                    x = center_x
                x_move_list.append(x)
                    
            if i < (n-1):
                if coordinate[1] < next_coordinate[1]:
                    x = center_x + float(0.5*container_cell_size)
                elif coordinate[1] > next_coordinate[1]:
                    x = center_x - float(0.5*container_cell_size)
                else:
                    x = center_x
                x_move_list.append(x)
            # Y
            center_y = float(0.5*container_cell_size+((500-(VarGlobal.row*container_cell_size))/(2*VarGlobal.row))) + float((coordinate[0])*(container_cell_size+(2*((500-(VarGlobal.row*container_cell_size))/(2*VarGlobal.row)))))
            if i > 0:
                if prev_coordinate[0] < coordinate[0]:
                    y = center_y - float(0.5*container_cell_size)
                elif prev_coordinate[0] > coordinate[0]:
                    y = center_y + float(0.5*container_cell_size)
                else:
                    y = center_y
                y_move_list.append(y)
                    
            if i < (n-1):
                if coordinate[0] < next_coordinate[0]:
                    y = center_y + float(0.5*container_cell_size)
                elif coordinate[0] > next_coordinate[0]:
                    y = center_y - float(0.5*container_cell_size)
                else:
                    y = center_y
                y_move_list.append(y)

        for i in range(0,len(x_move_list)):
            current_x = x_move_list[i]
            current_y = y_move_list[i] 
            if i%2 == 0:
                path = cv.Path.MoveTo(current_x,current_y)
            else:
                path = cv.Path.LineTo(current_x,current_y)
            solution_path.append(path)
      
        for i in range(0,VarGlobal.row):
            cell_list = []
            for j in range(0,VarGlobal.col):
                token = VarGlobal.matriks[i][j]
                coordinate_token = [i,j]
                if len(VarGlobal.BUFFER_MAX_VALUE_COORDINATE) > 0:
                    if coordinate_token == VarGlobal.BUFFER_MAX_VALUE_COORDINATE[0]:
                        BGCOLOR="#2192FF"
                    elif coordinate_token in VarGlobal.BUFFER_MAX_VALUE_COORDINATE:
                        BGCOLOR = Blue
                    else:
                        BGCOLOR = Black
                else:
                    BGCOLOR = Black
                cell_list.append(
                    ft.Container(
                        alignment=ft.alignment.center,
                        bgcolor=BGCOLOR,
                        height = container_cell_size,
                        width = container_cell_size,
                        content=ft.Column(
                            alignment="SPACEAROUND",
                            controls=[
                                ft.Container(  
                                    alignment=ft.alignment.center,
                                    width=cell_size,
                                    height=cell_size,
                                    bgcolor=Black,
                                    content=ft.Text(
                                        value=token,
                                        size=text_token_size,
                                        text_align="CENTER",
                                        color=Blue,
                                    )
                                )
                            ]
                        )
                    )
                )
            widget_matrix_row_list[i] = ft.Row(
                alignment="SPACEAROUND",
                controls=cell_list
            )
        save_file_textfield.disabled=False
        save_file_textfield.hint_style={
            "color":Light_Black
        }
        txt_savefile.color=Blue
        page.update()
    
    solve_button_manual = ft.ElevatedButton(
        text="SOLVE!",
        width=200,
        height=50,
        bgcolor=Blue,
        color=Black,
        disabled=True,
        on_click=solve
    )
    
    solve_button_manual_container = ft.Container(
        alignment=ft.alignment.center,
        content=solve_button_manual,
    )
    
    # INPUT MANUAL
    unique_tokens = []
    max_sequence_size = [0]
    def isDataComplete():
        if (VarGlobal.buffer_size > 0 and len(VarGlobal.list_sequence) > 0 and len(VarGlobal.matriks) > 0):
            if VarGlobal.row >= VarGlobal.col:
                container_cell_size = float(400/VarGlobal.row)
                text_token_size = float(container_cell_size/4)
            else:
                container_cell_size = float(400/VarGlobal.col)
                text_token_size = float(container_cell_size/4)
            cell_size = float(0.8*container_cell_size)
            paint_canvas.stroke_width = float(0.1*container_cell_size)
            page.update()
            for i in range(0,VarGlobal.row):
                cell_list = []
                for j in range(0,VarGlobal.col):
                    token = VarGlobal.matriks[i][j]
                    cell_list.append(
                        ft.Container(
                            alignment=ft.alignment.center,
                            bgcolor=Black,
                            height = container_cell_size,
                            width = container_cell_size,
                            content=ft.Column(
                                alignment="SPACEAROUND",
                                controls=[
                                    ft.Container(  
                                        alignment=ft.alignment.center,
                                        width=cell_size,
                                        height=cell_size,
                                        bgcolor=Black,
                                        content=ft.Text(
                                            value=token,
                                            size=text_token_size,
                                            text_align="CENTER",
                                            color=Blue,
                                        )
                                    )
                                ]
                            )
                        )
                    )

                widget_matrix_row_list.append(
                    ft.Row(
                    alignment="SPACEAROUND",
                    controls=cell_list
                    )
                )
            for i in range(0,VarGlobal.n_sequence):
                sequence = VarGlobal.list_sequence[i]
                sequence = " ".join(sequence)
                seq_reward = str(VarGlobal.list_sequenceValue[i])
                sequence_datarows.append(
                    ft.DataRow(
                        cells=[
                            ft.DataCell(ft.Text(value=sequence, size=20,color=Blue,text_align="center")),
                            ft.DataCell(ft.Text(value=seq_reward, size=20,color=Blue,text_align="center"))
                        ]
                    )
                )
            page.update()
            solve_button_manual.disabled=False
            page.update()
        else:
            solve_button_manual.disabled=True
            page.update()
    
    def token_changed(e):
        resetPartial()
        makeListEmpty(unique_tokens)
        tokens = e.control.value
        tokens = tokens.split(" ")
        isValid = True
        for token in tokens:
            if len(token)!=2:
                makeListEmpty(unique_tokens)
                e.control.error_text="Token harus terdiri dari 2 karakter alfanumerik"
                page.update()
                isValid=False
                break
            else:
                if token[0] not in alfanumerik or token[1] not in alfanumerik:
                    e.control.error_text="Token harus terdiri dari 2 karakter alfanumerik"
                    makeListEmpty(unique_tokens)
                    page.update()
                    isValid=False
                    break
        if isValid:
            e.control.error_text=""
            for i in range(0,len(tokens)):
                unique_tokens.append(tokens[i])
            generateSequence()
            if VarGlobal.col > 0 and VarGlobal.row > 0:
                random.seed(time.time())
                VarGlobal.matriks = [[(unique_tokens[int(random.randrange(0,len(unique_tokens)))]) for j in range(0,VarGlobal.col)] for i in range(0,VarGlobal.row)]
            isDataComplete()
            page.update()
                    
    input_token_field = ft.TextField(
        text_size= 10,
        border_color=Blue,
        color=Blue,        
        hint_text="AA BB X1 y2 ZZ",
        hint_style={"color":Light_Black},
        helper_text="*token must be unique (case sensitive)",
        
        on_change=token_changed
    )
        
    container_input_tokens = ft.Container(
        width=300,
        height=80,
        content=ft.Column(
            controls=[
                ft.Text("Tokens", color=Blue, font_family="Glitch",size=20),
                input_token_field
            ]
        )
    )
    
    def dropdown_changed_buffer(e):
        resetPartial()
        VarGlobal.buffer_size = int(buffer_size_dropdown.value)
        isDataComplete()
        page.update()
    
    buffer_size_dropdown = ft.Dropdown(
        height=55,
        width=150,
        border_color=Blue,
        color=Blue,
        options=[
            ft.dropdown.Option("1"),
            ft.dropdown.Option("2"),
            ft.dropdown.Option("3"),
            ft.dropdown.Option("4"),
            ft.dropdown.Option("5"),
            ft.dropdown.Option("6"),
            ft.dropdown.Option("7"),
        ],
        on_change=dropdown_changed_buffer
    )
    
    def dropdown_changed_col(e):
        resetPartial()
        VarGlobal.col = int(col_dropdown.value)
        if VarGlobal.row > 0 and len(unique_tokens) > 0:
            random.seed(time.time())
            VarGlobal.matriks = [[(unique_tokens[int(random.randrange(0,len(unique_tokens)))]) for j in range(0,VarGlobal.col)] for i in range(0,VarGlobal.row)]
            isDataComplete()        
        page.update()
    
    col_dropdown = ft.Dropdown(
        height=85,
        width=70,
        color=Blue,
        border_color=Blue,
        helper_text="Column",
        options=[
            ft.dropdown.Option("1"),
            ft.dropdown.Option("2"),
            ft.dropdown.Option("3"),
            ft.dropdown.Option("4"),
            ft.dropdown.Option("5"),
            ft.dropdown.Option("6"),
            ft.dropdown.Option("7"),
            ft.dropdown.Option("8"),
            ft.dropdown.Option("9"),
            ft.dropdown.Option("10"),
        ],
        on_change=dropdown_changed_col
    )
    
    def dropdown_changed_row(e):
        resetPartial()
        VarGlobal.row = int(row_dropdown.value)
        if VarGlobal.col > 0 and len(unique_tokens) > 0:
            random.seed(time.time())
            VarGlobal.matriks = [[(unique_tokens[int(random.randrange(0,len(unique_tokens)))]) for j in range(0,VarGlobal.col)] for i in range(0,VarGlobal.row)]
            isDataComplete()
        page.update()
    
    row_dropdown = ft.Dropdown(
        height=85,
        width=70,
        color=Blue,
        border_color=Blue,
        helper_text="Row",
        options=[
            ft.dropdown.Option("1"),
            ft.dropdown.Option("2"),
            ft.dropdown.Option("3"),
            ft.dropdown.Option("4"),
            ft.dropdown.Option("5"),
            ft.dropdown.Option("6"),
            ft.dropdown.Option("7"),
            ft.dropdown.Option("8"),
            ft.dropdown.Option("9"),
            ft.dropdown.Option("10"),
        ],
        on_change=dropdown_changed_row
    )
    
    def generateSequence():
        resetPartial()
        makeListEmpty(VarGlobal.list_sequence)
        makeListEmpty(VarGlobal.list_sequenceValue)
        if VarGlobal.n_sequence > 0 and max_sequence_size[0] > 0 and len(unique_tokens) > 0:
            VarGlobal.list_sequence = []
            isPossible = True
            threshold = 100
            for i in range(0, VarGlobal.n_sequence):
                counter_threshold = 0
                random.seed(time.time())
                while True:
                    len_seq = int(random.randrange(2,max_sequence_size[0]+1))
                    seq = []
                    
                    for j in range(len_seq):
                        idx = int(random.randrange(0,len(unique_tokens)))
                        seq.append(unique_tokens[idx])
                    
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
                VarGlobal.list_sequenceValue = [int(random.randrange(-100,101)) for i in range(0, VarGlobal.n_sequence)]
                sequence_count_dropdown.error_text=""
                sequence_size_dropdown.error_text=""
                
            else:
                sequence_count_dropdown.error_text="Num"
                sequence_size_dropdown.error_text="Size"
    
    def dropdown_changed_sequenceCount(e):
        VarGlobal.n_sequence = int(sequence_count_dropdown.value)
        generateSequence()
        isDataComplete()
        page.update()
        
    sequence_count_dropdown = ft.Dropdown(
        height=85,
        width=70,
        color=Blue,
        border_color=Blue,
        helper_text="Num",
        options=[
            ft.dropdown.Option("1"),
            ft.dropdown.Option("2"),
            ft.dropdown.Option("3"),
            ft.dropdown.Option("4"),
            ft.dropdown.Option("5"),
            ft.dropdown.Option("6"),
            ft.dropdown.Option("7"),
            ft.dropdown.Option("8"),
            ft.dropdown.Option("9"),
            ft.dropdown.Option("10"),
        ],
        on_change=dropdown_changed_sequenceCount,
    )
    
    def dropdown_changed_sequenceSize(e):
        max_sequence_size[0] = int(sequence_size_dropdown.value)
        generateSequence()
        isDataComplete()
        page.update()
        
    sequence_size_dropdown = ft.Dropdown(
        height=85,
        width=80,
        color=Blue,
        border_color=Blue,
        helper_text="Max Size",
        options=[
            ft.dropdown.Option("2"),
            ft.dropdown.Option("3"),
            ft.dropdown.Option("4"),
            ft.dropdown.Option("5"),
            ft.dropdown.Option("6"),
            ft.dropdown.Option("7"),
            ft.dropdown.Option("8"),
            ft.dropdown.Option("9"),
            ft.dropdown.Option("10"),
        ],
        on_change=dropdown_changed_sequenceSize
    )
    
    # MANUAL INPUT
    manual_input_container = ft.Container(
        width=w//2,
        alignment=ft.alignment.center,
        content=ft.Column(
            controls=[
                # TOKEN INPUT
                ft.Container(
                    alignment=ft.alignment.top_center,
                    content=ft.Row(
                        alignment="CENTER",
                        controls=[
                            container_input_tokens,
                            ft.Container(
                                content=ft.Column(
                                    height=80,
                                    controls=[
                                        ft.Text("Buffer Size", size=20,color=Blue, font_family="Glitch"),
                                        buffer_size_dropdown
                                    ]
                                )
                            ),
                            
                        ]
                        
                    ),
                ),
                ft.Container(
                    margin=ft.margin.only(top=35,left=150),
                    width=400,
                    content=ft.Row(
                        width=w//2 - 80,
                        alignment="SPACEBETWEEN",
                        controls=[
                            # SEQUENCE COUNT
                            ft.Container(
                                content=ft.Column(
                                    controls=[
                                        ft.Text("Sequence", size=20,color=Blue, font_family="Glitch",text_align="center"),
                                        ft.Row(
                                            controls=[
                                                ft.Column(
                                                    controls=[
                                                        sequence_size_dropdown
                                                    ]
                                                ),  
                                                ft.Column(
                                                    controls=[
                                                        sequence_count_dropdown,
                                                    ]
                                                ),
                                            ]
                                        )
                                    ]
                                )
                            ),
                         
                            # MATRIX SIZE
                            ft.Container(
                                content=ft.Column(
                                    controls=[
                                        ft.Text("Matrix Size", size=20, color=Blue, font_family="Glitch",text_align="center"),
                                        ft.Row(
                                            controls=[
                                                ft.Column(
                                                    controls=[
                                                        col_dropdown
                                                    ]
                                                ),
                                                ft.Column(
                                                    controls=[
                                                        row_dropdown
                                                    ]
                                                )   
                                            ]
                                        )
                                    ]
                                )
                            ),
                        ]
                    )
                )
            ] 
        )
    )
    
    # SOLVE! BUTTON
    container_cell_size = 0
    cell_size = 0
    x_move_list = [] 
    y_move_list = [] 
    solution_path = []
    widget_matrix_row_list = []
    widget_cell_list = []
    
    paint_canvas = ft.Paint(
        style=ft.PaintingStyle.STROKE,
        color=Blue
    )
    
    sequence_datarows = []
    reward_text = ft.Text(value="Reward :", size=30,font_family="Glitch",color=Blue)


    # INPUT .TXT
    def filename_changed(e):
        resetProblem()
        reward_text.value = "Reward :"
        makeListEmpty(sequence_datarows)
        page.update()
        makeListEmpty(widget_matrix_row_list)
        makeListEmpty(solution_path)
        finished = False
        isButtonDisable = True
        filename = str(e.control.value).lower()
        if not filename.endswith(".txt"):
            isValid = False
            e.control.error_text="Only .txt file will be accepted"
            page.update()
        else:
            try:
                path = os.path.dirname(__file__) 
                os.chdir(path)
                os.chdir("../")
                path = os.getcwd()
                path = os.path.join(path,"test",filename)

                file = open(path, "r")
            except:
                isValid = False
                e.control.error_text="File not found -- pastikan file terdapat pada folder \"test\""
                page.update()
            else:
                resetProblem()
                isValid = True
                e.control.error_text=""
                e.control.helper_text="File found -- checking on file..."
                page.update()
                time.sleep(0.5)
                if os.stat(path).st_size==0:
                    e.control.error_text="The file is empty"
                    page.update()
                else:
                    line_count = 0
                    isValid = True
                    for line in file:
                        if line_count == 0:
                            try:
                                VarGlobal.buffer_size = int(line)
                            except:
                                isValid = False
                                e.control.error_text="Invalid buffer size"
                                e.control.helper_text=""
                                page.update()
                                break
                            else:
                                if VarGlobal.buffer_size <= 0:
                                    isValid = False
                                    e.control.error_text="Invalid buffer size"
                                    e.control.helper_text=""
                                    page.update()
                                    break
                            
                        elif line_count == 1:
                            m_size = line.split(" ")
                            try:
                                VarGlobal.col = int(m_size[0])
                                VarGlobal.row = int(m_size[1])
                            except:
                                isValid = False
                                e.control.error_text="Invalid matrix size"
                                e.control.helper_text=""
                                page.update()
                                break
                            else:
                                if VarGlobal.col > 0 and VarGlobal.row >0: 
                                    last_row_line = 1 + VarGlobal.row
                                else:
                                    isValid = False
                                    e.control.error_text="Invalid matrix size"
                                    e.control.helper_text=""
                                    page.update()
                                    break
                                    
                        elif 2 <= line_count <= last_row_line:
                            line = re.split('\n| ', line)
                            line.pop()
                        
                            if len(line) != VarGlobal.col:
                                isValid = False
                                e.control.error_text="Invalid matrix"
                                e.control.helper_text=""
                                page.update()
                                break
                            else:  
                                for i in range(0,VarGlobal.col):
                                        line[i] = (line[i])
                                        if len(line[i]) != 2:
                                            isValid = False
                                            e.control.error_text="Invalid token in matriks detected"
                                            e.control.helper_text=""
                                            page.update()
                                            break
                                        else:
                                            if (line[i][0] not in VarGlobal.alfanumerik) or (line[i][1] not in VarGlobal.alfanumerik):
                                                e.control.error_text="Invalid token in matriks detected"
                                                e.control.helper_text=""
                                                page.update()
                                                isValid = False
                                                break
                                if not isValid:
                                    break
                                else:
                                    VarGlobal.matriks.append(line)
                                
                        elif line_count == (1+last_row_line):
                            try:
                                VarGlobal.n_sequence = int(line)
                            except:
                                isValid = False
                                e.control.error_text="Invalid jumlah sequence"
                                e.control.helper_text=""
                                page.update()
                                break
                            else:
                                if VarGlobal.n_sequence <= 0:
                                    isValid = False
                                    e.control.error_text="Invalid jumlah sequence"
                                    e.control.helper_text=""
                                    page.update()
                                    break
                                else:
                                    last_line = 1 + (2*VarGlobal.n_sequence)
                                
                        elif ((line_count-last_row_line)%2 == 0) and (line_count-last_row_line <= last_line):
                            line = re.split('\n| ', line)
                            line.pop()
                            n = len(line)
                            for i in range(0,n):
                                    line[i] = (line[i])
                                    if len(line[i]) != 2:
                                        isValid = False
                                        e.control.error_text="Invalid token in sequence detected"
                                        e.control.helper_text=""
                                        page.update()
                                        break
                                    else:
                                        if (line[i][0] not in VarGlobal.alfanumerik) or (line[i][1] not in VarGlobal.alfanumerik):
                                            e.control.error_text="Invalid token in sequence detected"
                                            e.control.helper_text=""
                                            page.update()
                                            isValid = False
                                            break
                            if not isValid:
                                break
                            else:
                                VarGlobal.list_sequence.append(line)
                        
                        elif ((line_count-last_row_line)%2 == 1) and ((line_count-last_row_line) <= last_line):
                            try:
                                value = int(line)
                            except:
                                isValid = False
                                e.control.error_text="Invalid sequence reward"
                                e.control.helper_text=""
                                page.update()
                                break
                            else:
                                VarGlobal.list_sequenceValue.append(value)
                            if (line_count-last_row_line) == last_line:
                                finished = True
                                break
                 
                        line_count += 1
                    
                    if not isValid:
                        e.control.error_text="Invalid File Content"
                        e.control.helper_text=""
                        page.update()
                    else:
                        if finished:
                            isButtonDisable = False
                            e.control.error_text=""
                            e.control.helper_text="Data successfully loaded"
                            if VarGlobal.row >= VarGlobal.col:
                                container_cell_size = float(400/VarGlobal.row)
                                text_token_size = float(container_cell_size/4)
                            else:
                                container_cell_size = float(400/VarGlobal.col)
                                text_token_size = float(container_cell_size/4)
                            cell_size = float(0.8*container_cell_size)
                            paint_canvas.stroke_width = float(0.1*container_cell_size)
                            page.update()
                            for i in range(0,VarGlobal.row):
                                cell_list = []
                                for j in range(0,VarGlobal.col):
                                    token = VarGlobal.matriks[i][j]
                                    cell_list.append(
                                        ft.Container(
                                            alignment=ft.alignment.center,
                                            bgcolor=Black,
                                            height = container_cell_size,
                                            width = container_cell_size,
                                            content=ft.Column(
                                                alignment="SPACEAROUND",
                                                controls=[
                                                    ft.Container(  
                                                        alignment=ft.alignment.center,
                                                        width=cell_size,
                                                        height=cell_size,
                                                        bgcolor=Black,
                                                        content=ft.Text(
                                                            value=token,
                                                            size=text_token_size,
                                                            text_align="CENTER",
                                                            color=Blue,
                                                        )
                                                    )
                                                ]
                                            )
                                        )
                                    )

                                widget_matrix_row_list.append(
                                    ft.Row(
                                    alignment="SPACEAROUND",
                                    controls=cell_list
                                    )
                                )
                            for i in range(0,VarGlobal.n_sequence):
                                sequence = VarGlobal.list_sequence[i]
                                sequence = " ".join(sequence)
                                seq_reward = str(VarGlobal.list_sequenceValue[i])
                                sequence_datarows.append(
                                    ft.DataRow(
                                        cells=[
                                            ft.DataCell(ft.Text(value=sequence, size=20,color=Blue,text_align="center")),
                                            ft.DataCell(ft.Text(value=seq_reward, size=20,color=Blue,text_align="center"))
                                        ]
                                    )
                                )
                            page.update()
                        else:
                            e.control.error_text="Invalid File Content"
                            e.control.helper_text=""
                            page.update()
                file.close()

        solve_button.disabled = isButtonDisable
        page.update()
    
    file_name_input = ft.TextField(
        width=w//4,
        border_color=Blue,
        color=Blue,        
        hint_text="filename.txt",
        hint_style={"color":Light_Black},
        helper_text="File terdapat pada folder \"test\"",
        
        on_change=filename_changed
    )
    
    file_input_container = ft.Container(
        alignment=ft.alignment.center,
        content=ft.Column(
            alignment=ft.alignment.center,
            controls=[
                ft.Text("Insert File Name", size=30,font_family="Glitch",color=Blue),
                file_name_input
            ]
        )
    )
    
    solve_button = ft.ElevatedButton(
        text="SOLVE!",
        width=200,
        height=50,
        bgcolor=Blue,
        color=Black,
        disabled=True,
        on_click=solve
    )
    
    solve_button_container = ft.Container(
        alignment=ft.alignment.center,
        content=solve_button,
    )
    
    sequence_listview_container = ft.Container(
        height=150,
        width=500,
        margin=ft.margin.only(left=125),
        alignment=ft.alignment.center,
        content=ft.ListView(
            controls=[
                ft.DataTable(
                    border=ft.border.all(3, Blue),
                    horizontal_lines=ft.border.BorderSide(2, Blue),
                    columns=[
                        ft.DataColumn(ft.Text("Sequence", size=20,color=Blue,font_family="Glitch",text_align="center")),
                        ft.DataColumn(ft.Text("Reward", size=20,color=Blue,font_family="Glitch",text_align="center"))
                    ],
                    rows=sequence_datarows,
                )
            ]
        )
    )
    
    save_path = [""]
    
    def save_file(e):
        path = save_path[0]
        file = open(path, "w")
        for i in range(0,4):
            if i == 0:
                writeThis = str(VarGlobal.MAX_VALUE) + "\n"
            elif i == 1:
                writeThis = " ".join(VarGlobal.BUFFER_MAX_VALUE_TOKEN) + "\n"
            elif i == 2:
                if len(VarGlobal.BUFFER_MAX_VALUE_COORDINATE) == 0:
                    writeThis = ("\033[0;31;40mTidak ada solusi yang menghasilkan value bernilai positif\033[0;34;40m")
                else:
                    N = len(VarGlobal.BUFFER_MAX_VALUE_TOKEN)
                    for j in range(0, N):
                        writeThis = (str(VarGlobal.BUFFER_MAX_VALUE_COORDINATE[j][1]+1)+","+str(VarGlobal.BUFFER_MAX_VALUE_COORDINATE[j][0]+1)+"\n")
                        if j != N-1:
                            file.write(writeThis)
            else:
                writeThis = "\n" + str(VarGlobal.time_processing) + " ms\n"
            file.write(writeThis)
        save_file_textfield.helper_text="FILE SAVED"
        file.close() 
        page.update()
    
    save_button = ft.ElevatedButton(
        width=200,
        height=60,
        bgcolor="#16FF00",
        color=Black,
        text="Save Result",
        disabled=True,
        on_click=save_file
    )
    
    def changed_filesave(e):
        save_file_textfield.helper_text=""
        save_file_textfield.error_text=""
        page.update()
        filename = str(save_file_textfield.value).lower()
        if filename.endswith(".txt"):
            try:
                path = os.path.dirname(__file__) 
                os.chdir(path)
                os.chdir("../")
                path = os.getcwd()
                path = os.path.join(path,"test",filename)

                file = open(path, "r")
            except:
                save_path[0] = path
                save_file_textfield.error_text=""
                save_button.disabled=False
            else:
                save_button.disabled=True
                save_file_textfield.error_text ="File already exist"
                file.close()
        else:
            save_button.disabled=True
            save_file_textfield.error_text="File must be .txt"
        page.update()
    
    save_file_textfield = ft.TextField(
        hint_text="save.txt",
        height=70,
        width=150,
        border_color=Blue,
        color=Blue, 
        text_size=10,
        on_change=changed_filesave,
        hint_style={"color":Black},
        disabled=True
    )
    
    txt_savefile = ft.Text(value="Save File?",color=Black,font_family="Glitch")
    save_container = ft.Row(
        alignment="CENTER",
        controls=[
            txt_savefile,
            ft.Container(
                margin=ft.margin.only(top=21),
                alignment=ft.alignment.center,
                content=save_file_textfield
            ),
            ft.Container(
                height=50,
                alignment=ft.alignment.center,
                content=save_button
            ),
        ]
    )
    
    input = [
        file_input_container,
        sequence_listview_container,
        solve_button_container, 
        save_container    
    ]
    
    def file_input_clicked(e):
        input_token_field.value=""
        buffer_size_dropdown.value=""
        col_dropdown.value=""
        row_dropdown.value=""
        sequence_count_dropdown.value=""
        sequence_size_dropdown.value=""
        makeListEmpty(input)
        makeListEmpty(input_buttons)
        reward_text.value="Reward : "
        makeListEmpty(solution_path)
        input.append(file_input_container),
        input.append(sequence_listview_container),
        input.append(solve_button_container), 
        input.append(save_container), 
        resetProblem()
        input_buttons.append(
            ft.ElevatedButton(
                bgcolor=Blue,
                color=Black,
                text="File Input",
                width=200,
                on_click=file_input_clicked
            )
        )
        input_buttons.append(
            ft.ElevatedButton(
                bgcolor=Light_Black,
                color=Black,
                text="Manual Input",
                width=200,
                on_click=manual_input_clicked
            )
        )      
        page.update()
        
    def manual_input_clicked(e):
        file_name_input.value=""
        reward_text.value="Reward : "
        makeListEmpty(solution_path)
        makeListEmpty(input)
        makeListEmpty(input_buttons)
        input.append(manual_input_container),
        input.append(sequence_listview_container),
        input.append(solve_button_manual_container), 
        input.append(save_container), 
        resetProblem()
        input_buttons.append(
            ft.ElevatedButton(
                bgcolor=Light_Black,
                color=Black,
                text="File Input",
                width=200,
                on_click=file_input_clicked
            )
        )
        input_buttons.append(
            ft.ElevatedButton(
                bgcolor=Blue,
                color=Black,
                text="Manual Input",
                width=200,
                on_click=manual_input_clicked
            )
        )      
        page.update()
        
    input_buttons = [
        ft.ElevatedButton(
            bgcolor=Blue,
            color=Black,
            text="File Input",
            width=200,
            on_click=file_input_clicked
        ),
        ft.ElevatedButton(
            bgcolor=Light_Black,
            color=Black,
            text="Manual Input",
            width=200,
            on_click=manual_input_clicked
        )
    ]
    
    input_container = ft.Container(
        width=w//2,
        height=600,
        alignment=ft.alignment.top_center,
        content=ft.Column(
            alignment=ft.alignment.top_center,
            controls=[
                ft.Container( 
                    alignment=ft.alignment.top_center,
                    content=ft.Row(
                        alignment="CENTER",
                        controls=input_buttons
                    ),
                ),
                ft.Container(
                    content=ft.Column(
                        controls=input
                    )
                ),
            ]
        ),
    )

    output_container = ft.Container(
        width=w//2,
        content=ft.Column(
            controls=[
                ft.Container(
                    alignment=ft.alignment.center,
                    content=ft.Column(
                        controls=[
                            ft.Text("Matrix", size=40,color=Blue, font_family="Glitch",text_align="center",width=500),
                            ft.Container(
                                width=500,
                                height=500,
                                border_radius=5,
                                bgcolor=Black,
                                content=ft.Stack(
                                    # LOOP ROW
                                    controls=[
                                        ft.Column(
                                            alignment="SPACEAROUND",
                                            controls=widget_matrix_row_list
                                        ),
                                        cv.Canvas(
                                            [
                                                cv.Path(
                                                    solution_path,
                                                    paint=paint_canvas
                                                )
                                            ],
                                            width=float("inf"),
                                            expand=True,
                                        )
                                    ]   
                                )
                            ),
                            reward_text,
                        ]
                    )
                )
            ]
        )
    )
    
    row_main = ft.Row(
        alignment=ft.alignment.center,
        controls=[
            output_container,
            input_container
        ]
    )
    
    container = ft.Container(
        bgcolor=Black,
        width=w,
        height=h-58,
        content=ft.Column(
            controls=[
                row_title,
                row_main
            ]
        )
    )
    
    page.add(container)
    page.update
    pass

ft.app(target=main)