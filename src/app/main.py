import tkinter
from tkinter import *
from colors import Colores as color

application = Tk()
application.title("Calculadora")
application.geometry("300x490")
application.config(bg=color.backColor)


frameScreen = Frame(application, width=300, height=84)
frameScreen.grid(row=0, column=0)
frameScreen.config(bg=color.alphaColor)


frameBody = Frame(application, width=300, height=450)
frameBody.grid(row=1, column=0)
frameBody.config(bg=color.backColor)


values = ''
operatorValues= ''
recordOperatorValue = []
last = ''
listSimbols = ["+","-","/","*","%"]
number = ''
recordAllvalues= ''
next = ''
textValue = StringVar()
verifyLastOperator = ''

def operator(event):
    global values, recordOperatorValue, last, next, operatorValues, number,recordAllvalues, verifyLastOperator
    number += event 
    recordOperatorValue += event
    operatorValues = event

    try:
        next = recordOperatorValue[- 1]
    except:
        pass
    try:
        last = recordOperatorValue[-2]
    except:
        pass
    
    if verifyLastOperator in listSimbols:
            size = len(values)
            values = values[:size - 1] 
            verifyLastOperator = ''

    if next in listSimbols: 
        if recordAllvalues in listSimbols:  
            if last in listSimbols:
                size = len(values)
                values = values[:size - 1] 
        values += operatorValues     
        textValue.set(values)
        recordAllvalues = number[-1::] 
   
def cleanInput(event):
    global values, result,recordAllvalues, number, verifyLastOperator, last, next
    
    if values != '':
        try:
            s = len(number)
            verifyLastOperator = values[-2]
            last = ''
        except:
            pass
        next = ''
        recordAllvalues = ''
        size = len(values)
        values = values[:size - 1]  
        textValue.set(values [:size - 1])
       
        
def teste(event):
    global values, recordOperatorValue, last, next, operatorValues, number,recordAllvalues, verifyLastOperator
    print('teste')

def inputDate(event):
    global values, number,recordAllvalues, verifyLastOperator
    values += str(event)  
    number += event 
    recordAllvalues = number[-1::]  
    verifyLastOperator = ''
    textValue.set(values)
 
def calculate(event):
    global values, operatorValues, next, last,recordOperatorValue
    try:
        result = eval(values)
        textValue.set(result)
        operatorValues = ''
        next = ''
        last= ''
        recordOperatorValue = ''
        values = str(result)
    except:
        pass
    
def cleanAllInput(event):
    global values, operatorValues, next, last,recordOperatorValue, verifyLastOperator, number
    values = ''
    textValue.set(values)
    operatorValues = ''
    next = ''
    last= ''
    recordOperatorValue = ''
    verifyLastOperator = ''
    number = ''


appLabel = Label(frameScreen, textvariable=textValue, width=16, height=3, padx=7, relief=FLAT, anchor="e", justify=RIGHT, font=('Arial',22,'bold'), bg=color.alphaColor, fg=color.textColor)
appLabel.place(x=0,y=0)




#-------------------------------------------------------
btnPorcen= Button(frameBody, command= lambda: operator('%'), text="%", width=8, height=4, relief=RAISED, overrelief=RIDGE, bg=color.btnColor, fg=color.textColor, font=('Arial',9,'bold'))
btnPorcen.place(x=12,y=15)
btnClearAll= Button(frameBody,command= lambda: cleanAllInput(''), text="CE", width=8, height=4,relief=RAISED, overrelief=RIDGE, bg=color.btnColor, fg=color.textColor, font=('Arial',9,'bold'))
btnClearAll.place(x=82,y=15)
btnBackSpace= Button(frameBody,command= lambda: cleanInput(''), text="<x",width=8, height=4,relief=RAISED, overrelief=RIDGE, bg=color.btnColor, fg=color.textColor, font=('Arial',9,'bold'))
btnBackSpace.place(x=152,y=15)
btnDivison= Button(frameBody,command= lambda: operator('/'), text="/",width=8, height=4,relief=RAISED, overrelief=RIDGE, bg=color.btnColor, fg=color.textColor, font=('Arial',9,'bold'))
btnDivison.place(x=222,y=15)

#-------------------------------------------------------
btn7= Button(frameBody,  command= lambda: inputDate('7'), text="7",width=8, height=4,relief=RAISED, overrelief=RIDGE, bg=color.btnColor, fg=color.textColor, font=('Arial',9,'bold'))
btn7.place(x=12,y=90)
btn8= Button(frameBody,command= lambda: inputDate('8'), text="8",width=8, height=4,relief=RAISED, overrelief=RIDGE, bg=color.btnColor, fg=color.textColor, font=('Arial',9,'bold'))
btn8.place(x=82,y=90)
btn9= Button(frameBody,command= lambda: inputDate('9'), text="9",width=8, height=4,relief=RAISED, overrelief=RIDGE, bg=color.btnColor, fg=color.textColor, font=('Arial',9,'bold'))
btn9.place(x=152,y=90)
btnMutiplication= Button(frameBody,command= lambda: operator('*'), text="X",width=8, height=4,relief=RAISED, overrelief=RIDGE, bg=color.btnColor, fg=color.textColor, font=('Arial',9,'bold'))
btnMutiplication.place(x=222,y=90)
#----------------------------------------------------
btn4= Button(frameBody,command= lambda: inputDate('4'), text="4",width=8, height=4,relief=RAISED, overrelief=RIDGE, bg=color.btnColor, fg=color.textColor, font=('Arial',9,'bold'))
btn4.place(x=12,y=165)
btn5= Button(frameBody,command= lambda: inputDate('5'), text="5",width=8, height=4,relief=RAISED, overrelief=RIDGE, bg=color.btnColor, fg=color.textColor, font=('Arial',9,'bold'))
btn5.place(x=82,y=165)
btn6= Button(frameBody,command= lambda: inputDate('6'), text="6",width=8, height=4,relief=RAISED, overrelief=RIDGE, bg=color.btnColor, fg=color.textColor, font=('Arial',9,'bold'))
btn6.place(x=152,y=165)
btnSubtract= Button(frameBody,command= lambda: operator('-'), text="-",width=8, height=4,relief=RAISED, overrelief=RIDGE, bg=color.btnColor, fg=color.textColor, font=('Arial',9,'bold'))
btnSubtract.place(x=222,y=165)
#---------------------------------------------------
btn1= Button(frameBody,command= lambda: inputDate('1'), text="1",width=8, height=4,relief=RAISED, overrelief=RIDGE, bg=color.btnColor, fg=color.textColor, font=('Arial',9,'bold'))
btn1.place(x=12,y=240)
btn2= Button(frameBody,command= lambda: inputDate('2'), text="2",width=8, height=4,relief=RAISED, overrelief=RIDGE, bg=color.btnColor, fg=color.textColor, font=('Arial',9,'bold'))
btn2.place(x=82,y=240)
btn3= Button(frameBody,command= lambda: inputDate('3'), text="3",width=8, height=4,relief=RAISED, overrelief=RIDGE, bg=color.btnColor, fg=color.textColor, font=('Arial',9,'bold'))
btn3.place(x=152,y=240)
btnAdd= Button(frameBody,command= lambda: operator('+'), text="+",width=8, height=4,relief=RAISED, overrelief=RIDGE, bg=color.btnColor, fg=color.textColor, font=('Arial',9,'bold'))
btnAdd.place(x=222,y=240)
#--------------------------------------------------
btnNothing= Button(frameBody,command= lambda: teste(), text=" ",width=8, height=4,relief=RAISED, overrelief=RIDGE, bg=color.btnColor, fg=color.textColor, font=('Arial',9,'bold'))
btnNothing.place(x=12,y=315)
btn0= Button(frameBody,command= lambda: inputDate('0'), text="0",width=8, height=4,relief=RAISED, overrelief=RIDGE, bg=color.btnColor, fg=color.textColor, font=('Arial',9,'bold'))
btn0.place(x=82,y=315)
btnVirgula= Button(frameBody,command= lambda: inputDate('.'), text=",",width=8, height=4,relief=RAISED, overrelief=RIDGE, bg=color.btnColor, fg=color.textColor, font=('Arial',9,'bold'))
btnVirgula.place(x=152,y=315)
btnIgual= Button(frameBody,command= lambda: calculate(''), text="=",width=8, height=4,relief=RAISED, overrelief=RIDGE, bg=color.btnColor, fg=color.textColor, font=('Arial',9,'bold'))
btnIgual.place(x=222,y=315)

#-------------------------------------------------------
application.bind("<Key-*>", lambda event: operator('*'))
application.bind("<Key-+>", lambda event: operator('+'))
application.bind("<Key-/>", lambda event: operator('/'))
application.bind("<Key-%>", lambda event: operator('%'))
application.bind("<Key-->", lambda event: operator('-'))
#-------------------------------------------------------
application.bind("<Key-1>", lambda event: inputDate('1'))
application.bind("<Key-2>", lambda event: inputDate('2'))
application.bind("<Key-3>", lambda event: inputDate('3'))
application.bind("<Key-4>", lambda event: inputDate('4'))
application.bind("<Key-5>", lambda event: inputDate('5'))
application.bind("<Key-6>", lambda event: inputDate('6'))
application.bind("<Key-7>", lambda event: inputDate('7'))
application.bind("<Key-8>", lambda event: inputDate('8'))
application.bind("<Key-9>", lambda event: inputDate('9'))
application.bind("<Key-0>", lambda event: inputDate('0'))
#-------------------------------------------------------
application.bind("<Key-Delete>",cleanAllInput)
application.bind("<Key-Escape>",cleanAllInput)
application.bind("<BackSpace>", cleanInput)
application.bind("<Return>", calculate)


application.mainloop()