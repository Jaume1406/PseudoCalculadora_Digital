import tkinter as tk
import math


num1=1
num2=1
numbers=[num1,num2]
category_index=("Bàsic","Avançat","Trigonometria","Geometria")
operations_index=(("Suma","Resta","Multiplicació","Divisió"),("Potencia","Arrel","Factorial","Factoritzar"),("Teorema de Pitàgores","Def. Sinus","Def. Cosinus","Def. Tangent","Sinus","Cosinus","Tangent","Arcsinus","Arcosinus","Arctangent"),("Triangle","Quadrilàter","Poligon regular","Circumferència"))
selected_operation=["Basic","Suma",[0,0]]
symbols=("+","-","x","÷","√","X","α = X","α =          °","Sin(        )","Cos(        )","Tan(        )","ArcSin(        )","ArcCos(        )","ArcTan(        )")


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
    
def comprovate_positive_entries(n_entries):
    try:
        for n in range(n_entries):
            numbers[n]=float(entries[n].get())
            if not numbers[n]>0:
                result_label["text"]= "Han de ser nombres positius majors a zero"
                return False
                continue
        return True
    except:
        result_label["text"]= "Falten Paràmetres"
        return False
    
def operate():
    if selected_operation[0] == "Bàsic":
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
                if numbers[0]-int(numbers[0])==0 and numbers[0]>=0:
                    numbers[0]=int(numbers[0])
                    return factorial()
                else:
                    return "Domes funciona amb nombres naturals (positius i enters)"
        else:
            if comprovate_entries(1):
                    if numbers[0]>=0 and numbers[0]-int(numbers[0])==0:
                        if numbers[0]!=0:
                            return factoritzar()
                        else:
                            return 0
                    else:
                        return "Domes funciona amb nombres naturals (positius i enters)"
    elif selected_operation[0]=="Trigonometria":
        if selected_operation[1]=="Teorema de Pitàgores":
            if comprovate_entries(2):
                return t_pitagores()
        elif selected_operation[1]=="Def. Sinus":
            if comprovate_entries(2):
                return def_sinus()
        elif selected_operation[1]=="Def. Cosinus":
            if comprovate_entries(2):
                return def_cosinus()
        elif selected_operation[1]=="Def. Tangent":
            if comprovate_entries(2):
                return def_tangent()
        elif selected_operation[1]=="Sinus":
            if comprovate_entries(1):
                return sinus()
        elif selected_operation[1]=="Cosinus":
            if comprovate_entries(1):
                return cosinus()
        elif selected_operation[1]=="Tangent":
            if comprovate_entries(1):
                return tangent()
        elif selected_operation[1]=="Arcsinus":
            if comprovate_entries(1):
                return arcsinus()
        elif selected_operation[1]=="Arcosinus":
            if comprovate_entries(1):
                return arcosinus()
        elif selected_operation[1]=="Arctangent":
            if comprovate_entries(1):
                return arctangent()
    else:
        if selected_operation[1]=="Triangle":
            if int(operate_option.get())==0:
                if comprovate_positive_entries(1):
                    return triangle()
            else:
                if comprovate_positive_entries(2):
                    return triangle()
        elif selected_operation[1]=="Quadrilàter":
            if int(operate_option.get())==0:
                if comprovate_positive_entries(1):
                    return quadrilater()
            else:
                if comprovate_positive_entries(2):
                    return quadrilater()
        elif selected_operation[1]=="Poligon regular":
            if comprovate_positive_entries(2):
                if numbers[1]-int(numbers[1])==0 and numbers[1]>=3:
                    return poligon_regular()
                else:
                    return "Es necessiten un mínim de 3 costats\nper formar una figura tancada, el nombre ha de ser enter"
        else:
            if comprovate_positive_entries(1):
                return circumferencia()



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
    
def def_sinus():
    if int(operate_option.get())==0:
        if numbers[1]>numbers[0]:
            result = math.asin(numbers[0]/numbers[1])
            return f"sin α = {numbers[0]/numbers[1]}\nα = {result} Rad\nα = {round(math.degrees(result))} Deg"
        else:
            return "La hipotenusa ha de ser major al catet"
    elif int(operate_option.get())==1:
        if numbers[1]>=90 or numbers[1]<0:
            return "Angle imposible"
        else:
            return math.sin(math.radians(numbers[1]))*numbers[0]
    elif int(operate_option.get())==2:
        if numbers[1]>=90 or numbers[1]<0:
            return "Angle imposible"
        else:
            return numbers[0]/(math.sin(math.radians(numbers[1])))

def def_cosinus():
    if int(operate_option.get())==0:
        if numbers[1]>numbers[0]:
            result = math.acos(numbers[0]/numbers[1])
            return f"Cos α = {numbers[0]/numbers[1]}\nα = {result} Rad\nα = {round(math.degrees(result))} Deg"
        else:
            return "La hipotenusa ha de ser major al catet"
    elif int(operate_option.get())==1:
        if numbers[1]>=90 or numbers[1]<0:
            return "Angle imposible"
        else:
            return math.cos(math.radians(numbers[0]))*numbers[1]
    else:
        if numbers[1]>=90 or numbers[1]<0:
            return "Angle imposible"
        else:
            return numbers[1]/(math.cos(math.radians(numbers[0])))
        
def def_tangent():
    if int(operate_option.get())==0:
        result = math.atan(numbers[0]/numbers[1])
        return f"Tan α = {numbers[0]/numbers[1]}\nα = {result} Rad\nα = {round(math.degrees(result))} Deg"
    elif int(operate_option.get())==1:
        if numbers[0]>90 or numbers[0]<0:
            return "Angle imposible"
        else:
            return math.tan(math.radians(numbers[0]))*numbers[1]
    else:
        if numbers[0]>90 or numbers[0]<0:
            return "Angle imposible"
        else:
            return numbers[1]/math.tan(math.radians(numbers[0]))

def sinus():
    if int(operate_option.get())==0:
        return math.sin(math.radians(numbers[0]))
    else:
        return math.sin(numbers[0])

def cosinus():
    if int(operate_option.get())==0:
        return math.cos(math.radians(numbers[0]))
    else:
        return math.cos(numbers[0])
    
def tangent(): 
    if int(operate_option.get())==0:
        if numbers[0]!=90 and numbers[0]!=270:
            return math.tan(math.radians(numbers[0]))
        else:
            return "No existeix la tangent de 90 i 270 graus"
    else:
        if numbers[0]!=math.pi/2 and numbers!=(math.pi*3)/2:
            return math.tan(numbers[0])
        else:
            return "No existeix la tangent de 𝜋/2 i 3𝜋/2 radians"
    
def arcsinus():
    if not (numbers[0]>1 or numbers[0]<-1):
        result=math.asin(numbers[0])
        return f"α = {result} Rad\nα = {round(math.degrees(result))} Deg"
    else:
        return "La funció sinus domes pot ser Sin(α)=n\nn∈[-1,1]"

def arcosinus():
    if not (numbers[0]>1 or numbers[0]<-1):
        result=math.acos(numbers[0])
        return f"α = {result} Rad\nα = {round(math.degrees(result))} Deg"
    else:
        return "La funció cosinus domes pot ser Cos(α)=n\nn∈[-1,1]"

def arctangent():
    result=math.atan(numbers[0])
    return f"α = {result} Rad\nα = {round(math.degrees(result))} Deg"

def triangle():
    if int(operate_option.get())==0:
        perimeter=numbers[0]*3
        higth=math.sqrt((numbers[0]**2)+((numbers[0]/2)**2))
        area=(numbers[0]*higth)/2
        return f"Perímetre={perimeter} ud\nÀrea={round(area,2)} ud^2"
    else:
        perimeter=numbers[0]*3
        higth=numbers[1]
        area=(numbers[0]*higth)/2
        return f"Perímetre={perimeter} ud\nÀrea={area} ud^2"

def quadrilater():
    if int(operate_option.get())==0:
        perimeter=numbers[0]*4
        area=numbers[0]**2
        return f"Perímetre={perimeter} ud\nÀrea={area} ud^2"
    else:
        perimeter=numbers[0]*2+numbers[1]*2
        area=numbers[0]*numbers[1]
        return f"Perímetre={perimeter} ud\nÀrea={area} ud^2"

def poligon_regular():
    perimeter=numbers[0]*numbers[1]
    angle=(360/numbers[1])/2
    apotema=(numbers[0]/2)/(math.tan(math.radians(angle)))
    area=(numbers[0]*apotema/2)*numbers[1]
    return f"Perímetre={perimeter} ud\nÀrea={round(area,2)} ud^2"

def circumferencia():
    perimeter = 2*math.pi*numbers[0]
    area = math.pi*(numbers[0]**2)
    return f"Perímetre={perimeter} ud\nÀrea={area} ud^2"

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

def menu_def_sinus():
    selected_operation[2]=[2,1]
    change_operation()

def menu_def_cosinus():
    selected_operation[2]=[2,2]
    change_operation()

def menu_def_tangent():
    selected_operation[2]=[2,3]
    change_operation()

def menu_sinus():
    selected_operation[2]=[2,4]
    change_operation()

def menu_cosinus():
    selected_operation[2]=[2,5]
    change_operation()

def menu_tangent():
    selected_operation[2]=[2,6]
    change_operation()

def menu_arcsinus():
    selected_operation[2]=[2,7]
    change_operation()

def menu_arcosinus():
    selected_operation[2]=[2,8]
    change_operation()

def menu_arctangent():
    selected_operation[2]=[2,9]
    change_operation()

def menu_triangle():
    selected_operation[2]=[3,0]
    change_operation()

def menu_quadrilater():
    selected_operation[2]=[3,1]
    change_operation()

def menu_poligon_regular():
    selected_operation[2]=[3,2]
    change_operation()

def menu_circumferencia():
    selected_operation[2]=[3,3]
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

teoremes_definicions_trigonometria_menu=tk.Menu(trigonometria_menu,tearoff=0)
trigonometria_menu.add_cascade(menu=teoremes_definicions_trigonometria_menu,label="Teoremes i definicions")


teoremes_definicions_trigonometria_menu.add_command(label="Teorema de Pitàgores",command=menu_pitagores)
teoremes_definicions_trigonometria_menu.add_command(label="Definició de Sinus",command=menu_def_sinus)
teoremes_definicions_trigonometria_menu.add_command(label="Definició de Cosinus",command=menu_def_cosinus)
teoremes_definicions_trigonometria_menu.add_command(label="Definició de Tangent",command=menu_def_tangent)

trigonometria_menu.add_command(label="Sinus",command=menu_sinus)
trigonometria_menu.add_command(label="Cosinus",command=menu_cosinus)
trigonometria_menu.add_command(label="Tangent",command=menu_tangent)
trigonometria_menu.add_command(label="Arcsinus",command=menu_arcsinus)
trigonometria_menu.add_command(label="Arcosinus",command=menu_arcosinus)
trigonometria_menu.add_command(label="Arctangent",command=menu_arctangent)

geometria_menu=tk.Menu(pricipal_menu,tearoff=0)
pricipal_menu.add_cascade(menu=geometria_menu,label="Geometria")

geometria_menu.add_command(label="Triangle",command=menu_triangle)
geometria_menu.add_command(label="Quadrilàter",command=menu_quadrilater)
geometria_menu.add_command(label="Poligon regular",command=menu_poligon_regular)
geometria_menu.add_command(label="Circumferència",command=menu_circumferencia)


#Text
operation_label = tk.Label(program, text= f"{selected_operation[0]}\n{selected_operation[1]}",font= "open_sans 25",background="#FFFFF7")
operation_label.place(x=400,y=0,anchor="n")
result_label = tk.Label(program,font="open_sans 40",background="#FFFFF7")
result_label.place(x=400,y=375,anchor="center")
operator_label_1=tk.Label(program,font="open_sans 50",background="#FFFFF7")
operator_label_2=tk.Label(program,font="open_sans 50",background="#FFFFF7")
operators_labels=(operator_label_1,operator_label_2)

#Entrades
num_entry_1=tk.Entry(program,font="open_sans 50",width="4",justify="center",validate="key", validatecommand=(float_block, "%P"))
num_entry_1.insert(0,"1")
num_entry_2=tk.Entry(program,font="open_sans 50",width="4",justify="center",validate="key", validatecommand=(float_block, "%P"))
num_entry_2.insert(0,"1")
num_entry_3=tk.Entry(program,font="open_sans 50",width="4",justify="center",validate="key", validatecommand=(float_block, "%P"))
num_entry_3.insert(0,"1")
entries=(num_entry_1,num_entry_2,num_entry_3)





# Funcions del canvas
lines=[]
def crear_linea(start:tuple,end:tuple,color="black"):
    lines.append(canvas.create_line(start[0], start[1], end[0], end[1], fill=color))
    
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
            result_label["font"] = "open_sans 18"
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
    result_label["text"]=""
    selected_option = int(operate_option.get())
    selected_operation[0]=category_index[selected_operation[2][0]]
    selected_operation[1]=operations_index[selected_operation[2][0]][selected_operation[2][1]]
    operation_label["text"] = f"{selected_operation[0]}\n{selected_operation[1]}"

    #Treure els widgets
    for label in operators_labels:
        label["font"]="open_sans 50"
        label.place_forget()
    eliminate_lines()
    canvas.place_forget()
    destroy_options()
    for entry in entries:
        entry["font"]="open_sans 50"
        entry.place_forget()
    #Basiques
    if selected_operation[2][0]==0:
        
        operator_label_1.place(x=400,y=200,anchor="center")
        operator_label_1["text"] = symbols[selected_operation[2][1]]
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
            operator_label_1["text"]= symbols[4]
            operator_label_1.place(x=320,y= 220,anchor="center")
        else:
            num_entry_1.place(x=400,y=200,anchor="center")      
    #Trigonometria
    elif selected_operation[2][0]==2:
        if selected_operation[2][1]==0 or selected_operation[2][1]==1 or selected_operation[2][1]==2 or selected_operation[2][1]==3:
            operator_label_1["text"]=symbols[5]
            canvas.place(x=400,y=200,anchor="center")
            crear_linea((50,200),(350,200))
            crear_linea((350,200),(350,50))
            crear_linea((50,200),(350,50))
            num_entry_1["font"]="open_sans 25"
            num_entry_2["font"]="open_sans 25"
            operator_label_1["font"]="open_sans 25"
            operator_label_2["font"]="open_sans 25"
            if selected_operation[2][1]==0:
                create_options(("Hipotenusa","Catet"))
                place_options()
                if selected_option==0:
                    num_entry_1.place(x=400,y=300,anchor="center")
                    num_entry_2.place(x=600,y=200,anchor="center")
                    operator_label_1.place(x=370,y=170,anchor="center")
                else:
                    num_entry_2.place(x=400,y=300,anchor="center")
                    num_entry_1.place(x=350,y=160,anchor="center")
                    operator_label_1.place(x=580,y=200,anchor="center")
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
                    operator_label_2.place(x=330,y=300,anchor="w")
                    operator_label_1.place(x=580,y=200,anchor="center")
                    num_entry_1.place(x=350,y=160,anchor="center")
                    num_entry_2.place(x=425,y=300,anchor="center")
                elif selected_option==2:
                    operator_label_1.place(x=370,y=170,anchor="center")
                    operator_label_2["text"]=symbols[7]
                    operator_label_2.place(x=330,y=300,anchor="w")
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
                    operator_label_2.place(x=160,y=100,anchor="w")
                    num_entry_2.place(x=350,y=160,anchor="center")
                    num_entry_1.place(x=260,y=100,anchor="center")
                    operator_label_1.place(x=400,y=300,anchor="center")
                else:
                    operator_label_2["text"]=symbols[7]
                    operator_label_2.place(x=160,y=100,anchor="w")
                    num_entry_1.place(x=260,y=100,anchor="center")
                    num_entry_2.place(x=400,y=300,anchor="center")
                    operator_label_1.place(x=350,y=160,anchor="center")
            elif selected_operation[2][1]==3:
                create_options(("Angle","Catet oposat","Catet continu"))
                place_options()
                if selected_option==0:
                    operator_label_2["text"]=symbols[6]
                    operator_label_2.place(x=250,y=100,anchor="center")
                    num_entry_1.place(x=600,y=200,anchor="center")
                    num_entry_2.place(x=400,y=300,anchor="center")
                elif selected_option==1:
                    operator_label_2["text"]=symbols[7]
                    operator_label_2.place(x=230,y=100,anchor="w")
                    num_entry_1.place(x=330,y=100,anchor="center")
                    num_entry_2.place(x=400,y=300,anchor="center")
                    operator_label_1.place(x=580,y=200,anchor="center")
                else:
                    operator_label_2["text"]=symbols[7]
                    operator_label_2.place(x=230,y=100,anchor="w")
                    num_entry_1.place(x=330,y=100,anchor="center")
                    num_entry_2.place(x=600,y=200,anchor="center")
                    operator_label_1.place(x=400,y=300,anchor="center")
        elif selected_operation[2][1]==4 or selected_operation[2][1]==5 or selected_operation[2][1]==6:
            create_options(("Graus (DEG)","Radians (RAD)"))
            place_options("Unitat")
            operator_label_1.place(x=280,y=200,anchor="w")
            if selected_operation[2][1]==4:
                num_entry_1.place(x=480,y=200,anchor="center")
                operator_label_1["text"]=symbols[8]
            elif selected_operation[2][1]==5:
                num_entry_1.place(x=500,y=200,anchor="center")
                operator_label_1["text"]=symbols[9]
            elif selected_operation[2][1]==6:
                num_entry_1.place(x=500,y=200,anchor="center")
                operator_label_1["text"]=symbols[10]
        elif selected_operation[2][1]==7:
            operator_label_1["text"]=symbols[11]
            operator_label_1.place(x=230,y=200,anchor="w")
            num_entry_1.place(x=530,y=200,anchor="center")
        elif selected_operation[2][1]==8:
            operator_label_1["text"]=symbols[12]
            operator_label_1.place(x=230,y=200,anchor="w")
            num_entry_1.place(x=550,y=200,anchor="center")
        elif selected_operation[2][1]==9:
            operator_label_1["text"]=symbols[13]
            operator_label_1.place(x=230,y=200,anchor="w")
            num_entry_1.place(x=550,y=200,anchor="center")
    else:
        if selected_operation[2][1]==0:
            create_options(("equilàter (Costats iguals)","qualsevol"))
            place_options("Tipus")
            num_entry_1.place(x=400,y=300,anchor="center")
            canvas.place(x=400,y=200,anchor="center")
            num_entry_1["font"]="open_sans 25"
            if int(operate_option.get())==0:
                crear_linea((200,50),(300,200))
                crear_linea((300,200),(100,200))
                crear_linea((100,200),(200,50))
            
            else:
                crear_linea((200,50),(350,200))
                crear_linea((350,200),(50,200))
                crear_linea((50,200),(200,50))
                crear_linea((200,50),(200,200),color="grey")
                num_entry_2["font"]="open_sans 25"
                num_entry_2.place(x=600,y=200,anchor="center")
                operator_label_1["font"]="open_sans 25"
                operator_label_1["text"]="h"
                operator_label_1.place(x=410,y=200)
                operator_label_2["font"]="open_sans 25"
                operator_label_2["text"]="h="
                operator_label_2.place(x=530,y=200,anchor="center")
        elif selected_operation[2][1]==1:
            create_options(("Quadrat","Rectangle"))
            place_options("Tipus")
            num_entry_1["font"]="open_sans 25"
            num_entry_1.place(x=400,y=300,anchor="center")
            canvas.place(x=400,y=200,anchor="center")
            if int(operate_option.get())==0:
                crear_linea((125,50),(275,50))
                crear_linea((275,50),(275,200))
                crear_linea((275,200),(125,200))
                crear_linea((125,200),(125,50))
            else:
                num_entry_2["font"]="open_sans 25"
                num_entry_2.place(x=550,y=200,anchor="center")  
                crear_linea((100,50),(300,50))
                crear_linea((300,50),(300,200))
                crear_linea((300,200),(100,200))
                crear_linea((100,200),(100,50))
        elif selected_operation[2][1]==2:
            canvas.place(x=500,y=200,anchor="center")
            num_entry_1["font"]="open_sans 25"
            num_entry_1.place(x=370,y=150,anchor="center")
            num_entry_2["font"]="open_sans 25"
            num_entry_2.place(x=370,y=250,anchor="center")
            operator_label_1["font"]="open_sans 25"
            operator_label_2["font"]="open_sans 25"
            operator_label_1["text"]="mida dels costats"
            operator_label_2["text"]="n de costats"
            operator_label_1.place(x=320,y=150,anchor="e")
            operator_label_2.place(x=320,y=250,anchor="e")
            #triangle
            crear_linea((200,50),(225,100))
            crear_linea((175,100),(225,100))
            crear_linea((200,50),(175,100))
            #quadrat
            crear_linea((150,150),(200,150))
            crear_linea((200,150),(200,200))
            crear_linea((150,200),(200,200))
            crear_linea((150,150),(150,200))
            #hexagon
            crear_linea((300,155),(330,155))
            crear_linea((330,155),(350,125))
            crear_linea((350,125),(330,95))
            crear_linea((330,95),(300,95))
            crear_linea((300,95),(280,125))
            crear_linea((280,125),(300,155))


        else:
            canvas.place(x=400,y=200,anchor="center")
            num_entry_1["font"]="open_sans 25"
            num_entry_1.place(x=440,y=225,anchor="center")
            crear_linea((200,125),(300,125))
            lines.append(canvas.create_oval(100,25,300,225))
            

         
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
