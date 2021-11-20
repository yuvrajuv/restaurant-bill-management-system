from time import localtime
from tkinter import*
import random
import time;

root=Tk ()
root.geometry("1600x800+0+0")
root.title("Resturant Billing")


text_Input=StringVar()
operator=""

Tops = Frame(root,width = 1600,height=50,bg="#BCEE68", relief= SUNKEN)
Tops.pack(side=TOP)

f1 = Frame(root,width = 800,height=700, relief= SUNKEN)
f1.pack(side=LEFT)

f2 = Frame(root,width = 300,height=700, relief= SUNKEN)
f2.pack(side=RIGHT)

#####################################################DATE TIME FUNCTION#####################################################
localtime=time.asctime(time.localtime(time.time()))

#################local INfo#################################################################################################
lblInfo = Label(Tops, font=('arial',50,'bold'),text= "Resturant Bill Management System",fg="#6E8B3D",bd=10,anchor='w')
lblInfo.grid(row=0,column=0)

lblDateTime = Label(Tops, font=('arial',20,'bold'),text= localtime,fg="#00C957",bd=10,anchor='w')

lblDateTime.grid(row=1,column=0)


#################################Calculator for calculatin the stufff

def btnClick(numbers):
    global operator
    operator=operator+ str(numbers)
    text_Input.set(operator)

def btnClearDisplay():
    global operator
    operator=""
    text_Input.set("")

def btnEqualsInput():
    global operator
    sumup= str(eval(operator))
    text_Input.set(sumup)
    operator=""

def Ref():
    x= random.randint(12908,50876)
    randomRef = str(x)
    rand.set(randomRef)
    
    CoF = float(Fries.get())
    CoD = float(Drinks.get())
    CoFilet = float(Filet.get())
    CoBurger= float(Burger.get())

    CoChicBurger = float(Chicken.get())
    CoCheese_Burger= float(Cheese.get())

   

    CostofFries= CoF * 50
    CostofDrinks = CoD * 45
    CostofFliet= CoFilet * 125
    CostofBurger = CoBurger * 65
    CostChicken_Burger = CoChicBurger * 100
    CostCheese_Burger= CoCheese_Burger * 85

    CostofMeals = "₹", str('%.2f' % (CostofFries + CostofDrinks + CostofFliet + CostofBurger + CostCheese_Burger + CostChicken_Burger))

    PayTax=((CostofFries+ CostofDrinks + CostofFliet + CostofBurger + CostCheese_Burger + CostChicken_Burger)* 0.2)

    TotalCost= (CostofFries+ CostofDrinks + CostofFliet + CostofBurger + CostCheese_Burger + CostChicken_Burger)

    Ser_Charge = ((CostofFries+ CostofDrinks + CostofFliet + CostofBurger + CostCheese_Burger + CostChicken_Burger)/99)


    Service = "₹",str('%.2f'% Ser_Charge)
    OverAllCost = "₹",str('%.2f'% (PayTax+ TotalCost + Ser_Charge))
    PaidTax="₹",str('%.2f'% PayTax)



    Service_Charge.set(Service)
    Cost.set(CostofMeals)
    Tax.set(PaidTax)
    SubTotal.set(CostofMeals)
    Total.set(OverAllCost)

def qExit():
    root.destroy()

def Reset():
    rand.set("")
    Fries.set("")
    Burger.set("")
    Filet.set("")
    Chicken.set("")
    Cheese.set("")
    SubTotal.set("")
    Total.set("")
    Service_Charge.set("")
    Drinks.set("")
    Tax.set("")
    Cost.set("")
    '''Chicken_Burger.set("")
    Cheese_Burger.set("")'''
  


#------------------------------------------------------------------------------------------------------------
txtDisplay = Entry(f2,font=('arial',20,'bold') ,bd=30 ,textvariable=text_Input,  insertwidth=4,bg="#BCEE68",
                   justify='right')
txtDisplay.grid(columnspan=4)

#---------------------------------------------------------------------------------------------------------------
btn7=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
            text="7",bg="#BCEE68",command=lambda: btnClick(7)).grid(row=2,column=0)
btn8=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
            text="8",bg="#BCEE68",command=lambda: btnClick(8)).grid(row=2,column=1)
btn9=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
            text="9",bg="#BCEE68",command=lambda: btnClick(9)).grid(row=2,column=2)
Addition=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
            text="+",bg="#BCEE68",command=lambda: btnClick("+")).grid(row=2,column=3)
#---------------------------------------------------------------------------------------------------------------
btn4=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
            text="4",bg="#BCEE68",command=lambda: btnClick(4)).grid(row=3,column=0)
btn5=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
            text="5",bg="#BCEE68",command=lambda: btnClick(5)).grid(row=3,column=1)
btn6=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
            text="6",bg="#BCEE68",command=lambda: btnClick(6)).grid(row=3,column=2)
Subtraction=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
            text="-",bg="#BCEE68",command=lambda: btnClick("-")).grid(row=3,column=3)
#_-------------------------------------------------------------------------------------------------------------

btn1=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
            text="1",bg="#BCEE68",command=lambda: btnClick(1)).grid(row=4,column=0)
btn2=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
            text="2",bg="#BCEE68",command=lambda: btnClick(2)).grid(row=4,column=1)
btn3=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
            text="3",bg="#BCEE68",command=lambda: btnClick(3)).grid(row=4,column=2)
Multiply=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
            text="*",bg="#BCEE68",command=lambda: btnClick("*")).grid(row=4,column=3)

#-----------------------------------------------------------------------------------------------------------------

btn0=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
            text="0",bg="#BCEE68",command=lambda: btnClick(0)).grid(row=5,column=0)
btnClear=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
            text="C",bg="#BCEE68",command=btnClearDisplay).grid(row=5,column=1)
btnEquals=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
            text="=",bg="#BCEE68",command= btnEqualsInput).grid(row=5,column=2)
Division =Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
            text="/",bg="#BCEE68",command=lambda: btnClick("/")).grid(row=5,column=3)


#-------------------------------------------RESTURANT INFO 1------------------------------------------------------------------
rand= StringVar()
Fries= StringVar()
Burger= StringVar()
Filet= StringVar()
Chicken = StringVar()
Cheese= StringVar()
SubTotal = StringVar()
Total= StringVar()
Service_Charge= StringVar()
Drinks = StringVar()
Tax= StringVar()
Cost=StringVar()
Chicken_Burger= StringVar()
Cheese_Burger= StringVar()

lblDrinks = Label(f1,font=('arial',16,'bold'), text="Cold Drinks", bd=16,anchor='w')
lblDrinks.grid(row=0,column=0)

txtDrinks= Entry(f1,font=('arial',16,'bold'), textvariable=Drinks, bd=10,insertwidth=4,bg="#ffffff",justify='right')
txtDrinks.grid(row=0,column=1)


lblFries = Label(f1,font=('arial',16,'bold'), text="French Fries", bd=16,anchor='w')
lblFries.grid(row=1,column=0)

txtFries= Entry(f1,font=('arial',16,'bold'), textvariable=Fries, bd=10,insertwidth=4,bg="#ffffff",justify='right')
txtFries.grid(row=1,column=1)

lblBurger = Label(f1,font=('arial',16,'bold'), text="AlooTiki Burger", bd=16,anchor='w')
lblBurger.grid(row=2,column=0)

txtBurger= Entry(f1,font=('arial',16,'bold'), textvariable=Burger, bd=10,insertwidth=4,bg="#ffffff",justify='right')
txtBurger.grid(row=2,column=1)

lblFilet = Label(f1,font=('arial',16,'bold'), text="Paneer Filet", bd=16,anchor='w')
lblFilet.grid(row=3,column=0)

txtFilet= Entry(f1,font=('arial',16,'bold'), textvariable=Filet, bd=10,insertwidth=4,bg="#ffffff",justify='right')
txtFilet.grid(row=3,column=1)


lblChicken = Label(f1,font=('arial',16,'bold'), text="Chicken Burger", bd=16,anchor='w')
lblChicken.grid(row=4,column=0)

txtChicken= Entry(f1,font=('arial',16,'bold'), textvariable=Chicken, bd=10,insertwidth=4,bg="#ffffff",justify='right')
txtChicken.grid(row=4,column=1)

lblCheese = Label(f1,font=('arial',16,'bold'), text="Cheese Burger", bd=16,anchor='w')
lblCheese.grid(row=5,column=0)

txtCheese= Entry(f1,font=('arial',16,'bold'), textvariable=Cheese, bd=10,insertwidth=4,bg="#ffffff",justify='right')
txtCheese.grid(row=5,column=1)



#-------------------------------------------RESTURANT INFO 2 ------------------------------------------------------------------


lblReference = Label(f1,font=('arial',16,'bold'), text="Reference", bd=16,anchor='w')
lblReference.grid(row=0,column=2)

txtReference= Entry(f1,font=('arial',16,'bold'), textvariable=rand, bd=10,insertwidth=4,bg="#BCEE68",justify='right')
txtReference.grid(row=0,column=3)

lblCost = Label(f1,font=('arial',16,'bold'), text="Cost of Meals", bd=16,anchor='w')
lblCost.grid(row=1,column=2)

txtCost= Entry(f1,font=('arial',16,'bold'), textvariable=Cost, bd=10,insertwidth=4,bg="#BCEE68",justify='right')
txtCost.grid(row=1,column=3)

lblService = Label(f1,font=('arial',16,'bold'), text="Service Charge", bd=16,anchor='w')
lblService.grid(row=2,column=2)

txtService= Entry(f1,font=('arial',16,'bold'), textvariable=Service_Charge, bd=10,insertwidth=4,bg="#BCEE68",justify='right')
txtService.grid(row=2,column=3)

lblStateTax = Label(f1,font=('arial',16,'bold'), text="GST", bd=16,anchor='w')
lblStateTax.grid(row=3,column=2)

txtStateTax= Entry(f1,font=('arial',16,'bold'), textvariable=Tax, bd=10,insertwidth=4,bg="#BCEE68",justify='right')
txtStateTax.grid(row=3,column=3)


lblSubTotal = Label(f1,font=('arial',16,'bold'), text="Sub Total", bd=16,anchor='w')
lblSubTotal.grid(row=4,column=2)

txtSubTotal= Entry(f1,font=('arial',16,'bold'), textvariable=SubTotal, bd=10,insertwidth=4,bg="#BCEE68",justify='right')
txtSubTotal.grid(row=4,column=3)

lblTotalCost = Label(f1,font=('arial',16,'bold'), text="Total Cost", bd=16,anchor='w')
lblTotalCost.grid(row=5,column=2)

txtTotalCost= Entry(f1,font=('arial',16,'bold'), textvariable=Total, bd=10,insertwidth=4,bg="#BCEE68",justify='right')
txtTotalCost.grid(row=5,column=3)



######-------------------------------------BUTTONS---------------------------------------------------------------

btnTotal= Button(f1,padx=16,pady=8,bd=16,fg="black",font=('arial',16,'bold'),width=10,text="Total",bg="#BCEE68",
                 command= Ref).grid(row=7,column=1)

btnReset= Button(f1,padx=16,pady=8,bd=16,fg="black",font=('arial',16,'bold'),width=10,text="Reset",bg="#BCEE68",
                 command= Reset).grid(row=7,column=2)

btnExit= Button(f1,padx=16,pady=8,bd=16,fg="black",font=('arial',16,'bold'),width=10,text="Exit",bg="#BCEE68",
                 command= qExit).grid(row=7,column=3)


root.mainloop()