from tkinter import *
T=Tk()#main window created
T.title("Demo")
T.geometry('400x400')
T.configure(bg='light pink')
L1=Label(text="Enter your name : ",fg='yellow',bg='blue')
E1=Entry(fg='white',bg='black',width=50)
L2=Label(text="Enter your age : ",fg='yellow',bg='blue')
E2=Entry(fg='white',bg='black',width=50)#single line

L3=Label(text="Enter your address : ",fg='yellow',bg='blue')

B1=Button(text="Submit",bg='red',fg='purple')
L1.pack()
E1.pack()
L2.pack()
E2.pack()
L3.pack()
B1.pack()

L1 = Label(master=T, text="Label 1:")
E1 = Entry(master=T, fg='white', bg='black', width=50)

L2 = Label(master=T, text="Label 2:")
E2 = Entry(master=T, fg='white', bg='black', width=50)

L3 = Label(master=T, text="Label 3:")
B1 = Button(master=T, text="Submit")

B1.grid(row=3, column=0)
T.mainloop()

PS C:\