#from  tkinter import *
#root=Tk()
#root.title("very basic calculator")
#mylabel=Label(root,text="hello world")
#mylabel.grid(row=1,column=14)
#function
#def myname():
#    lp=Label(root,text="hello"+name.get())
#    lp.grid(row=11,column=14)

#click=Button(root,text="enter your name",padx=50,pady=60,command=myname)
#name=Entry(root,width=50,fg="blue",bg="#FFC0CB")
#name.insert(0,"enter your name")
#click.grid(row=9,column=14)
#name.grid(row=10,column=14)
#root.mainloop()




#starting my calculator from here
from tkinter import colorchooser
from tkinter import *
import tkinter.font as font
root=Tk()
type=Entry(root,width=15,borderwidth=20,bg="#DE3163",font=('Arial 48'))
type.grid(row=1,column=1,columnspan=4)



#backend

def click(number):
    current=type.get()
    type.delete(0,END)
    type.insert(0,str(current)+str(number))
    

def clc():
    type.delete(0,END)
    
def add():
    number1=type.get()
    global f_num
    f_num=int(number1)
    type.delete(0,END)
    global math
    math="addition"
    
    return

def backspace():
    type.delete(0,END)
    
    
def equal():
    number2=type.get()
    type.delete(0,END)
    if(math=="addition"):
        type.insert(0,f_num+int(number2))
    elif math=="multiplication":
        type.insert(0,f_num*int(number2))
    elif math=="subtraction":
        type.insert(0,f_num-int(number2))

    elif math=="division":
        type.insert(0,f_num/int(number2))
    
    
    return
    
   

    
def mult():
    number1=type.get()
    global f_num
    f_num=int(number1)
    type.delete(0,END)
    global math
    math="multiplication"
    
    return


def div():
    number1=type.get()
    global f_num
    f_num=int(number1)
    type.delete(0,END)
    global math
    math="division"
    return


def subt():
    number1=type.get()
    global f_num
    f_num=int(number1)
    type.delete(0,END)
    global math
    math="subtraction"
    return
    
root.title("Aarushi's basic calculator")
font_size=font.Font(size=30)
font_size2=font.Font(size=20)
font_size3=font.Font(size=60)

#to give background color
# Call the function to display the color palette
#color=colorchooser.askcolor()

# Initialize the color range by picking up the first color
#colorname=color[1]

# Configure the background color
root.configure(background="#F987C5")

##label1=Label(root,text=" ",bg="#F987C5")
##label1.grid(row=1,column=2)
##label1['font']=font_size3

#frontend



button_clear=Button(root,text="clc",padx="25",pady="21",bg="#DE3163",command=clc)
button_clear.grid(row=2,column=1)
button_clear['font']=font_size

button_backspace=Button(root,text="backspace",padx="20",pady="10",bg="#DE3163",command=backspace)
button_backspace.grid(row=2,column=2,)
button_backspace['font']=font_size2

button_divide=Button(root,text="/",padx="25",pady="20",bg="#DE3163",command=div)
button_divide.grid(row=2,column=4)
button_divide['font']=font_size

button_7=Button(root,text="7",padx="30",pady="10",bg="#DE3163",command=lambda: click(7))
button_7.grid(row=3,column=1)
button_7['font']=font_size

button_8=Button(root,text="8",padx="30",pady="20",bg="#DE3163",command=lambda: click(8))
button_8.grid(row=3,column=2)
button_8['font']=font_size

button_9=Button(root,text="9",padx="30",pady="20",bg="#DE3163",command=lambda: click(9))
button_9.grid(row=3,column=3)
button_9['font']=font_size

button_multiply=Button(root,text="x",padx="25",pady="20",bg="#DE3163",command=mult)
button_multiply.grid(row=3,column=4)
button_multiply['font']=font_size

button_4=Button(root,text="4",padx="30",pady="20",bg="#DE3163",command=lambda: click(4))
button_4.grid(row=4,column=1)
button_4['font']=font_size


button_5=Button(root,text="5",padx="30",pady="20",bg="#DE3163",command=lambda: click(5))
button_5.grid(row=4,column=2)
button_5['font']=font_size

button_6=Button(root,text="6",padx="30",pady="20",bg="#DE3163",command=lambda: click(6))
button_6.grid(row=4,column=3)
button_6['font']=font_size




button_add=Button(root,text="+",padx="25",pady="20",bg="#DE3163",command=add)
button_add.grid(row=4,column=4,)
button_add['font']=font_size


button_1=Button(root,text="1",padx="30",pady="20",bg="#DE3163",command=lambda: click(1))
button_1.grid(row=5,column=1)
button_1['font']=font_size


button_2=Button(root,text="2",padx="30",pady="20",bg="#DE3163",command=lambda: click(2))
button_2.grid(row=5,column=2)
button_2['font']=font_size


button_3=Button(root,text="3",padx="30",pady="20",bg="#DE3163",command=lambda: click(3))
button_3.grid(row=5,column=3)
button_3['font']=font_size


button_subtract=Button(root,text="-",padx="30",pady="20",bg="#DE3163",command=subt)
button_subtract.grid(row=5,column=4)
button_subtract['font']=font_size


button_0=Button(root,text="0",padx="30",pady="20",bg="#DE3163",command=lambda: click(0))
button_0.grid(row=6,column=2)
button_0['font']=font_size


button_dot=Button(root,text=". ",padx="30",pady="20",bg="#DE3163",command=lambda: click("."))
button_dot.grid(row=6,column=3)
button_dot['font']=font_size


button_ans=Button(root,text="=",padx="25",pady="20",bg="#DE3163",command=equal)
button_ans.grid(row=6,column=4)
button_ans['font']=font_size


root.mainloop()
