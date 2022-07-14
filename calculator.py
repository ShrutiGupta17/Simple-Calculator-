import tkinter as tk

def Addition():
  txt1 = int(box1.get())
  txt2 = int(box2.get())
  box3.insert(0,int(txt1+txt2))
  
def Substraction():
  txt1 = int(box1.get())
  txt2 = int(box2.get())
  box3.insert(0,int(txt1-txt2))
  
def Multiplication():
  txt1 = int(box1.get())
  txt2 = int(box2.get())
  box3.insert(0,int(txt1*txt2))
  
def Division():
  txt1 = int(box1.get())
  txt2 = int(box2.get())
  box3.insert(0,(txt1/txt2))
  
def Clear():
    box1.delete(0,tk.END)
    box2.delete(0,tk.END)
    box3.delete(0,tk.END)
app =  tk.Tk()
app.title("Calculator")
app.geometry("700x400")
app.iconbitmap("WhatsApp-Image-2022-03-30-at-22.20.02.jpg.ico")
app.resizable(False, False)

label1 = tk.Label(app, text = "Enter the first number:-", font = ("segoe",15))
label1.place(x = 20, y = 20)

label2 = tk.Label(app, text = "Enter the second number:-", font = ("segoe",15))
label2.place(x = 20 , y = 80)

label3 = tk.Label(app, text = "Result:-", font = ("segoe",15))
label3.place(x = 20 , y = 200)

button1 = tk.Button(app ,text = "+" ,font=("Arial",15),bg ="pink",command = Addition)
button1.place(x=80 , y= 150 , width = 70)

button2 = tk.Button(app ,text = "-" ,font=("Arial",15),bg ="pink",command = Substraction)
button2.place(x=180 , y= 150 , width = 70)

button3 = tk.Button(app ,text = "x" ,font=("Arial",15),bg ="pink",command = Multiplication)
button3.place(x=280 , y= 150 , width = 70)

button4 = tk.Button(app ,text = "/" ,font=("Arial",15),bg ="pink",command = Division)
button4.place(x=380 , y= 150 , width = 70)

button5 = tk.Button(app ,text = "CE" ,font=("Arial",12),bg ="silver",command = Clear)
button5.place(x=480 , y= 150 , width = 70)


box1 = tk.Entry(app,font = ("segoe",25),bg = "#D3D3D3")
box1.place(x=300 ,y=20)

box2 = tk.Entry(app,font = ("segoe",25),bg = "#D3D3D3")
box2.place(x=300 ,y=80)

box3 = tk.Entry(app,font = ("segoe",25),bg = "#D3D3D3")
box3.place(x= 300,y=200)



#img = tk.photolabel(file= "")
#label = tk.label(image = img )
#label.place(x= 575 , y= 50)
app.mainloop()
