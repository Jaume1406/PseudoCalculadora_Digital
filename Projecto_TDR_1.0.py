import tkinter as tk
import math


num1=1
num2=1
numbers=[num1,num2]
category_index=("Basic","Avançat","Trigonometria")
operations_index=(("Suma","Resta","Multiplicació","Divisió"),("Potencia","Arrel","Factorial","Factoritzar"),("Teorema de pitagores","Def. Sinus","Def. Cosinus","Def. Tangent"))
selected_operation=["Basic","Suma",[0,0]]
symbols=("+","-","x","÷","√","X","α = X","α =")


def validar_input(P):
    if P == "":
        return True
    try:
        float(P)
        return True
    except ValueError:
        return False
    
def comprovate_entries(n_entries):
    try:
        for n in range(n_entries):
            numbers[n]=float(entries[n].get())
        return True
    except:
        result_label["text"]= "Falten Paràmetres"
        return False

def operate():
    if selected_operation[0] == "Basic":
        if comprovate_entries(2):
            if selected_operation[1]=="Suma":
                return suma()
            elif selected_operation[1]=="Resta":
                return resta()
            elif selected_operation[1]=="Multiplicació":
                return multiplicacio()
            else:
                return divisio()
    elif selected_operation[0]== "Avançat":
        if selected_operation[1]=="Potencia":
            if comprovate_entries(2):
                return potencia()
        elif selected_operation[1]=="Arrel":
            if comprovate_entries(2):
                return arrel()
        elif selected_operation[1]=="Factorial":
            if comprovate_entries(1):
                try:
                    numbers[0]=int(numbers[0])
                    return factorial()
                except:
                    return "Domes funciona amb números enters"
        else:
            if comprovate_entries(1):
                    if numbers[0]!=0:
                        return factoritzar()
                    else:
                        return 0
    elif selected_operation[0]=="Trigonometria":
        if selected_operation[1]=="Teorema de pitagores":
            if comprovate_entries(2):
                return t_pitagores()
        elif selected_operation[1]=="Def. Sinus":
            if comprovate_entries(2):
                return sinus()
        elif selected_operation[1]=="Def. Cosinus":
            if comprovate_entries(2):
                return cosinus()
        else:
            if comprovate_entries(2):
                return tangent()


#Operacions
def suma():
    return numbers[0]+numbers[1]

def resta():
    return numbers[0]-numbers[1]

def multiplicacio():
    return numbers[0]*numbers[1]

def divisio():
    return numbers[0]/numbers[1]

def potencia():
    return numbers[0]**numbers[1]

def arrel():
    return numbers[0]**(1/numbers[1])

def factorial():
    return math.factorial(numbers[0])

def prime_number(n:int):
    prime_nums= 0
    number=1
    prime_numbers_set=set()
    while prime_nums!=n:
        prime = True
        number+=1
        for value in prime_numbers_set:
            if number%value==0:
                prime = False
        if prime==True:
            prime_numbers_set.add(number)
            prime_nums+=1
    return number
            
def factoritzar(loops=1):
    prime_num=prime_number(loops)
    if numbers[0]==1:
        return 1
    elif numbers[0]%prime_num==0:
        numbers[0]/=prime_num
        return f"{prime_num},{factoritzar()}"
    else:
        return factoritzar(loops=loops+1)

def t_pitagores():
    if int(operate_option.get())==0:
        return math.sqrt((numbers[0]**2)+(numbers[1]**2))
    else:
        if numbers[0]>numbers[1]:
            return math.sqrt((numbers[0]**2)-(numbers[1]**2))
        else:
            return "La hipotenusa ha de ser major al catet"
    
def sinus():
    if int(operate_option.get())==0:
        if numbers[1]>numbers[0]:
            return f"sin α = {numbers[0]/numbers[1]}\nα = {math.asin(numbers[0]/numbers[1])}"
        else:
            return "La hipotenusa ha de ser major al catet"
    elif int(operate_option.get())==1:
        if numbers[1]>90 or numbers[1]<0:
            return "Angle imposible"
        else:
            return math.sin(numbers[1])*numbers[0]
    elif int(operate_option.get())==2:
        if numbers[1]>90 or numbers[1]<0:
            return "Angle imposible"
        else:
            return numbers[0]/(math.sin(numbers[1]))

def cosinus():
    if int(operate_option.get())==0:
        if numbers[1]>numbers[0]:
            return f"cos α = {numbers[0]/numbers[1]}\nα = {math.acos(numbers[0]/numbers[1])}"
        else:
            return "La hipotenusa ha de ser major al catet"
    elif int(operate_option.get())==1:
        if numbers[1]>90 or numbers[1]<0:
            return "Angle imposible"
        else:
            return math.cos(numbers[0])*numbers[1]
    else:
        if numbers[1]>90 or numbers[1]<0:
            return "Angle imposible"
        else:
            return numbers[1]/(math.cos(numbers[0]))
        
def tangent():
    if int(operate_option.get())==0:
        return f"tan α = {numbers[0]/numbers[1]}\nα = {math.atan(numbers[0]/numbers[1])}"
    elif int(operate_option.get())==1:
        if numbers[0]>90 or numbers[0]<0:
            return "Angle imposible"
        else:
            return math.tan(numbers[0])*numbers[1]
    else:
        if numbers[0]>90 or numbers[0]<0:
            return "Angle imposible"
        else:
            return numbers[1]/math.tan(numbers[0])
        
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

def menu_potencia():
    selected_operation[2]=[1,0]
    change_operation()

def menu_arrel():
    selected_operation[2]=[1,1]
    change_operation()

def menu_factorial():
    selected_operation[2]=[1,2]
    change_operation()

def menu_factoritzar():
    selected_operation[2]=[1,3]
    change_operation()

def menu_pitagores():
    selected_operation[2]=[2,0]
    change_operation()

def menu_sinus():
    selected_operation[2]=[2,1]
    change_operation()

def menu_cosinus():
    selected_operation[2]=[2,2]
    change_operation()

def menu_tangent():
    selected_operation[2]=[2,3]
    change_operation()

#canvas
canvas=tk.Canvas(program,width=400,height=250,background="#FFFFF7")

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

avançats_menu=tk.Menu(pricipal_menu,tearoff=0)
pricipal_menu.add_cascade(menu=avançats_menu,label="Avançat")

avançats_menu.add_command(label="Potencia",command=menu_potencia)
avançats_menu.add_command(label="Arrel",command=menu_arrel)
avançats_menu.add_command(label="Factorial",command=menu_factorial)
avançats_menu.add_command(label="Factoritzar",command=menu_factoritzar)

trigonometria_menu=tk.Menu(pricipal_menu,tearoff=0)
pricipal_menu.add_cascade(menu=trigonometria_menu,label="Trigonometria")

trigonometria_menu.add_command(label="Teorema de Pitagores",command=menu_pitagores)
trigonometria_menu.add_command(label="Definició de Sinus",command=menu_sinus)
trigonometria_menu.add_command(label="Definició de Cosinus",command=menu_cosinus)
trigonometria_menu.add_command(label="Definició de Tangent",command=menu_tangent)

#Text
operation_label = tk.Label(program, text= f"{selected_operation[0]}\n{selected_operation[1]}",font= "open_sans 25",background="#FFFFF7")
operation_label.place(x=400,y=0,anchor="n")
result_label = tk.Label(program,font="open_sans 40",background="#FFFFF7")
result_label.place(x=400,y=380,anchor="center")
operator_label=tk.Label(program,font="open_sans 50",background="#FFFFF7")
operator_label_2=tk.Label(program,font="open_sans 50",background="#FFFFF7")
operators_labels=(operator_label,operator_label_2)

#Entrades
num_entry_1=tk.Entry(program,font="open_sans 50",width="4",justify="center",validate="key", validatecommand=(float_block, "%P"))
num_entry_1.insert(0,"1")
num_entry_2=tk.Entry(program,font="open_sans 50",width="4",justify="center",validate="key", validatecommand=(float_block, "%P"))
num_entry_2.insert(0,"1")
entries=(num_entry_1,num_entry_2)





# Funcions del canvas
lines=[]
def crear_linea(start:tuple,end:tuple):
    lines.append(canvas.create_line(start[0], start[1], end[0], end[1], fill="black"))
    
    

def eliminate_lines():
    for line in lines:
        canvas.delete(line)

# Funcions dels botons

def button_pressed():
    try:
        result_label["text"] = operate()
    except:
        result_label["text"] = "error"
    if len(str(result_label["text"])) > 13:
        
        if (type(result_label["text"])==float or type(result_label["text"])==int):
            result_label["text"] = round(result_label["text"],2)
            if len(str(result_label["text"])) > 13:
                try:
                    result_label["font"] = "open_sans 50"
                    result_label["text"] = format(result_label["text"],".2E").replace("E", "x10^")
                except:
                    result_label["font"] = "open_sans 10"
            else:
                result_label["font"] = "open_sans 50"
        else:
            result_label["font"] = "open_sans 25"
    else:
        result_label["font"] = "open_sans 50"


def left_button_pressed():
    if selected_operation[2][1]-1 in range(len(operations_index[selected_operation[2][0]])):
        selected_operation[2][1]-=1
    else:
        if selected_operation[2][0]!=0:
            selected_operation[2][0]-=1
            selected_operation[2][1] = len(operations_index[selected_operation[2][0]])-1
        else:
            selected_operation[2][0] = len(operations_index)-1
            selected_operation[2][1] = len(operations_index[selected_operation[2][0]])-1
    change_operation()


def right_button_pressed():
    if selected_operation[2][1]+1 in range(len(operations_index[selected_operation[2][0]])):
        selected_operation[2][1]+=1
    else:
        if selected_operation[2][0]+1 > len(operations_index)-1:
            selected_operation[2][0] = 0
            selected_operation[2][1] = 0
        else:
            selected_operation[2][0] +=1
            selected_operation[2][1] = 0
    change_operation()
    
        
#Botons
resolution_button = tk.Button(program,text="Resol", command = button_pressed,font="open_sans 25")
resolution_button.place(x=400,y=450,anchor="center")
left_buttom=tk.Button(program,text="<",font="open_sans 50",width=1,height=6,command=left_button_pressed)
left_buttom.place(x=0,y=250,anchor="w")
right_buttom=tk.Button(program,text=">",font="open_sans 50",width=1,height=6, command= right_button_pressed)
right_buttom.place(x=800,y=250,anchor="e")

#Funcions de canvi

def change_operation():
    #Assignació
    selected_option = int(operate_option.get())
    selected_operation[0]=category_index[selected_operation[2][0]]
    selected_operation[1]=operations_index[selected_operation[2][0]][selected_operation[2][1]]
    operation_label["text"] = f"{selected_operation[0]}\n{selected_operation[1]}"
    operator_label["font"]="open_sans 50"
    #Treure els widgets
    for label in operators_labels:
        label.place_forget()
    eliminate_lines()
    canvas.place_forget()
    destroy_options()
    for entry in entries:
        entry["font"]="open_sans 50"
        entry.place_forget()
    
    #Basiques
    if selected_operation[2][0]==0:
        
        operator_label.place(x=400,y=200,anchor="center")
        operator_label["text"] = symbols[selected_operation[2][1]]
        num_entry_1.place(x=250,y= 200,anchor="center")
        num_entry_2.place(x=550,y= 200,anchor="center")
    #Avançades
    elif selected_operation[2][0]==1:
        if selected_operation[2][1]==0:
            num_entry_1.place(x=400,y=220,anchor="center")
            num_entry_2.place(x=420,y=150,anchor="center")
            num_entry_2["font"]="open_sans 25"
        elif selected_operation[2][1]==1:
            num_entry_1.place(x=420,y=220,anchor="center")
            num_entry_2.place(x=320,y=150,anchor="center")
            num_entry_2["font"]="open_sans 25"
            operator_label["text"]= symbols[4]
            operator_label.place(x=320,y= 220,anchor="center")
        else:
            num_entry_1.place(x=400,y=200,anchor="center")      
    #Trigonometria
    elif selected_operation[2][0]==2:
        if selected_operation[2][1]==0 or selected_operation[2][1]==1 or selected_operation[2][1]==2 or selected_operation[2][1]==3:
            operator_label["text"]=symbols[5]
            canvas.place(x=400,y=200,anchor="center")
            crear_linea((50,200),(350,200))
            crear_linea((350,200),(350,50))
            crear_linea((50,200),(350,50))
            num_entry_1["font"]="open_sans 25"
            num_entry_2["font"]="open_sans 25"
            operator_label["font"]="open_sans 25"
            operator_label_2["font"]="open_sans 25"
            if selected_operation[2][1]==0:
                create_options(("Hipotenusa","Catet"))
                place_options()
                if selected_option==0:
                    num_entry_1.place(x=400,y=300,anchor="center")
                    num_entry_2.place(x=600,y=200,anchor="center")
                    operator_label.place(x=370,y=170,anchor="center")
                else:
                    num_entry_2.place(x=400,y=300,anchor="center")
                    num_entry_1.place(x=350,y=160,anchor="center")
                    operator_label.place(x=580,y=200,anchor="center")
            elif selected_operation[2][1]==1:
                create_options(("Angle","Catet oposat","Hipotenusa"))
                place_options()
                if selected_option==0:
                    operator_label_2["text"]=symbols[6]
                    operator_label_2.place(x=250,y=100,anchor="center")
                    num_entry_1.place(x=600,y=200,anchor="center")
                    num_entry_2.place(x=350,y=160,anchor="center")
                elif selected_option==1:
                    operator_label_2["text"]=symbols[7]
                    operator_label_2.place(x=360,y=300,anchor="center")
                    operator_label.place(x=580,y=200,anchor="center")
                    num_entry_1.place(x=350,y=160,anchor="center")
                    num_entry_2.place(x=425,y=300,anchor="center")
                elif selected_option==2:
                    operator_label.place(x=370,y=170,anchor="center")
                    operator_label_2["text"]=symbols[7]
                    operator_label_2.place(x=360,y=300,anchor="center")
                    num_entry_1.place(x=600,y=200,anchor="center")
                    num_entry_2.place(x=425,y=300,anchor="center")
            elif selected_operation[2][1]==2:
                create_options(("Angle","Catet continu","Hipotenusa"))
                place_options()
                if selected_option==0:
                    operator_label_2["text"]=symbols[6]
                    operator_label_2.place(x=250,y=100,anchor="center")
                    num_entry_1.place(x=400,y=300,anchor="center")
                    num_entry_2.place(x=350,y=160,anchor="center")
                elif selected_option==1:
                    operator_label_2["text"]=symbols[7]
                    operator_label_2.place(x=180,y=100,anchor="center")
                    num_entry_2.place(x=350,y=160,anchor="center")
                    num_entry_1.place(x=260,y=100,anchor="center")
                    operator_label.place(x=400,y=300,anchor="center")
                else:
                    operator_label_2["text"]=symbols[7]
                    operator_label_2.place(x=180,y=100,anchor="center")
                    num_entry_1.place(x=260,y=100,anchor="center")
                    num_entry_2.place(x=400,y=300,anchor="center")
                    operator_label.place(x=350,y=160,anchor="center")
            else:
                create_options(("Angle","Catet oposat","Catet continu"))
                place_options()
                if selected_option==0:
                    operator_label_2["text"]=symbols[6]
                    operator_label_2.place(x=250,y=100,anchor="center")
                    num_entry_1.place(x=600,y=200,anchor="center")
                    num_entry_2.place(x=400,y=300,anchor="center")
                elif selected_option==1:
                    operator_label_2["text"]=symbols[7]
                    operator_label_2.place(x=250,y=100,anchor="center")
                    num_entry_1.place(x=330,y=100,anchor="center")
                    num_entry_2.place(x=400,y=300,anchor="center")
                    operator_label.place(x=580,y=200,anchor="center")
                else:
                    operator_label_2["text"]=symbols[7]
                    operator_label_2.place(x=250,y=100,anchor="center")
                    num_entry_1.place(x=330,y=100,anchor="center")
                    num_entry_2.place(x=600,y=200,anchor="center")
                    operator_label.place(x=400,y=300,anchor="center")

#Botons d'opció
operate_option=tk.StringVar(program,value=0)
radiobuttons=[]
options_index_namer_label=tk.Label(program,background="#FFFFF7",font="open_sans 25",text="Incognita:")

def create_options(options_names:tuple):
    for n in range(len(options_names)):
        radiobuttons.append(tk.Radiobutton(program, text=options_names[n],font="open_sans 15",variable=operate_option, value=n,command=change_operation,background="#FFFFF7"))

def place_options(text="Incognita"):
    options_index_namer_label["text"]=text
    y_pos=450
    for option in reversed(radiobuttons):
        option.place(x=50,y=y_pos,anchor="w")
        y_pos-=50
    options_index_namer_label.place(x=50,y=y_pos,anchor="w")

def destroy_options():
    global radiobuttons
    for option in radiobuttons:
        option.place_forget()
    options_index_namer_label.place_forget()
    radiobuttons=[]





change_operation()

program.mainloop()