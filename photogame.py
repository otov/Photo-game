from tkinter import*
from PIL import ImageTK, Image
import random
photogame=Tk()

photogame.title("Image game")

btn1=Button(width=10,height=5)
btn2=Button(width=10,height=5)
btn3=Button(width=10,height=5)
btn4=Button(width=10,height=5)

btn5=Button(width=10,height=5)
btn6=Button(width=10,height=5)
btn7=Button(width=10,height=5)
btn8=Button(width=10,height=5)
btn9=Button(width=10,height=5)
btn10=Button(width=10,height=5)


btn1.grid(row=1,column=1,padx=5,pady=5)
btn2.grid(row=1,column=2,padx=5,pady=5)
btn3.grid(row=1,column=3,padx=5,pady=5)
btn4.grid(row=1,column=4,padx=5,pady=5)
btn5.grid(row=1,column=5,padx=5,pady=5)

btn6.grid(row=2,column=1,padx=5,pady=5)
btn7.grid(row=2,column=2,padx=5,pady=5)
btn8.grid(row=2,column=3,padx=5,pady=5)
btn9.grid(row=2,column=4,padx=5,pady=5)
btn10.grid(row=2,column=5,padx=5,pady=5)


img1=ImageTK.PhotoImage(Image.open("coke1.jpg"))
photogame.mainloop()