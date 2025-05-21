import tkinter

button_values = [
    ["AC", "+/-", "%", "÷"], 
    ["7", "8", "9", "×"], 
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["0", ".", "√", "="]
]

right_symbols = ["÷", "×", "-", "+", "="]
top_symbols = ["AC", "+/-", "%"]

row_count = len(button_values) #5
column_count = len(button_values[0]) #4

color_light_gray = "#D4D4D4"
color_black = "#000000"
color_dark_gray = "#A9A9A9"
color_orange = "#FF9500"
color_white = "white"

#window setup
window = tkinter.Tk() #create a window
window.title("Calculator") #set the title
window.resizable(False, False)

frame = tkinter.Frame(window) #create a frame
label = tkinter.Label(frame, text="0", font=("Arial", 45), background=color_black, 
                      foreground=color_white, anchor="e" ,width=column_count)

label.grid(row=0, column=0, columnspan=column_count, sticky="we")

for row in range(row_count):
    for column in range(column_count):
        value = button_values[row][column]
        button = tkinter.Button(frame, text=value, font=("Arial", 30),
                                width=column_count-1, height=1,
                                command=lambda value=value: button_click(value))
        if value in top_symbols:
            button.config(foreground=color_black, background=color_dark_gray)
        elif value in right_symbols:
            button.config(foreground=color_white, background=color_orange)
        else:
            button.config(foreground=color_white, background=color_black)

        button.grid(row=row+1, column=column)

frame.pack()

#A+B, A*B, A-B, A/B
A = "0"
operation = None
B = None

def clear_all():
    global A, operation, B
    A = "0"
    operation = None
    B = None

def remove_zero_decimal(num):
    if num % 1 == 0:
        num = int(num)
    return str(num)    

def button_click(value):
    global right_symbols, top_symbols , label, A, B, operation

    if value in right_symbols:
        if value == "=":
            if A is not None and operation is not None:
                B = label["text"]
                numA = float(A)
                numB = float(B)

                if operation == "+":
                    label["text"] = remove_zero_decimal(numA + numB)
                elif operation == "-":
                    label["text"] = remove_zero_decimal(numA - numB)
                elif operation == "×":
                    label["text"] = remove_zero_decimal(numA * numB)
                elif operation == "÷":
                    label["text"] = remove_zero_decimal(numA / numB)

                clear_all()    

        elif value in "+-×÷":
            if operation is None:
                A = label["text"]
                label["text"] = "0"
                B = None

            operation = value

    elif value in top_symbols:
        if value == "AC":
            clear_all()
            label["text"] = "0"

        elif value == "+/-":
            result = float(label["text"]) * -1
            label["text"] = remove_zero_decimal(result)

        elif value == "%":
            result = float(label["text"]) / 100
            label["text"] = remove_zero_decimal(result)

    else: #digits or .
        if value == ".":
            if value not in label["text"]:
                label["text"] += value
        elif value in "0123456789":
            if label["text"] == "0":
                label["text"] = value #replace 0
            else:
                label["text"] += value #append digit

#center the window
window.update() #update window with new size dimensions
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

window_x = int((screen_width/2) - (window_width/2))
window_y = int((screen_height/2) - (window_height/2))

#format "(w)x(h)+(x)+(y)"
window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")

window.mainloop()