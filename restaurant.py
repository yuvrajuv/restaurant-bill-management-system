from time import localtime
from tkinter import*
import random
import time;
from tkinter import simpledialog
import smtplib;
from email.mime.text import MIMEText;
from email.mime.multipart import MIMEMultipart;
from email.mime.base import MIMEBase;
from email import encoders;
from tkinter import messagebox
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
def emailbill():
    passwrd = simpledialog.askstring(title="Input",prompt="Enter Your G-Mail Passsword to Mail Invoice:",show = "*");
    ne3 = simpledialog.askstring(title="Input",prompt="Enter users mail address to mail invoice");
    from_user = "yuvvraajuvpandey@gmail.com";
    to_user = ne3;
    subject = "Invoice";
    msg = MIMEMultipart();
    msg["From"] = from_user;
    msg["To"] = to_user;
    msg["Subject"] = subject;
    body = "Hi, \nYour e-bill has been generated. See details in below Attachment.\nFor any query, feel free to contact us.\nThank You";
    msg.attach(MIMEText(body,"plain"));
    file = "Documents\invoice.txt";
    attach = open(file,"rb");
    p = MIMEBase("application","octet-stream");
    p.set_payload((attach).read());        
    encoders.encode_base64(p);
    p.add_header('content-Disposition',"attachment; filename = "+file);
    msg.attach(p);
    text = msg.as_string();
    server = smtplib.SMTP('smtp.gmail.com',587);             
    server.starttls();
    server.login(from_user,passwrd);
    server.sendmail(from_user,to_user,text);
    c = server.quit();
    if c:
        messagebox.showinfo("","Invoice has been Successfully mailed");
    else:
        messagebox.showinfo("","Sorry please check the Email again or other glitches");

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

    subtotal=(CostofFries + CostofDrinks + CostofFliet + CostofBurger + CostCheese_Burger + CostChicken_Burger)

    PayTax=((CostofFries+ CostofDrinks + CostofFliet + CostofBurger + CostCheese_Burger + CostChicken_Burger)* 0.2)

    Ser_Charge = ((CostofFries+ CostofDrinks + CostofFliet + CostofBurger + CostCheese_Burger + CostChicken_Burger)/99)
    
    subtotal2=(PayTax+ subtotal)
    
    TotalCost=(PayTax+ subtotal + Ser_Charge)


    CostofMeals = "₹", str('%.2f' % subtotal)
    Service = "₹",str('%.2f'% Ser_Charge)
    OverAllCost = "₹",str('%.2f'% (TotalCost))
    PaidTax="₹",str('%.2f'% PayTax)



    Service_Charge.set(Service)
    Cost.set(CostofMeals)
    Tax.set(PaidTax)
    SubTotal.set(subtotal2)
    Total.set(OverAllCost)
    
   
    file = open('Documents\invoice.txt','w')
    file.write("\n\n******INVOICE******")
    file.write("\n\nService Provider")
    file.write("\n\nName : Yuvraj")
    file.write("\nCity : Prayagraj")
    file.write("\nState : Uttar Pradesh")
    file.write("\nPost Code : 211008")
    
    file.write("\n\n******BILL DETAILS******")
    file.write("\n\nReference Number : "+str(randomRef));
    
    file.write("\n\n   Name       Units    UnitCost  Amount\n")
    file.write("\nCold Drinks\t"+str(CoD)+"\t45\t"+str(CostofDrinks));
    file.write("\nFrench Fries\t"+str(CoF)+"\t50\t"+str(CostofFries));
    file.write("\nVeg Burger\t"+str(CoBurger)+"\t65\t"+str(CostofBurger));
    file.write("\nPaneer Filet\t"+str(CoFilet)+"\t125\t"+str(CostofFliet));
    file.write("\nChicken Burger\t"+str(CoChicBurger)+"\t100\t"+str(CostChicken_Burger));
    file.write("\nCheese Burger\t"+str(CoCheese_Burger)+"\t85\t"+str(CostCheese_Burger));
    
    file.write("\n\nCost Of Meals : "+str('%.2f'%subtotal));
    file.write("\nService Charge : "+str('%.2f'%Ser_Charge));
    file.write("\nGST : "+str('%.2f'%PayTax));
    file.write("\nSub Total : "+str('%.2f'%subtotal2));
    file.write("\n\nTotal Cost : "+str('%.2f'%TotalCost));
    file.write("\n\nEmail: yuvvraajuvpandey@gmail.com")
    file.write("\nDon't hesitate to contact us for any questions")
    file.write("\n\n******Thank You, Visit Again******")
    file.close()
    

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

lblBurger = Label(f1,font=('arial',16,'bold'), text="Veg Burger", bd=16,anchor='w')
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
                 command= Ref).grid(row=7,column=0)

btnbill= Button(f1,padx=16,pady=8,bd=16,fg="black",font=('arial',16,'bold'),width=10,text="Send Bill",bg="#BCEE68",
                 command= emailbill).grid(row=7,column=1)

btnReset= Button(f1,padx=16,pady=8,bd=16,fg="black",font=('arial',16,'bold'),width=10,text="Reset",bg="#BCEE68",
                 command= Reset).grid(row=7,column=2)

btnExit= Button(f1,padx=16,pady=8,bd=16,fg="black",font=('arial',16,'bold'),width=10,text="Exit",bg="#BCEE68",
                 command= qExit).grid(row=7,column=3)

root.mainloop()
