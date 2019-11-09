from tkinter import *
import math

def leftClickButton(event):
    BMI = (float(textBoxWeight.get())/math.pow(float(textBoxHight.get())/100,2))
    labelResult.configure(text=BMI)
    if BMI > 30:
        labelResultThai.configure(text="อ้วนมาก")
    elif BMI > 25:
        labelResultThai.configure(text="อ้วน")
    elif BMI > 23:
        labelResultThai.configure(text="น้ำหนักเกิน")
    elif BMI > 18.6:
        labelResultThai.configure(text="น้ำหนักปกติ")
    elif BMI < 18.5:
        labelResultThai.configure(text="ผอมเกินไป")

mainWindow = Tk()
labelHight = Label(mainWindow,text="ส่วนสูง (เซนติเมตร)")
labelHight.grid(row=0,column=0)
textBoxHight = Entry(mainWindow)
textBoxHight.grid(row=0,column=1)
labelWeight = Label(mainWindow,text="น้ำหนัก (กิโลกรัม)")
labelWeight.grid(row=1,column=0)
textBoxWeight = Entry(mainWindow)
textBoxWeight.grid(row=1,column=1)
calculateButton = Button(mainWindow,text="คำนวณ")
calculateButton.bind('<Button-1>',leftClickButton)
calculateButton.grid(row=2,column=0)
labelResult = Label(mainWindow,text="ผลลัพธ์")
labelResult.grid(row=2,column=1)
labelResultThai = Label(mainWindow,text="เกณฑ์")
labelResultThai.grid(row=3,column=1)

mainWindow.mainloop()