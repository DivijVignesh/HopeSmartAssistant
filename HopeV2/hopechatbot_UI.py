from tkinter import *
root=Tk()

root.title('Hope ChatBot')

root.geometry('400x500')

#creating a main menu
main_menu = Menu(root)

#creating a submenu in main menu
file_menu = Menu(root)

file_menu.add_command(label='New..')
file_menu.add_command(label='Save As..')
file_menu.add_command(label='Exit..')

main_menu.add_cascade(label= 'File',menu=file_menu)
main_menu.add_command(label= 'Edit')
main_menu.add_command(label= 'Quit')
root.config(menu=main_menu)

#creating a chat window
chatWindow= Text(root, bd=1 , bg='black',  width=50, height=8)
chatWindow.place(x=6,y=6,height=385 ,width=370)


#creating the message window
messageWindow = Text(root, bg='white',  width=30, height=4)
messageWindow.place(x=128,y=400,height=88 ,width=260)
# message1=messageWindow.Entry(root)

#creating a button
Button=Button(root, text='Send' , bg='blue',activebackground='light blue', width=12, height=5,font=('Arial',12))
Button.place(x=6, y=400, height=88,width=120)

#creating scrolling bar
scrollbar=Scrollbar(root, command=chatWindow.yview())
scrollbar.place(x=375,y=5, height= 385)


root.mainloop()