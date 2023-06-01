from tkinter import *

root = Tk()

#To change title of the calculator name use function below
root.title("Basic Calculator")

#Make an entry text box
e = Entry(root, width=35, borderwidth= 5)

e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

#define button_add
def button_add(variable):
    return

#Create 9 button functions.
#WE can call button 1  press_1
#Button will go into root
#We want it to say 1 so we put  text = "1"
#create padx and pady functions for the size of the button

press_1 = Button(root, text = "1", padx= 40, pady= 20, command=lambda: button_add(1)) #lambda is a function that allows you to pass in numbers or arguements to the expression
#Now do the same for 2-9
press_2 = Button(root, text = "2", padx= 40, pady= 20, command= lambda: button_add(2))
press_3 = Button(root, text = "3", padx= 40, pady= 20, command= lambda: button_add(3))
press_4 = Button(root, text = "4", padx= 40, pady= 20, command= lambda: button_add(4))
press_5 = Button(root, text = "5", padx= 40, pady= 20, command= lambda: button_add(5))
press_6 = Button(root, text = "6", padx= 40, pady= 20, command= lambda: button_add(6))
press_7 = Button(root, text = "7", padx= 40, pady= 20, command= lambda: button_add(7))
press_8 = Button(root, text = "8", padx= 40, pady= 20, command= lambda: button_add(8))
press_9 = Button(root, text = "9", padx= 40, pady= 20, command= lambda: button_add(9))
press_0 = Button(root, text = "0", padx= 40, pady= 20, command= lambda: button_add(0))


#The 3 functions below will put addition(+) button and The equal(=) and also division(/) and multiplication(x)
button_add = Button(root, text = "+", padx= 35, pady= 25, command= button_add)
button_equal = Button(root, text = "=", padx= 95, pady= 20, command= button_add)
button_div = Button(root, text = "/", padx= 95 , pady= 25 , command= button_add)
button_mult = Button(root, text = "*", padx= 95 , pady= 25 , command= button_add)
#This function below will clear out all the numbers on the calculator
button_clear = Button(root, text = "Clear", padx= 75, pady= 20, command= button_add)


#Below will put the buttons on the screen
press_1.grid(row=1 , column=0)
press_2.grid(row=1 , column=1)
press_3.grid(row=1 , column=2)

press_4.grid(row=2 , column=0)
press_5.grid(row=2 , column=1)
press_6.grid(row=2 , column=2)

press_7.grid(row=3 , column=0)
press_8.grid(row=3 , column=1)
press_9.grid(row=3 , column=2)

press_0.grid(row=4 , column=0)

#Now this will put the clear,add, and equal on the screen. The columspan will make sure how many how row or columns the button will be in.
#With columnspan 0 and clear will be next to eachother since their on the same row, same for add and equal.
button_clear.grid(row=4, column=0, columnspan=2)
button_add.grid(row=5 , column= 0)
button_equal.grid(row=5 , column= 1 , columnspan=2)
button_div.grid(row=6, column= 1 )
button_mult.grid(row=6, column= 2)
root.mainloop()
