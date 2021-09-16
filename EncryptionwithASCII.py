# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 17:59:41 2021

@author: Adarsh
"""

from tkinter import *

#Uncomment the following line if you have MacOS
#Ask the student to write the following line if the student has MacOS

#from tkmacosx import *

root=Tk()
root.title("Encyption With Ascii")

root.geometry("400x400")
root.configure(background = 'pink')

enter_word = Entry(root)
enter_word.place(relx=0.5,rely=0.4,anchor=CENTER)

label = Label(root, text = "Name in Ascii : ", bg="purple", fg="white")
label2 = Label(root, text = "Encrypted Name : ", bg="purple", fg="white")

def asciiConverter():
    input_word = enter_word.get()
    
    for letter in input_word :
        label["text"] += str(ord(letter)) + "  "
        asciicode = int(ord(letter))
        encrypted = asciicode - 1
        label2["text"] += str(chr(encrypted))
        
btn=Button(root,text="Show ASCII Code and Encrypted Name",command=asciiConverter, bg='blue', fg = 'white')
btn.place(relx=0.5,rely=0.5,anchor=CENTER)

label.place(relx=0.5,rely=0.6,anchor=CENTER)
label2.place(relx=0.5,rely=0.7,anchor=CENTER)

root.mainloop()

