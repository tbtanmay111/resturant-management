from tkinter import *
main=Tk()
main.title('My Resturant')
info=[]
readdata=[]
data=[]
c=0
#scrollbar= Scrollbar(main)
#scrollbar.grid(sticky=E, fill=Y)

frame1 = Frame(main,width=1200,height=800,bg='red')
first=Label(frame1,text='OUR RESTRAUNT',bg='green',font=('Comic Sans MS',30,'underline'))
first.grid(row=0,columnspan=5,ipadx=100,pady=5)
bil=Label(frame1,text="BILL",bg='green',font=('Comic Sans MS',20,'underline'))
bil.grid(row=1,columnspan=5,ipadx=100,pady=5)
item=Label(frame1,text='QUANTITY',bg='green',font=('Comic Sans MS',10,'underline'))
item.grid(row=2,column=0,ipadx=50,sticky='',pady=10)
price=Label(frame1,text='PRICE',bg='green',font=('Comic Sans MS',10,'underline'))
price.grid(row=2,column=1,ipadx=50,sticky='',pady=10)
quantity=Label(frame1,text='FOOD ITEMS',bg='green',font=('Comic Sans MS',10,'underline'))
quantity.grid(row=2,column=3,ipadx=50,sticky='',pady=10,padx=10)


#for writing into file
def writeInfo():
    global info
    with open('restraunt.txt','w') as file:
        for listitem in info:
            file.write('%s \n'%listitem)
    file.close()

#FOR EXTRACTING FROM FILE AND DISPLAYING FILE CONTENTS
def readInfo():
    global data
    with open('restraunt.txt','r') as file:
        for line in file:
            readd=line[:-1]
            data.append(readd)
            submitout.config(text=data)
    file.close()

#for extracting single element
def extract():
    global data
    l=len(data)
    for i in range(0,l):
        #if(type(data[i])==int):
        print(type(data[i]))

#for billing
def generatebill():
    readInfo()
    extract()

    cgst=9
    sgst=9
    total=price+(price*0.18)

def totalAmount():
    global totq
    global tot

    for j in range (0,4):
        tot+=totq[j]
    totalout.config(text=tot)
    sgstv = tot * (sgst/100)
    cgstv = sgstv
    tot +=(sgstv*2)
    nettotalout.config(text = tot)
def billNo():
    global billNumscr

    billno = random.randint(9712980, 9950876)
    billNumscr.config(text= billno)
    sgstvalue.config(text=sgst)
    cgstvalue.config(text=cgst)
    totalAmount()
    read()





#it gets the value from user and sends it to writeinfo
def getval(s):
    global info
    if(s=='1'):
        info=['SAMOSA(2PC)']
        sa=samo.get()
        tot=int(sa)*15
        info.append(int(tot))
        print(type(info[1]))
        writeInfo()
        info=[ ]
    elif (s == '2'):
        info = ['MOMOS(8PC)']
        sa=mom.get()
        tot = int(sa) * 40
        info.append(int(tot))
        print(info)
        writeInfo()
        info = []
    elif (s == '3'):
        info = ['VEG THALI']
        sa=thal.get()
        tot = int(sa) * 90
        info.append(int(tot))
        print(info)
        writeInfo()
        info = []
    elif (s == '4'):
        info = ['DELUXE THALI']
        sa=dthal.get()
        tot = int(sa) * 120
        info.append(int(tot))
        print(info)
        writeInfo()
        info = []
    elif (s == '5'):
        info=['NON VEG THALI']
        sa=nthal.get()
        tot = int(sa) *120
        info.append(int(tot))
        print(info)
        writeInfo()
        info = []
    elif (s == '6'):
        info = ['WATER']
        sa=wate.get()
        tot=int(sa)*20
        info.append(int(tot))
        print(info)
        writeInfo()
        info = []
    elif (s == '7'):
        info = ['COLD DRINK']
        sa=drin.get()
        tot = int(sa)*20
        info.append(int(tot))
        print(info)
        writeInfo()
        info = []

samo=Entry(frame1)
samo.grid(row=3,column=0,ipadx=50,sticky='',pady=3)
samp=Label(frame1,text='Rs.15',bg='green',font=('Comic Sans MS',10,'underline'))
samp.grid(row=3,column=1,ipadx=50,sticky='',pady=3)
sam = Button(frame1, text='SAMOSA(2PC)',command=lambda:getval('1'), height=2, width=20)
sam.grid(row=3, column=3, padx=5, pady=3,sticky=W)
photo1=PhotoImage(file='samosa.png')
samoi=Label(frame1,image=photo1)
samoi.grid(row=3,column=4,sticky='')


mom=Entry(frame1)
mom.grid(row=4,column=0,ipadx=50,sticky='',pady=3)
momop=Label(frame1,text='Rs.40',bg='green',font=('Comic Sans MS',10,'underline'))
momop.grid(row=4,column=1,ipadx=50,sticky='',pady=3)
momo = Button(frame1, text='MOMOS(8PC)', command = lambda:getval('2'),height=2, width=20)
momo.grid(row=4, column=3, padx=5, pady=3,sticky=W)
photo2=PhotoImage(file='momos.png')
momosi=Label(frame1,image=photo2)
momosi.grid(row=4,column=4,ipadx=5,sticky='',pady=3)

thal=Entry(frame1)
thal.grid(row=5,column=0,ipadx=50,sticky='',pady=3)
thalip=Label(frame1,text='Rs.90',bg='green',font=('Comic Sans MS',10,'underline'))
thalip.grid(row=5,column=1,ipadx=50,sticky='',pady=3)
thali = Button(frame1, text='VEG. THALI', command = lambda:getval('3'),height=2, width=20)
thali.grid(row=5, column=3, padx=5, pady=3,sticky=W)
photo3=PhotoImage(file='veg thali.png')
thalii=Label(frame1,image=photo3)
thalii.grid(row=5,column=4,ipadx=5,sticky='',pady=3)

dthal=Entry(frame1)
dthal.grid(row=6,column=0,ipadx=50,sticky='',pady=3)
dthalip=Label(frame1,text='Rs.120',bg='green',font=('Comic Sans MS',10,'underline'))
dthalip.grid(row=6,column=1,ipadx=50,sticky='',pady=3)
dthali = Button(frame1, text='DELUXE VEG. THALI', command = lambda:getval('4'), height=2, width=20)
dthali.grid(row=6, column=3, padx=5, pady=3,sticky=W)
photo4=PhotoImage(file='sthali.png')
dthalii=Label(frame1,image=photo4)
dthalii.grid(row=6,column=4,ipadx=5,sticky='',pady=3)

nthal=Entry(frame1)
nthal.grid(row=7,column=0,ipadx=50,sticky='',pady=3)
nthalip=Label(frame1,text='Rs.120',bg='green',font=('Comic Sans MS',10,'underline'))
nthalip.grid(row=7,column=1,ipadx=50,sticky='',pady=3)
nthali = Button(frame1, text='NON. VEG. THALI', command = lambda:getval('5'), height=2, width=20)
nthali.grid(row=7, column=3, padx=5, pady=3,sticky=W)
photo5=PhotoImage(file='nthali.png')
nthalii=Label(frame1,image=photo5)
nthalii.grid(row=7,column=4,ipadx=5,sticky='',pady=3)

wate=Entry(frame1)
wate.grid(row=8,column=0,ipadx=50,sticky='',pady=3)
watp=Label(frame1,text='Rs.20',bg='green',font=('Comic Sans MS',10,'underline'))
watp.grid(row=8,column=1,ipadx=50,sticky='',pady=3)
wat = Button(frame1, text='MINERAL WATER', command = lambda:getval('6'), height=2, width=20)
wat.grid(row=8, column=3, padx=5, pady=3,sticky=W)
photo6=PhotoImage(file='water.png')
watei=Label(frame1,image=photo6)
watei.grid(row=8,column=4,ipadx=5,sticky='',pady=3)

drin=Entry(frame1)
drin.grid(row=9,column=0,ipadx=50,sticky='',pady=3)
drinkp=Label(frame1,text='Rs.15',bg='green',font=('Comic Sans MS',10,'underline'))
drinkp.grid(row=9,column=1,ipadx=50,sticky='',pady=3)
drink = Button(frame1, text='COLD DRINKS',command = lambda:getval('7') , height=2, width=20)
drink.grid(row=9, column=3, padx=5, pady=3,sticky=W)
photo7=PhotoImage(file='drink.png')
drini=Label(frame1,image=photo7)
drini.grid(row=9,column=4,ipadx=5,sticky='',pady=3)


submit = Button(frame1,text='MY ORDER',command = lambda:readInfo(),height=2,width=20)
submit.grid(row=2,column=6)
submitout=Label(frame1,height=10,width=20)
submitout.grid(row=3,column=6)

#bill = Button(frame1, text='BILL',command= lambda:generatebill(),height=2,width=20)
#bill.grid(row=2, column=7)

billNum = Label(frame1, font=('aria', 10, 'bold'), text="BILL NO.", fg="black", bd=5)
billNum.grid(row=2, column=7)
billNumscr = Button(frame1, height=1, width=15, relief='sunken', borderwidth=5, bg="powder blue")
billNumscr.grid(row=2, column=8, padx=5, pady=5, ipadx=5, ipady=5)

sgstlabel = Label(frame1, font=('aria', 10, 'bold'), text="SGST %", fg="black", bd=5)
sgstlabel.grid(row=3, column=7)
sgstvalue = Button(frame1, height=1, width=15, relief='sunken', borderwidth=5, bg="powder blue")
sgstvalue.grid(row=3, column=8, padx=5, pady=5, ipadx=5, ipady=5)

cgstlabel = Label(frame1, font=('aria', 10, 'bold'), text="CGST %", fg="black", bd=5)
cgstlabel.grid(row=4, column=7)
cgstvalue = Button(frame1, height=1, width=15, relief='sunken', borderwidth=5, bg="powder blue")
cgstvalue.grid(row=4, column=8, padx=5, pady=5, ipadx=5, ipady=5)

quantitylabel = Label(frame1, font=('aria', 10, 'bold'), text="QUANTITY", fg="black", bd=5)
quantitylabel.grid(row=5, column=7)
quantityout = Button(frame1, height=2, width=30, relief='sunken', borderwidth=5, bg="powder blue")
quantityout.grid(row=6, column=7, padx=5, pady=5, ipadx=5, ipady=5)


total = Label(frame1, font=('aria', 10, 'bold'), text="TOTAL", fg="black", bd=5)
total.grid(row=5, column=8)
totalout = Button(frame1, height=1, width=15, relief='sunken', borderwidth=5, bg="powder blue")
totalout.grid(row=6, column=8, padx=5, pady=5, ipadx=5, ipady=5)

nettotal = Label(frame1, font=('aria', 10, 'bold'), text="TOTAL (TAX INC)", fg="black", bd=5)
nettotal.grid(row=7, column=7)
nettotalout = Button(frame1, height=1, width=15, relief='sunken', borderwidth=5, bg="powder blue")
nettotalout.grid(row=7, column=8, padx=5, pady=5, ipadx=5, ipady=5)



frame1.grid()
main.mainloop()
