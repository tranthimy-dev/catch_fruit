from tkinter import*
#Từ thư viện Tkinter import các hàm của nó vào
from tkinter import messagebox
# Dùng hàm sleep trong thư viện time để delay hay trì hoãn thời gian cho hành động. 
#giả sử như quả táo rơi thì có thể quan sát đc
from time import sleep
#Từ thư viện pillow import 2 hàm là ImageTK và Image để sử dụng
from PIL import ImageTk, Image
#Sủ dụng hàm random để lấy ngẫu nhiên, randint để lấy giá trị ngẫu nhiên số nguyên
from random import randint
#Thư viện playsound để phát ra âm thanh
from playsound import playsound
#Lưu ý: Có 3 thư viện tkinter, pillow, playsound phải cài đặt nếu không sẽ báo lỗi.

#Đưa ảnh vào, khởi tạo 1 list, có 9 ảnh thì gồm 9 phần tử
img=[0,0,0,0,0,0,0,0,0]

#y ngoài màn hình nên lấy giá trị âm
y=-20
#x lấy ngẫu nhiên từ 0-700. Đặt 10-690 để cách mép màn hình
#Dùng hàm randint để rơi ngẫu nhiên nên phải để mỗi ảnh 1 tên biến khác nhau 
# bởi vì nếu mà để giống nhau thì nó sẽ rơi đè lên nhau
x_apple=randint(10,690)
x_diamond=randint(10,690)
x_orange=randint(10,690)
x_boom=randint(10,690)
x_doubleFruit=randint(10,690)
x_greenApple=randint(10,690)
x_firecrackers=randint(10,690)

#Tạo cửa sổ game
game=Tk()

Button(game, text="Quit", command=game.destroy).pack()

#Đặt tiêu đề cho game
game.title("Catch Fruit")

#Màn hình chơi game:Rộng 700, cao 525, background màu trắng
canvas=Canvas(master=game, width=700, height=525, background="white")
#canvas.pack() ghim màn hình vào trong cửa sổ game
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

#create_image để vẽ ảnh

#background tọa độ 0,0
background= canvas.create_image(0,0, anchor=NW, image=img[0])
#nobita tọa độ 0,420
nobita= canvas.create_image(0,400, anchor=NW, image=img[1])
#y sẽ cho ra màn hình nên để âm. ở đây gán y=-20 x lấy ngẫu nhiên 0-700
apple= canvas.create_image(x_apple,y, anchor=NW, image=img[2])
diamond= canvas.create_image(x_diamond,y, anchor=NW, image=img[3])
orange= canvas.create_image(x_orange,y, anchor=NW, image=img[4])
boom= canvas.create_image(x_boom,y, anchor=NW, image=img[5])
doubleFruit= canvas.create_image(x_doubleFruit,y, anchor=NW, image=img[6])
greenApple= canvas.create_image(x_greenApple,y, anchor=NW, image=img[7])
firecrackers= canvas.create_image(x_firecrackers,y, anchor=NW, image=img[8])

#update các thay đổi
canvas.update()

#giá trị khởi đầu của gameOver = false
gameOver=False

#Tạo biến score để lưu điểm số, gán giá trị khởi đầu bằng 0
score = 0
#Tạo text và đặt tại vị trí có tọa độ x=620 và y =30 có tên là score và + str của biến score
#Vì biến score là biến số, muốn cộng được với biến chuỗi phải chuyển sang string, màu chữ là đỏ và phông chữ là time, cỡ chữ 20

text_score=canvas.create_text(620,30, text= "SCORE:" +str(score), fill="red", font=("Times",20))

#Xây dựng hàm cho quả táo rơi
def TraiCay():
    #Khai báo biến toàn cục
    global apple, diamond, orange, boom, doubleFruit, greenApple, firecrackers, score, gameOver

    #Khi quả táo rơi từ trên xuống tức là y tăng dần, dùng canvas.move x giữ nuyên, y tăng 10
    canvas.move(apple,0,10)
    #Nếu tọa độ y của quả táo lớn hơn từ 525 trở lên tức là ra khỏi màn hình (x táo =0 y táo =1 nên để [1])
    if canvas.coords(apple)[1]>550:
        #xóa quả táo 
        canvas.delete(apple)
        #tạo và vẽ lại quả táo 
        #quả táo vẫn rơi từ trên xuống nên y = giá trị âm để ra ngoài màn hình. ở đây gán y=-20 x lấy ngẫu nhiên 0-700
        y=-20
        x_apple=randint(10, 690)
        apple= canvas.create_image(x_apple,y, anchor=NW, image=img[2])
        #phải có canvas.update thì mới update được thay đổi. 
    
    #Nếu tọa độ x của quả táo >= tọa độ x của Nobita và tọa độ x của quả táo + 50<= tọa độ x của quả táo 100
    #Nếu tọa độ y của quả táo +51 >= tọa độ y của Nobita và tọa độ y của quả táo + 51<= tọa độ y của quả táo + 65
    if  (canvas.coords(apple)[0]>=canvas.coords(nobita)[0] and canvas.coords(apple)[0]
        +50<=canvas.coords(nobita)[0]+ 100) and (canvas.coords(apple)[1]
        +51>=canvas.coords(nobita)[1] and canvas.coords(apple)[1]+51<= canvas.coords(nobita)[1]+65):

        #Sau khi va chạm sẽ phát ra âm thanh
        playsound('score.mp3')
        #Sau khi va chạm, phát ra âm thanh thì sẽ xóa quả táo đi
        canvas.delete(apple)
        #và tạo lại quả táo
        y=-20
        x_apple=randint(10, 690)
        apple= canvas.create_image(x_apple,y, anchor=NW, image=img[2])

        #Mỗi lần quả táo chạm vào Nobita điểm số sẽ tăng lên 1
        score = score + 1
        #Nếu điểm <0 thì gameover
        if score < 0:
            gameOver=True
            #Hiện lên messagebox GameOver
            messagebox.showinfo("Alert", "Game Over")
        #update lại điểm số
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
        if score < 0:
            gameOver=True
            messagebox.showinfo("Alert", "Game Over")
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
        if score < 0:
            gameOver=True
            messagebox.showinfo("Alert", "Game Over")
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
        if score < 0:
            gameOver=True
            messagebox.showinfo("Alert", "Game Over")
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
        if score < 0:
            gameOver=True
            messagebox.showinfo("Alert", "Game Over")
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

#Xây dựng hàm di chuyển của Nobita

#Hàm di chuyển sang phải
def right():
    global nobita
      #xét tọa độ x Nobita
    if canvas.coords(nobita)[0]<650:
        #move để di chuyển nobita có x=20, y=0
        canvas.move(nobita,20,0)
    canvas.update()

#Hàm di chuyển sang trái
def left():
    global nobita
    if canvas.coords(nobita)[0]>-10:
        #move để di chuyển nobita có x=-20, y=0
        canvas.move(nobita,-20,0)
    canvas.update()

#Xây dựng hàm sự kiện
def keyPress (event):
    #Nếu sự kiện == right thì thực hiện hàm right
    if event.keysym=="Right":
        right()
    if event.keysym=="Left":
        left()
#lệnh canvas.bind_all để gắn sk nhấn phím vào hàm keyPress
canvas.bind_all("<KeyPress>", keyPress)

#Để hàm trái cây chạy
#Trong khi chưa kết thúc game thì hàm trái cây sử dụng sleep để delay 0.04s
while not gameOver:
    TraiCay()
    sleep(0.04)

#phải có mới chạy đc game 
game.mainloop()
