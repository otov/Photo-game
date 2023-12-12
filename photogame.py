from tkinter import*
from PIL import ImageTk, Image
import random
photogame=Tk()

photogame.title("Image game")

bckimg=ImageTk.PhotoImage(Image.open("bckimg.jpg"))

btn1=Button(width=100,height=80,image=bckimg,bd=5)
btn2=Button(width=100,height=80,image=bckimg,bd=5)
btn3=Button(width=100,height=80,image=bckimg,bd=5)
btn4=Button(width=100,height=80,image=bckimg,bd=5)

btn5=Button(width=100,height=80,image=bckimg,bd=5)
btn6=Button(width=100,height=80,image=bckimg,bd=5)
btn7=Button(width=100,height=80,image=bckimg,bd=5)
btn8=Button(width=100,height=80,image=bckimg,bd=5)
btn9=Button(width=100,height=80,image=bckimg,bd=5)
btn10=Button(width=100,height=80,image=bckimg,bd=5)


btn1.grid(row=1,column=1,padx=2,pady=2)
btn2.grid(row=1,column=2,padx=2,pady=2)
btn3.grid(row=1,column=3,padx=2,pady=2)
btn4.grid(row=1,column=4,padx=2,pady=2)
btn5.grid(row=1,column=5,padx=2,pady=2)

btn6.grid(row=2,column=1,padx=2,pady=2)
btn7.grid(row=2,column=2,padx=2,pady=2)
btn8.grid(row=2,column=3,padx=2,pady=2)
btn9.grid(row=2,column=4,padx=2,pady=2)
btn10.grid(row=2,column=5,padx=2,pady=2)


img1=ImageTk.PhotoImage(Image.open("coke11.jpg"))
img2=ImageTk.PhotoImage(Image.open("fanta1.jpg"))
img3=ImageTk.PhotoImage(Image.open("peper1.jpg"))
img4=ImageTk.PhotoImage(Image.open("pepsi1.jpg"))
img5=ImageTk.PhotoImage(Image.open("sprite1.jpg"))

img1=ImageTk.PhotoImage(Image.open("coke11.jpg").resize((200,200)))
img2=ImageTk.PhotoImage(Image.open("fanta1.jpg").resize((200,200)))
img3=ImageTk.PhotoImage(Image.open("peper1.jpg").resize((200,200)))
img4=ImageTk.PhotoImage(Image.open("pepsi1.jpg").resize((200,200)))
img5=ImageTk.PhotoImage(Image.open("sprite1.jpg").resize((200,200)))

photogame.mainloop()