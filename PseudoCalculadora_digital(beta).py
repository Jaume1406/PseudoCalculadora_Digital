import tkinter as tk
import math


num1=1
num2=1
numbers=[num1,num2]
category_index=("Basic","Avançat","Trigonometria")
operations_index=(("Suma","Resta","Multiplicació","Divisió"),("Potencia","Arrel","Factorial","Factoritzar"))
selected_operation=["Basic","Suma",[0,0]]
basic_operations_symbols=("+","-","x","÷")

def validar_input(P):
    if P == "":
        return True
    try:
        float(P)
        return True
    except ValueError:
        return False
    
def operate():
    if selected_operation[0] == "Basic":
        if selected_operation[1]=="Suma":
            return suma()
        elif selected_operation[1]=="Resta":
            return resta()
        elif selected_operation[1]=="Multiplicació":
            return multiplicacio()
        else:
            return divisio()

#Operacions
def suma():
    return numbers[0]+numbers[1]

def resta():
    return numbers[0]-numbers[1]

def multiplicacio():
    return numbers[0]*numbers[1]

def divisio():
    return numbers[0]/numbers[1]


#Finestra
program=tk.Tk()
program.title("Pseudo-Calculadora Digital")
program.maxsize(800,500)
program.minsize(800,500)
program.configure(background="#FFFFF7")
float_block = program.register(validar_input)

#Funcions Menu
def menu_suma():
    selected_operation[2]=[0,0]
    change_operation()
def menu_resta():
    selected_operation[2]=[0,1]
    change_operation()
def menu_multiplicacio():
    selected_operation[2]=[0,2]
    change_operation()
def menu_divisio():
    selected_operation[2]=[0,3]
    change_operation()

#Menu

menu=tk.Menu(program)
program.config(menu=menu)

pricipal_menu=tk.Menu(menu,tearoff=1)
menu.add_cascade(label="Menu",menu=pricipal_menu)

basics_menu=tk.Menu(pricipal_menu,tearoff=0)
pricipal_menu.add_cascade(menu=basics_menu,label="Basics")

basics_menu.add_command(label="Suma",command=menu_suma)
basics_menu.add_command(label="Resta",command=menu_resta)
basics_menu.add_command(label="Multiplicació",command=menu_multiplicacio)
basics_menu.add_command(label="Divisió",command=menu_divisio)


#Text
operation_label = tk.Label(program, text= f"{selected_operation[0]}\n{selected_operation[1]}",font= "open_sans 25",background="#FFFFF7")
operation_label.place(x=400,y=0,anchor="n")
result_label = tk.Label(program,font="open_sans 50",background="#FFFFF7")
result_label.place(x=400,y=330,anchor="center")
operator_label=tk.Label(program,font="open_sans 50",background="#FFFFF7")

#Entrades
num_entry_1=tk.Entry(program,font="open_sans 50",width="4",justify="center",validate="key", validatecommand=(float_block, "%P"))
num_entry_1.insert(0,"1")
num_entry_2=tk.Entry(program,font="open_sans 50",width="4",justify="center",validate="key", validatecommand=(float_block, "%P"))
num_entry_2.insert(0,"1")
entries=(num_entry_1,num_entry_2)
#canvas
canvas=tk.Canvas()

# Funcions del canvas
def crear_linea(start:tuple,end:tuple):
    global line
    line = canvas.create_line(start[0], start[1], end[0], end[1], fill="black")

def eliminar_linea():
    canvas.delete(line)

# Funcions dels botons
def button_pressed():
    try:
        for n in range(len(numbers)):
            numbers[n]=float(entries[n].get())
        result_label["font"] = "open_sans 40"
        result_label["text"] = operate()
    except:
        result_label["text"] = "falten parametres"

def left_button_pressed():
    if selected_operation[2][1]-1 in range(len(operations_index[selected_operation[2][0]])):
        selected_operation[2][1]-=1
        change_operation()
    else:
        print("error")

def right_button_pressed():
    if selected_operation[2][1]+1 in range(len(operations_index[selected_operation[2][0]])):
        selected_operation[2][1]+=1
        change_operation()
    else:
        print("error")
    
        
#Botons
resolution_button = tk.Button(program,text="Resol", command = button_pressed,font="open_sans 25")
resolution_button.place(x=400,y=400,anchor="center")
left_buttom=tk.Button(program,text="<",font="open_sans 50",width=1,height=6,command=left_button_pressed)
left_buttom.place(x=0,y=250,anchor="w")
right_buttom=tk.Button(program,text=">",font="open_sans 50",width=1,height=6, command= right_button_pressed)
right_buttom.place(x=800,y=250,anchor="e")

#Funcions de canvi

def change_operation():
    selected_operation[0]=category_index[selected_operation[2][0]]
    selected_operation[1]=operations_index[selected_operation[2][0]][selected_operation[2][1]]
    operation_label["text"] = f"{selected_operation[0]}\n{selected_operation[1]}"
    if selected_operation[2][0]==0:
        operator_label.place(x=400,y=200,anchor="center")
        operator_label["text"] = basic_operations_symbols[selected_operation[2][1]]
        num_entry_1.place(x=250,y= 200,anchor="center")
        num_entry_2.place(x=550,y= 200,anchor="center")


change_operation()

program.mainloop()
