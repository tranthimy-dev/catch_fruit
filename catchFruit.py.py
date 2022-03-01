from tkinter import*
from tkinter import messagebox
from time import sleep
from PIL import ImageTk, Image
from random import randint
from playsound import playsound

img=[0,0,0,0,0,0,0,0,0]

y=-20
x_apple=randint(10,690)
x_diamond=randint(10,690)
x_orange=randint(10,690)
x_boom=randint(10,690)
x_doubleFruit=randint(10,690)
x_greenApple=randint(10,690)
x_firecrackers=randint(10,690)

game=Tk()
Button(game, text="Quit", command=game.destroy).pack()
game.title("Catch Fruit")
canvas=Canvas(master=game, width=700, height=525, background="white")
canvas.pack()

img[0]=ImageTk.PhotoImage(Image.open("backgr.png"))
img[1]=ImageTk.PhotoImage(Image.open("nobita.png"))
img[2]=ImageTk.PhotoImage(Image.open("apple.png"))
img[3]=ImageTk.PhotoImage(Image.open("diamond.png"))
img[4]=ImageTk.PhotoImage(Image.open("orange.png"))
img[5]=ImageTk.PhotoImage(Image.open("boom.png"))
img[6]=ImageTk.PhotoImage(Image.open("doubleFruit.png"))
img[7]=ImageTk.PhotoImage(Image.open("greenApple.png"))
img[8]=ImageTk.PhotoImage(Image.open("firecrackers.png"))

background= canvas.create_image(0,0, anchor=NW, image=img[0])
nobita= canvas.create_image(0,400, anchor=NW, image=img[1])
apple= canvas.create_image(x_apple,y, anchor=NW, image=img[2])
diamond= canvas.create_image(x_diamond,y, anchor=NW, image=img[3])
orange= canvas.create_image(x_orange,y, anchor=NW, image=img[4])
boom= canvas.create_image(x_boom,y, anchor=NW, image=img[5])
doubleFruit= canvas.create_image(x_doubleFruit,y, anchor=NW, image=img[6])
greenApple= canvas.create_image(x_greenApple,y, anchor=NW, image=img[7])
firecrackers= canvas.create_image(x_firecrackers,y, anchor=NW, image=img[8])

canvas.update()

gameOver=False
score = 0
text_score=canvas.create_text(620,30, text= "SCORE:" +str(score), fill="red", font=("Times",20))

def TraiCay():
    global apple, diamond, orange, boom, doubleFruit, greenApple, firecrackers,  score, gameOver

    canvas.move(apple,0,10)
    if canvas.coords(apple)[1]>550:
        canvas.delete(apple)
        y=-20
        x_apple=randint(10, 690)
        apple= canvas.create_image(x_apple,y, anchor=NW, image=img[2])
    if  (canvas.coords(apple)[0]>=canvas.coords(nobita)[0] and canvas.coords(apple)[0]
        +50<=canvas.coords(nobita)[0]+ 100) and (canvas.coords(apple)[1]
        +51>=canvas.coords(nobita)[1] and canvas.coords(apple)[1]+51<= canvas.coords(nobita)[1]+65):
        playsound('score.mp3')
        canvas.delete(apple)
        y=-20
        x_apple=randint(10, 690)
        apple= canvas.create_image(x_apple,y, anchor=NW, image=img[2])
        score = score + 1
        canvas.itemconfig(text_score, text= "SCORE:" +str(score))
        
    canvas.move(diamond,0,10)
    if canvas.coords(diamond)[1]>550:
        canvas.delete(diamond)
        y=-20
        x_diamond=randint(10, 690)
        diamond= canvas.create_image(x_diamond,y, anchor=NW, image=img[3])
    if  (canvas.coords(diamond)[0]>=canvas.coords(nobita)[0] and canvas.coords(diamond)[0]
        +40<=canvas.coords(nobita)[0]
        +100) and (canvas.coords(diamond)[1]+40>=canvas.coords(nobita)[1] and canvas.coords(diamond)[1]+40<= canvas.coords(nobita)[1]+65):
        playsound('score.mp3')
        canvas.delete(diamond)
        y=-20
        x_diamond=randint(10, 690)
        diamond= canvas.create_image(x_diamond,y, anchor=NW, image=img[3])
        score = score + 4
        canvas.itemconfig(text_score, text= "SCORE:" +str(score))
       
       
    canvas.move(orange,0,10)
    if canvas.coords(orange)[1]>550:
        canvas.delete(orange)
        y=-20
        x_orange=randint(10, 690)
        orange= canvas.create_image(x_orange,y, anchor=NW, image=img[4])
    if  (canvas.coords(orange)[0]>=canvas.coords(nobita)[0] and canvas.coords(orange)[0]+50<=canvas.coords(nobita)[0]
     + 100) and (canvas.coords(orange)[1]+50>=canvas.coords(nobita)[1] and canvas.coords(orange)[1]+50<= canvas.coords(nobita)[1]+65):
        playsound('score.mp3')
        canvas.delete(orange)
        y=-20
        x_orange=randint(10, 690)
        orange= canvas.create_image(x_orange,y, anchor=NW, image=img[4])
        score = score + 1
        canvas.itemconfig(text_score, text= "SCORE:" +str(score))
       
       
    canvas.move(boom,0,10)
    if canvas.coords(boom)[1]>550:
        canvas.delete(boom)
        y=-20
        x_boom=randint(10, 690)
        boom = canvas.create_image(x_boom,y, anchor=NW, image=img[5])
    if  (canvas.coords(boom)[0]>=canvas.coords(nobita)[0] and canvas.coords(boom)[0]+50<=canvas.coords(nobita)[0]
     + 100) and (canvas.coords(boom)[1]+51>=canvas.coords(nobita)[1] and canvas.coords(boom)[1]+51<= canvas.coords(nobita)[1]+65):
        playsound('bom.mp3')
        canvas.delete(boom)
        y=-20
        x_boom=randint(10, 690)
        boom= canvas.create_image(x_boom,y, anchor=NW, image=img[5])
        score = score - 5
        canvas.itemconfig(text_score, text= "SCORE:" +str(score))
        if score < 0:
            gameOver=True
            messagebox.showinfo("Alert", "Game Over")
        

    canvas.move(doubleFruit,0,10)
    if canvas.coords(doubleFruit)[1]>550:
        canvas.delete(doubleFruit)
        y=-20
        x_doubleFruit=randint(10, 690)
        doubleFruit= canvas.create_image(x_doubleFruit,y, anchor=NW, image=img[6])
    if  (canvas.coords(doubleFruit)[0]>=canvas.coords(nobita)[0] and canvas.coords(doubleFruit)[0]
        +50<=canvas.coords(nobita)[0]+ 100) and (canvas.coords(doubleFruit)[1]
        +50>=canvas.coords(nobita)[1] and canvas.coords(doubleFruit)[1]+50<= canvas.coords(nobita)[1]+65):
        playsound('score.mp3')
        canvas.delete(doubleFruit)
        y=-20
        x_doubleFruit=randint(10, 690)
        doubleFruit= canvas.create_image(x_doubleFruit,y, anchor=NW, image=img[6])
        score = score + 2
        canvas.itemconfig(text_score, text= "SCORE:" +str(score))
        
        

    canvas.move(greenApple,0,10)
    if canvas.coords(greenApple)[1]>550:
        canvas.delete(greenApple)
        y=-20
        x_greenApple=randint(10, 690)
        greenApple= canvas.create_image(x_greenApple,y, anchor=NW, image=img[7])
    if  (canvas.coords(greenApple)[0]>=canvas.coords(nobita)[0] and canvas.coords(greenApple)[0]
        +50<=canvas.coords(nobita)[0]+ 100) and (canvas.coords(greenApple)[1]
        +60>=canvas.coords(nobita)[1] and canvas.coords(greenApple)[1]+60<= canvas.coords(nobita)[1]+65):
        playsound('score.mp3')
        canvas.delete(greenApple)
        y=-20
        x_greenApple=randint(10, 690)
        greenApple= canvas.create_image(x_greenApple,y, anchor=NW, image=img[7])
        score = score + 1
        canvas.itemconfig(text_score, text= "SCORE:" +str(score))
       
        

    canvas.move(firecrackers,0,10)
    if canvas.coords(firecrackers)[1]>550:
        canvas.delete(firecrackers)
        y=-20
        x_firecrackers=randint(10, 690)
        firecrackers= canvas.create_image(x_firecrackers,y, anchor=NW, image=img[8])
    if  (canvas.coords(firecrackers)[0]>=canvas.coords(nobita)[0] and canvas.coords(firecrackers)[0]
        +50<=canvas.coords(nobita)[0]+ 100) and (canvas.coords(firecrackers)[1]
        +50>=canvas.coords(nobita)[1] and canvas.coords(firecrackers)[1]+50<= canvas.coords(nobita)[1]+65):
        playsound('bom.mp3')
        canvas.delete(firecrackers)
        y=-20
        x_firecrackers=randint(10, 690)
        firecrackers= canvas.create_image(x_firecrackers,y, anchor=NW, image=img[8])
        score = score - 3
        canvas.itemconfig(text_score, text= "SCORE:" +str(score))
        if score < 0:
            gameOver=True
            messagebox.showinfo("Alert", "Game Over")
            
        
    canvas.update()

def right():
    global nobita
    if canvas.coords(nobita)[0]<650:
        canvas.move(nobita,20,0)
    canvas.update()

def left():
    global nobita
    if canvas.coords(nobita)[0]>-10:
        canvas.move(nobita,-20,0)
    canvas.update()

def keyPress (event):
    if event.keysym=="Right":
        right()
    if event.keysym=="Left":
        left()
canvas.bind_all("<KeyPress>", keyPress)
while not gameOver:
    TraiCay()
    sleep(0.04)
    
game.mainloop()
