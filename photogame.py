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


def btnclick(btn,number):
    global count,correctAnswer,answers,answer_dict
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
                correctAnswer==0
            #if correctAnswer==5:
                #messagebox.showinfo("All images are matching, YOU WON!")
            else:
                messagebox.showinfo("NOT matching images", "INCORRECT!")
                for key in answer_dict:
                    key["Image"]="pyimage5"
            count=0
            answers=[]
            answer_dict={}

    return 0

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

img1=ImageTk.PhotoImage(Image.open("coke11.jpg").resize((200,200)))
img2=ImageTk.PhotoImage(Image.open("fanta1.jpg").resize((200,200)))
img3=ImageTk.PhotoImage(Image.open("peper1.jpg").resize((200,200)))
img4=ImageTk.PhotoImage(Image.open("pepsi1.jpg").resize((400,200)))
img5=ImageTk.PhotoImage(Image.open("sprite1.jpg").resize((200,200)))


Imagelist=[img1,img1,img2,img2,img3,img3,img4,img4,img5,img5]
random.shuffle(Imagelist)

photogame.mainloop()