value1 = " "
value2 = " "
last = ''
next= ''
while True:
    text = str(input("Valor: "))
    value1 += text
    size  = len(value1)
    last = value1[-2]
    next = text
    if last == next:
        print("colocar pass")
    else:
        value2 += text
        
        print(value2)
    print (f"valor {value1}, last{last}, next{next}")
    
