from tkinter import *
from math import *
import random
from tkinter import filedialog,messagebox
import time
import os,tempfile

#functionality
        
def subtotal():
    global rotiprice,daalprice,fishprice,paneerprice,muttonprice,chickenprice,butternonprice,methichamanprice
    global kitkatprice,oreoprice,mangoprice,vanillaprice,nutellaprice,chocolateprice,strawberryprice,bananaprice
    global blackforestprice,butterscotchprice,redvelvetprice,pineappleprice,brownieprice,cupcakeprice,spongecakeprice,cheesecakeprice
    global totalcakesprice,totalmilkshakeprice,totalfoodprice,subtotal1,servicetax1,totalcostprice
    rotiprice=int(rotiEntry.get())*20
    daalprice=int(daalEntry.get())*50
    fishprice=int(fishEntry.get())*200
    paneerprice=int(paneerEntry.get())*150
    muttonprice=int(muttonEntry.get())*300
    chickenprice=int(chickenEntry.get())*50
    butternonprice=int(butternonEntry.get())*50
    methichamanprice=int(methichamanEntry.get())*50
    
    totalfoodprice=sum([rotiprice,daalprice,fishprice,paneerprice,muttonprice,chickenprice,butternonprice,methichamanprice])
    print(totalfoodprice)
    
    costoffoodEntry.delete(0,END)
    costoffoodEntry.insert(1,totalfoodprice)
    
    kitkatprice= int(kitkatEntry.get())*60
    oreoprice=int(oreoEntry.get())*80
    mangoprice=int(mangoEntry.get())*50
    vanillaprice=int(vanillaEntry.get())*60
    nutellaprice=int(nutellaEntry.get())*100
    chocolateprice=int(chocolateEntry.get())*80
    strawberryprice=int(strawberryEntry.get())*70
    bananaprice=int(bananaEntry.get())*50
    
    totalmilkshakeprice=sum([kitkatprice,oreoprice,mangoprice,vanillaprice,nutellaprice,chocolateprice,strawberryprice,bananaprice])
    costofdrinksEntry.delete(0,END)
    costofdrinksEntry.insert(1,totalmilkshakeprice)
    
    blackforestprice=int(blackforestEntry.get())*80
    redvelvetprice=int(redvelvetEntry.get())*70
    butterscotchprice=int(butterscotchEntry.get())*60
    pineappleprice=int(pineappleEntry.get())*50
    brownieprice=int(BrownieEntry.get())*80
    cupcakeprice=int(cupcakeEntry.get())*40
    spongecakeprice=int(spongecakeEntry.get())*40
    cheesecakeprice=int(cheesecakeEntry.get())*40
    
    totalcakesprice=sum([blackforestprice,redvelvetprice,butterscotchprice,pineappleprice,brownieprice,cupcakeprice,spongecakeprice,cheesecakeprice])
    costofcakesEntry.delete(0,END)
    costofcakesEntry.insert(1,totalcakesprice)
    
    subtotal1=totalcakesprice+totalfoodprice+totalmilkshakeprice
    subtotalEntry.delete(0,END)
    subtotalEntry.insert(0,subtotal1)
    
    servicetax1=subtotal1*0.05
    ServicetaxEntry.delete(0,END)
    ServicetaxEntry.insert(0,servicetax1)
    
    totalcostprice=subtotal1+servicetax1
    TotalcostEntry.delete(0,END)
    TotalcostEntry.insert(0,totalcostprice)
    
def receipt():
    textarea.delete(1.0,END)
    x=random.randint(100,10000)
    billnumber='BILL'+str(x)
    date=time.strftime('%d/%m/%Y') 
    textarea.insert(END,'Receipt Ref:\t\t\t'+billnumber+'\t\t'+date+'\n')
    textarea.insert(END,'************************************************************\n')
    textarea.insert(END,'ITEMS:\t\t\t Quantity\t\tCost of Items(Rs)\n')
    textarea.insert(END,'************************************************************\n')
    if rotiEntry.get()!='0':
        textarea.insert(END,f" Roti \t\t\t {rotiEntry.get()}\t\t {rotiprice}\n")
    if daalEntry.get()!='0':
        textarea.insert(END,f" Daal \t\t\t {daalEntry.get()}\t\t {daalprice}\n")
    if fishEntry.get()!='0':
        textarea.insert(END,f" Fish \t\t\t {fishEntry.get()}\t\t {fishprice}\n")
    if paneerEntry.get()!='0':
        textarea.insert(END,f" Paneer \t\t\t {paneerEntry.get()}\t\t {paneerprice}\n")
    if muttonEntry.get()!='0':
        textarea.insert(END,f" Mutton \t\t\t {muttonEntry.get()}\t\t {muttonprice}\n")
    if chickenEntry.get()!='0':
        textarea.insert(END,f" Chicken Biryani \t\t\t {chickenEntry.get()}\t\t {chickenprice}\n")
    if butternonEntry.get()!='0':
        textarea.insert(END,f" Butter non \t\t\t {butternonEntry.get()}\t\t {butternonprice}\n")
    if methichamanEntry.get()!='0':
        textarea.insert(END,f" Methi chaman \t\t\t {methichamanEntry.get()}\t\t {methichamanprice}\n")  

    if kitkatEntry.get()!='0':
        textarea.insert(END,f" Kitkat shake \t\t\t {kitkatEntry.get()}\t\t {kitkatprice}\n")
    if oreoEntry.get()!='0':
        textarea.insert(END,f" Oreo shake \t\t\t {oreoEntry.get()}\t\t {oreoprice}\n")
    if mangoEntry.get()!='0':
        textarea.insert(END,f" Mango shake \t\t\t {mangoEntry.get()}\t\t {mangoprice}\n")
    if chocolateEntry.get()!='0':
        textarea.insert(END,f" Chocolate shake \t\t\t {chocolateEntry.get()}\t\t {chocolateprice}\n")
    if nutellaEntry.get()!='0':
        textarea.insert(END,f" Nutella shake \t\t\t {nutellaEntry.get()}\t\t {nutellaprice}\n")
    if vanillaEntry.get()!='0':
        textarea.insert(END,f" Vanilla shake \t\t\t {vanillaEntry.get()}\t\t {vanillaprice}\n")
    if bananaEntry.get()!='0':
        textarea.insert(END,f" Banana shake \t\t\t {bananaEntry.get()}\t\t {bananaprice}\n")
    if strawberryEntry.get()!='0':
        textarea.insert(END,f" Strawberry shake \t\t\t {strawberryEntry.get()}\t\t {strawberryprice}\n")

    if blackforestEntry.get()!='0':
        textarea.insert(END,f" Black forest cake \t\t\t {blackforestEntry.get()}\t\t {blackforestprice}\n")
    if butterscotchEntry.get()!='0':
        textarea.insert(END,f" Butter scotch cake \t\t\t {butterscotchEntry.get()}\t\t {butterscotchprice}\n")
    if redvelvetEntry.get()!='0':
        textarea.insert(END,f" Red velvet cake \t\t\t {redvelvetEntry.get()}\t\t {redvelvetprice}\n")
    if  BrownieEntry.get()!='0':
        textarea.insert(END,f" Brownie cake \t\t\t {BrownieEntry.get()}\t\t {brownieprice}\n")
    if pineappleEntry.get()!='0':
        textarea.insert(END,f" Pineapple cake \t\t\t {pineappleEntry.get()}\t\t {pineappleprice}\n")
    if cupcakeEntry.get()!='0':
        textarea.insert(END,f" Cup cake \t\t\t {cupcakeEntry.get()}\t\t {cupcakeprice}\n")
    if spongecakeEntry.get()!='0':
        textarea.insert(END,f" Sponge cake \t\t\t {spongecakeEntry.get()}\t\t {spongecakeprice}\n")
    if cheesecakeEntry.get()!='0':
        textarea.insert(END,f" Cheese cake \t\t\t {cheesecakeEntry.get()}\t\t {cheesecakeprice}\n")
    textarea.insert(END,'************************************************************\n')
    if totalfoodprice!='0':
        textarea.insert(END,f'Cost Of Food \t\t\t \t\t {totalfoodprice}\n\n')
    if totalmilkshakeprice!='0':
         textarea.insert(END,f'Cost Of Milkshakes \t\t\t \t\t {totalmilkshakeprice}\n\n')
    if totalcakesprice!='0':    
        textarea.insert(END,f'Cost Of Cakes \t\t\t \t\t {totalcakesprice}\n\n')
    textarea.insert(END,f'Sub Total \t\t\t \t\t {subtotal1}\n\n')
    textarea.insert(END,f'Service Tax \t\t\t \t\t {servicetax1}\n\n')
    textarea.insert(END,f'Total Cost \t\t\t \t\t {totalcostprice}\n\n')
    textarea.insert(END,'\n**********THANK YOU FOR SHOPPING!! HAVE A GREAT DAY*********\n')
  
if not os.path.exists('restaurant/'):
    os.mkdir('restaurant/')  
def save():
    u=filedialog.asksaveasfile(mode='w',defaultextension='.txt')
    bill_data=textarea.get(1.0,END)
    u.write(bill_data)
    u.close()
    messagebox.showinfo('Information','Your Bill is Succesfully Saved')

def printbilling():
    if textarea.get(1.0,END) =='\n':
        messagebox.showerror("Error","Bill is Empty")
    else:
       file = tempfile.mktemp('.txt')
       open(file,'w').write(textarea.get(1.0,END))
       os.startfile(file,'print')
def clearall():
    rotiEntry.delete(0,END)
    rotiEntry.insert(0,0)
    daalEntry.delete(0,END)
    daalEntry.insert(0,0)
    fishEntry.delete(0,END)
    fishEntry.insert(0,0)
    paneerEntry.delete(0,END)
    paneerEntry.insert(0,0)
    chickenEntry.delete(0,END)
    chickenEntry.insert(0,0)
    butternonEntry.delete(0,END)
    butternonEntry.insert(0,0)
    methichamanEntry.delete(0,END)
    methichamanEntry.insert(0,0)
    
    kitkatEntry.delete(0,END)
    kitkatEntry.insert(0,0)
    oreoEntry.delete(0,END)
    oreoEntry.insert(0,0)
    mangoEntry.delete(0,END)
    mangoEntry.insert(0,0)
    chocolateEntry.delete(0,END)
    chocolateEntry.insert(0,0)
    nutellaEntry.delete(0,END)
    nutellaEntry.insert(0,0)
    vanillaEntry.delete(0,END)
    vanillaEntry.insert(0,0)
    bananaEntry.delete(0,END)
    bananaEntry.insert(0,0)
    strawberryEntry.delete(0,END)
    strawberryEntry.insert(0,0)

    blackforestEntry.delete(0,END)
    blackforestEntry.insert(0,0)
    butterscotchEntry.delete(0,END)
    butterscotchEntry.insert(0,0)
    redvelvetEntry.delete(0,END)
    redvelvetEntry.insert(0,0)
    BrownieEntry.delete(0,END)
    BrownieEntry.insert(0,0)
    pineappleEntry.delete(0,END)
    pineappleEntry.insert(0,0)
    cupcakeEntry.delete(0,END)
    cupcakeEntry.insert(0,0)
    spongecakeEntry.delete(0,END)
    spongecakeEntry.insert(0,0)
    cheesecakeEntry.delete(0,END)
    cheesecakeEntry.insert(0,0)
    
    costoffoodEntry.delete(0,END)
    costoffoodEntry.insert(0,0)
    costofcakesEntry.delete(0,END)
    costofcakesEntry.insert(0,0)
    costofdrinksEntry.delete(0,END)
    costofdrinksEntry.insert(0,0)
    
    subtotalEntry.delete(0,END)
    subtotalEntry.insert(0,0)
    ServicetaxEntry.delete(0,END)
    ServicetaxEntry.insert(0,0)
    TotalcostEntry.delete(0,END)
    TotalcostEntry.insert(0,0)
    textarea.delete(1.0,END)
    
    


root=Tk()


root.title("Restaurant Management System")


root.iconbitmap('icon.ico')

root.config(bg='tan1')


labelTitle=Label(root,text='Restaurant Management System',font=('times new roman',30,'bold'),bg='Hotpink4',fg='black',bd='10',relief=GROOVE)
labelTitle.pack(fill=X,pady=5)

mainframe=Frame(root,bd='7',relief=GROOVE)
mainframe.pack()

food=LabelFrame(mainframe,text="Food",font=("times new roman",13,"bold"),bg='light sea green',fg='black')
food.grid(row=0,column=0)
food.config(bg='light sea green')

roti=Label(food,text="Roti",font=("times new roman",13,'bold'),bg='light sea green')
roti.grid(row=0,column=0,padx=20,pady=10,sticky='w')


rotiEntry=Entry(food,width=20)
rotiEntry.grid(row=0,column=1,padx=20,pady=10)
rotiEntry.insert(0,0)

daal=Label(food,text="Daal",font=("times new roman",13,'bold'),bg='light sea green')
daal.grid(row=1,column=0,padx=20,pady=10,sticky='w')

daalEntry=Entry(food,width=20)
daalEntry.grid(row=1,column=1,padx=20,pady=10)
daalEntry.insert(0,0)

fish=Label(food,text="Fish",font=("times new roman",13,'bold'),bg='light sea green')
fish.grid(row=2,column=0,padx=20,pady=10,sticky='w')

fishEntry=Entry(food,width=20)
fishEntry.grid(row=2,column=1,padx=20,pady=10)
fishEntry.insert(0,0)

paneer=Label(food,text="Paneer",font=("times new roman",13,'bold'),bg='light sea green')
paneer.grid(row=3,column=0,padx=20,pady=10,sticky='w')

paneerEntry=Entry(food,width=20)
paneerEntry.grid(row=3,column=1,padx=20,pady=10)
paneerEntry.insert(0,0)

mutton=Label(food,text="Mutton",font=("times new roman",13,'bold'),bg='light sea green')
mutton.grid(row=4,column=0,padx=20,pady=10,sticky='w')

muttonEntry=Entry(food,width=20)
muttonEntry.grid(row=4,column=1,padx=20,pady=10)
muttonEntry.insert(0,0)

chicken=Label(food,text="chicken Biryani",font=("times new roman",13,'bold'),bg='light sea green')
chicken.grid(row=5,column=0,padx=20,pady=10,sticky='w')

chickenEntry=Entry(food,width=20)
chickenEntry.grid(row=5,column=1,padx=20,pady=10) 
chickenEntry.insert(0,0)

butternon=Label(food,text="Butter non",font=("times new roman",13,'bold'),bg='light sea green')
butternon.grid(row=6,column=0,padx=20,pady=10,sticky='w')

butternonEntry=Entry(food,width=20)
butternonEntry.grid(row=6,column=1,padx=20,pady=10) 
butternonEntry.insert(0,0)

methichaman=Label(food,text="Methi chaman",font=("times new roman",13,'bold'),bg='light sea green')
methichaman.grid(row=7,column=0,padx=20,pady=10,sticky='w')

methichamanEntry=Entry(food,width=20)
methichamanEntry.grid(row=7,column=1,padx=20,pady=10)
methichamanEntry.insert(0,0)

Drinkslabelframe=LabelFrame(mainframe,text="Milkshakes",font=("times new roman",13,'bold'),bg='light sea green',fg='black')
Drinkslabelframe.grid(row=0,column=1,pady=10,sticky='w')

kitkat=Label(Drinkslabelframe,text="Kitkat Shake",font=("times new roman",13,'bold'),fg='black',bg='light sea green')
kitkat.grid(row=0,column=0,padx=20,pady=10)

kitkatEntry=Entry(Drinkslabelframe,width=20)
kitkatEntry.grid(row=0,column=1,padx=20,pady=10)
kitkatEntry.insert(0,0)
oreo=Label(Drinkslabelframe,text="Oreo Shake",font=("times new roman",13,'bold'),fg='black',bg='light sea green')
oreo.grid(row=1,column=0,padx=20,pady=10,sticky='w')

oreoEntry=Entry(Drinkslabelframe,width=20)
oreoEntry.grid(row=1,column=1,padx=20,pady=10)
oreoEntry.insert(0,0)
mango=Label(Drinkslabelframe,text="Mango Shake",font=("times new roman",13,'bold'),fg='black',bg='light sea green')
mango.grid(row=2,column=0,padx=20,pady=10,sticky='w')

mangoEntry=Entry(Drinkslabelframe,width=20)
mangoEntry.grid(row=2,column=1,padx=20,pady=10)
mangoEntry.insert(0,0)

chocolate=Label(Drinkslabelframe,text="Chocolate Shake",font=("times new roman",13,'bold'),fg='black',bg='light sea green')
chocolate.grid(row=3,column=0,padx=20,pady=10,sticky='w')

chocolateEntry=Entry(Drinkslabelframe,width=20)
chocolateEntry.grid(row=3,column=1,padx=20,pady=10)
chocolateEntry.insert(0,0)

nutella=Label(Drinkslabelframe,text="Nutella Shake",font=("times new roman",13,'bold'),fg='black',bg='light sea green')
nutella.grid(row=4,column=0,padx=20,pady=10,sticky='w')

nutellaEntry=Entry(Drinkslabelframe,width=20)
nutellaEntry.grid(row=4,column=1,padx=20,pady=10)
nutellaEntry.insert(0,0)

vanilla=Label(Drinkslabelframe,text="Vanilla Shake",font=("times new roman",13,'bold'),fg='black',bg='light sea green')
vanilla.grid(row=5,column=0,padx=20,pady=10,sticky='w')


vanillaEntry=Entry(Drinkslabelframe,width=20)
vanillaEntry.grid(row=5,column=1,padx=20,pady=10)
vanillaEntry.insert(0,0)

banana=Label(Drinkslabelframe,text="Banana Shake",font=("times new roman",13,'bold'),fg='black',bg='light sea green')
banana.grid(row=6,column=0,padx=20,pady=10,sticky='w')

bananaEntry=Entry(Drinkslabelframe,width=20)
bananaEntry.grid(row=6,column=1,padx=20,pady=10)
bananaEntry.insert(0,0)

strawberry=Label(Drinkslabelframe,text="Strawberry Shake",font=("times new roman",13,'bold'),fg='black',bg='light sea green')
strawberry.grid(row=7,column=0,padx=20,pady=10,sticky='w')

strawberryEntry=Entry(Drinkslabelframe,width=20)
strawberryEntry.grid(row=7,column=1,padx=20,pady=10)
strawberryEntry.insert(0,0)

cakelabelframe=LabelFrame(mainframe,text="Cakes",font=("times new roman",13,'bold'),bg='light sea green',fg='black')
cakelabelframe.grid(row=0,column=2,pady=10,sticky='w')

blackforest=Label(cakelabelframe,text="Black Forest",font=("times new roman",13,'bold'),bg='light sea green',fg='black')
blackforest.grid(row=0,column=0,padx=20,pady=10,sticky='w')

blackforestEntry=Entry(cakelabelframe,width=20)
blackforestEntry.grid(row=0,column=1,padx=20,pady=10)
blackforestEntry.insert(0,0)

butterscotch=Label(cakelabelframe,text="Butter Scotch",font=("times new roman",13,'bold'),bg='light sea green',fg='black')
butterscotch.grid(row=1,column=0,padx=20,pady=10,sticky='w')

butterscotchEntry=Entry(cakelabelframe,width=20)
butterscotchEntry.grid(row=1,column=1,padx=20,pady=10)
butterscotchEntry.insert(0,0)

redvelvet=Label(cakelabelframe,text="Red Velvet",font=("times new roman",13,'bold'),bg='light sea green',fg='black')
redvelvet.grid(row=2,column=0,padx=20,pady=10,sticky='w')

redvelvetEntry=Entry(cakelabelframe,width=20)
redvelvetEntry.grid(row=2,column=1,padx=20,pady=10)
redvelvetEntry.insert(0,0)

Brownie=Label(cakelabelframe,text="Brownie",font=("times new roman",13,'bold'),bg='light sea green',fg='black')
Brownie.grid(row=3,column=0,padx=20,pady=10,sticky='w')

BrownieEntry=Entry(cakelabelframe,width=20)
BrownieEntry.grid(row=3,column=1,padx=20,pady=10)
BrownieEntry.insert(0,0)

pineapple=Label(cakelabelframe,text="Pine Apple",font=("times new roman",13,'bold'),bg='light sea green',fg='black')
pineapple.grid(row=4,column=0,padx=20,pady=10,sticky='w')

pineappleEntry=Entry(cakelabelframe,width=20)
pineappleEntry.grid(row=4,column=1,padx=20,pady=10)
pineappleEntry.insert(0,0)

cupcake=Label(cakelabelframe,text="Cup Cake",font=("times new roman",13,'bold'),bg='light sea green',fg='black')
cupcake.grid(row=5,column=0,padx=20,pady=10,sticky='w')

cupcakeEntry=Entry(cakelabelframe,width=20)
cupcakeEntry.grid(row=5,column=1,padx=20,pady=10)
cupcakeEntry.insert(0,0)

spongecake=Label(cakelabelframe,text="Sponge Cake",font=("times new roman",13,'bold'),bg='light sea green',fg='black')
spongecake.grid(row=6,column=0,padx=20,pady=10,sticky='w')

spongecakeEntry=Entry(cakelabelframe,width=20)
spongecakeEntry.grid(row=6,column=1,padx=20,pady=10)
spongecakeEntry.insert(0,0)                                                                                               
cheesecake=Label(cakelabelframe,text="Cheese Cake",font=("times new roman",13,'bold'),bg='light sea green',fg='black')
cheesecake.grid(row=7,column=0,padx=20,pady=10,sticky='w')                                                                                                                                                                                                                                                                                                                                                                                                                          

cheesecakeEntry=Entry(cakelabelframe,width=20)
cheesecakeEntry.grid(row=7,column=1,padx=20,pady=10)
cheesecakeEntry.insert(0,0)

billarea=Frame(mainframe,bd=7,relief=GROOVE)
billarea.grid(row=0,column=3)

billarealabel=Label(billarea,text="Bill Area",font=('times new roman',15,'bold'),bd=7,relief=GROOVE)
billarealabel.pack(fill=X)

scrollbar=Scrollbar(billarea,orient=VERTICAL)
scrollbar.pack(side=RIGHT,fill=Y)
textarea=Text(billarea,height=22,width=60,yscrollcommand=scrollbar.set)
textarea.pack()
scrollbar.config(command=textarea.yview)

BillmenuFrame=LabelFrame(root,text="Cold Drinks",font=("times new roman",15,'bold'),fg='yellow',bg='Hotpink4',relief=GROOVE,bd=6)
BillmenuFrame.pack(pady=10,fill=X)

costofdrinks=Label(BillmenuFrame,text="Cost Of Milkshakes",font=('arial',13,'bold'),fg='white',bg='Hotpink4')
costofdrinks.grid(row=0,column=0,pady=9,padx=20,sticky='w')

costofdrinksEntry=Entry(BillmenuFrame,font=("times new roman",15,'bold'),width=10,border=7)
costofdrinksEntry.grid(row=0,column=1,padx=20,pady=9)
costofdrinksEntry.insert(0,0)

costofcakes=Label(BillmenuFrame,text="Cost of cakes",font=('arial',13,'bold'),fg='white',bg='Hotpink4')
costofcakes.grid(row=1,column=0,pady=9,padx=20,sticky='w')

costofcakesEntry=Entry(BillmenuFrame,font=("times new roman",15,'bold'),width=10,border=7)
costofcakesEntry.grid(row=1,column=1,padx=20,pady=9)
costofcakesEntry.insert(0,0)

costoffood=Label(BillmenuFrame,text="Cost Of Food",font=('arial',13,'bold'),fg='white',bg='Hotpink4')
costoffood.grid(row=2,column=0,pady=9,padx=20,sticky='w')

costoffoodEntry=Entry(BillmenuFrame,font=("times new roman",15,'bold'),width=10,border=7)
costoffoodEntry.grid(row=2,column=1,padx=20,pady=9)
costoffoodEntry.insert(0,0)

subtotal2=Label(BillmenuFrame,text="Sub Total",font=('arial',13,'bold'),fg='white',bg='Hotpink4')
subtotal2.grid(row=0,column=2,pady=9,padx=20,sticky='w')

subtotalEntry=Entry(BillmenuFrame,font=("times new roman",15,'bold'),width=10,border=7)
subtotalEntry.grid(row=0,column=3,padx=20,pady=9)
subtotalEntry.insert(0,0)

Servicetax=Label(BillmenuFrame,text="Service Tax",font=('arial',13,'bold'),fg='white',bg='Hotpink4')
Servicetax.grid(row=1,column=2,pady=9,padx=20,sticky='w')

ServicetaxEntry=Entry(BillmenuFrame,font=("times new roman",15,'bold'),width=10,border=7)
ServicetaxEntry.grid(row=1,column=3,padx=20,pady=9)
ServicetaxEntry.insert(0,0)

Totalcost=Label(BillmenuFrame,text="Total cost",font=('arial',13,'bold'),fg='white',bg='Hotpink4')
Totalcost.grid(row=2,column=2,pady=9,padx=20,sticky='w')

TotalcostEntry=Entry(BillmenuFrame,font=("times new roman",15,'bold'),width=10,border=7)
TotalcostEntry.grid(row=2,column=3,padx=20,pady=9)
TotalcostEntry.insert(0,0)

buttonFrame=Frame(BillmenuFrame,bd=7,relief=GROOVE)
buttonFrame.grid(row=0,column=4,rowspan=3)

totalButton=Button(buttonFrame,text="Total",font=("arial",15,'bold'),bg='Hotpink4',fg='white',bd=5,width=8,padx=27,pady=10,command=subtotal)
totalButton.grid(row=0,column=0,pady=20,padx=5)

billButton=Button(buttonFrame,text="Receipt",font=("arial",15,'bold'),bg='Hotpink4',fg='white',bd=5,width=8,padx=27,pady=10,command=receipt)
billButton.grid(row=0,column=1,pady=20,padx=5)

sendButton=Button(buttonFrame,text="Print",font=("arial",15,'bold'),bg='Hotpink4',fg='white',bd=5,width=8,padx=27,pady=10,command=printbilling)
sendButton.grid(row=0,column=2,pady=20,padx=5)

saveButton=Button(buttonFrame,text="Save",font=("arial",15,'bold'),bg='Hotpink4',fg='white',bd=5,width=8,padx=27,pady=10,command=save)
saveButton.grid(row=0,column=3,pady=20,padx=5)

clearButton=Button(buttonFrame,text="Clear",font=("arial",15,'bold'),bg='Hotpink4',fg='white',bd=5,width=8,padx=27,pady=10,command=clearall)
clearButton.grid(row=0,column=4,pady=20,padx=5)

thankyou=Label(root,text="LIVE TO EAT, LOVE TO LIVE!!",font=("times new roman",30,'bold'),bg='light sea green',fg='black',bd=5)
thankyou.pack(fill=X,pady=10)




root.geometry("1270x690+0+0")
#root.resizable(0,0)

root.mainloop()