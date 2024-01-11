
from tkinter import*
from PIL import ImageTk, Image
from tkinter import messagebox
import random
photogame=Tk()


photogame.title("Image game")


bckimg=ImageTk.PhotoImage(Image.open("zbckimage2.jpg"))

count=0
correctAnswer=0
answers=[]
answer_dict={}
countwin=0

def btnclick(btn,number):
    global count,correctAnswer,answers,answer_dict,countwin
    if btn["image"]=="pyimage1"and count<2:
        btn["image"]=Imagelist[number]
        count+=1
        answers.append(number)
        answer_dict[btn]=Imagelist[number]
    if len(answers)==2:
        if Imagelist[answers[0]]==Imagelist[answers[1]]:
            for key in answer_dict:
                key["state"]=DISABLED
            correctAnswer+=2
            if correctAnswer==2:
                messagebox.showinfo("Matching images", "CONGRATS!")
                correctAnswer=0
                countwin+=1
            if countwin==5:
                messagebox.showinfo("All images are matching", "YOU WON!")
        else:
            messagebox.showinfo("NOT matching images", "INCORRECT!")
            for key in answer_dict:
                key["image"]="pyimage1"
        count=0
        answers=[]
        answer_dict={}

    return 0

def infowindow():
    photogame=Toplevel()
    photogame.title("Rules")
    photogame.geometry("500x500")
    Rules=Label(photogame,text="Game rules")
    Rules.grid(row=0,column=0)

    return 0

def reset():
    global count,correctAnswer,answers,answer_dict,countwin
    count=0 
    correctAnswer=0
    answers=0
    answer_dict=0
    countwin=0
    btn0.config(state=NORMAL)
    btn1.config(state=NORMAL)
    btn2.config(state=NORMAL)
    btn3.config(state=NORMAL)
    btn4.config(state=NORMAL)
    btn5.config(state=NORMAL)
    btn6.config(state=NORMAL)
    btn7.config(state=NORMAL)
    btn8.config(state=NORMAL)
    btn9.config(state=NORMAL)

    btn0["image"]="pyimage1"
    btn1["image"]="pyimage1"
    btn2["image"]="pyimage1"
    btn3["image"]="pyimage1"
    btn4["image"]="pyimage1"
    btn5["image"]="pyimage1"
    btn6["image"]="pyimage1"
    btn7["image"]="pyimage1"
    btn8["image"]="pyimage1"
    btn9["image"]="pyimage1"

    count=0
    correctAnswer=0
    answers=[]
    answer_dict={}
    
    random.shuffle(Imagelist)

    return 0

mainmenu=Menu(photogame)
photogame.config(menu=mainmenu)

options=Menu(mainmenu,tearoff=False)
mainmenu.add_cascade(label="Options",menu=options)

options.add_cascade(label="New game",command=reset)
options.add_cascade(label="Exit game",command=photogame.quit)

mainmenu.add_command(label="About the game",command=infowindow)






btn0=Button(width=150,height=150,image=bckimg,bd=2,command=lambda:btnclick(btn0,0))
btn1=Button(width=150,height=150,image=bckimg,bd=2,command=lambda:btnclick(btn1,1))
btn2=Button(width=150,height=150,image=bckimg,bd=2,command=lambda:btnclick(btn2,2))
btn3=Button(width=150,height=150,image=bckimg,bd=2,command=lambda:btnclick(btn3,3))
btn4=Button(width=150,height=150,image=bckimg,bd=2,command=lambda:btnclick(btn4,4))

btn5=Button(width=150,height=150,image=bckimg,bd=2,command=lambda:btnclick(btn5,5))
btn6=Button(width=150,height=150,image=bckimg,bd=2,command=lambda:btnclick(btn6,6))
btn7=Button(width=150,height=150,image=bckimg,bd=2,command=lambda:btnclick(btn7,7))
btn8=Button(width=150,height=150,image=bckimg,bd=2,command=lambda:btnclick(btn8,8))
btn9=Button(width=150,height=150,image=bckimg,bd=2,command=lambda:btnclick(btn9,9))


btn0.grid(row=1,column=1,padx=2,pady=2)
btn1.grid(row=1,column=2,padx=2,pady=2)
btn2.grid(row=1,column=3,padx=2,pady=2)
btn3.grid(row=1,column=4,padx=2,pady=2)
btn4.grid(row=1,column=5,padx=2,pady=2)

btn5.grid(row=2,column=1,padx=2,pady=2)
btn6.grid(row=2,column=2,padx=2,pady=2)
btn7.grid(row=2,column=3,padx=2,pady=2)
btn8.grid(row=2,column=4,padx=2,pady=2)
btn9.grid(row=2,column=5,padx=2,pady=2)


img1=ImageTk.PhotoImage(Image.open("coke11.jpg"))
img2=ImageTk.PhotoImage(Image.open("fanta1.jpg"))
img3=ImageTk.PhotoImage(Image.open("peper1.jpg"))
img4=ImageTk.PhotoImage(Image.open("pepsi1.jpg"))
img5=ImageTk.PhotoImage(Image.open("sprite1.jpg"))

img1=ImageTk.PhotoImage(Image.open("coke11.jpg").resize((300,200)))
img2=ImageTk.PhotoImage(Image.open("fanta1.jpg").resize((300,200)))
img3=ImageTk.PhotoImage(Image.open("peper1.jpg").resize((300,200)))
img4=ImageTk.PhotoImage(Image.open("pepsi1.jpg").resize((500,200)))
img5=ImageTk.PhotoImage(Image.open("sprite1.jpg").resize((300,200)))


Imagelist=[img1,img1,img2,img2,img3,img3,img4,img4,img5,img5]
random.shuffle(Imagelist)

photogame.mainloop()