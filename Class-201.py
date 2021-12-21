from tkinter import *
window=Tk()

def calculate_BMI():
    weight = float(weight_entry.get())
    height = float(height_entry.get())/100
    
    bmi = weight/height**2
    bmi = round(bmi,1)
    
    user_name = username.get()
    
    msg = ''
    if bmi<18.5:
        msg = "You are Under Weight"
    elif bmi>=18.5 and bmi<=24.9:
        msg = "You are Normal Weight"
    elif bmi>24.9 and bmi <30:
        msg = "You are Over Weight"
    elif bmi>=30.0:
        msg = "You are Obiese"
    else:
        msg = "Something Went Wrong"
    msg = user_name+" your BMI is "+str(bmi)+", "+msg
    
    outputmsg = Label(result_frame,text=msg,bg = "lightcyan", font=("Calibri", 12), width=33).place(x=20,y=300)
    outputmsg.pack()

window.title('BMI Calculator')
window.geometry("380x400")
window.configure(bg='lightcyan')


app_label=Label(window, text="BMI CALCULATOR", fg = "black", bg = "lightcyan", font=("Calibri", 20),bd=5)
app_label.place(x=50, y=20)

name_label=Label(window, text="Your Name:", fg = "black", bg = "lightcyan", font=("Calibri", 12),bd=1).place(x=20, y=90)
username=Entry(window, text="", bd=2, width=22).place(x=170, y=90)

weight_label=Label(window, text="Your Weight (in Kg):", fg = "black", bg = "lightcyan", font=("Calibri", 12),bd=1).place(x=20, y=120)
weight_entry=Entry(window, text="", bd=2, width=22).place(x=170, y=120)

height_label=Label(window, text="Your Height (in cm):", fg = "black", bg = "lightcyan", font=("Calibri", 12),bd=1).place(x=20, y=150)
height_entry=Entry(window, text="", bd=2, width=22).place(x=170, y=150)

calculate_button = Button(window,text="Calculate BMI",fg = "black", bg = "lightcyan", font=("Calibri", 12),bd=1,command=calculate_BMI).place(x=130, y=175)

result_frame = LabelFrame(window,text="Result", bg = "lightcyan", font=("Calibri", 12))
result_frame.pack(padx=20, pady=20)
result_frame.place(x=20,y=300)

result_label=Label(result_frame,text=" ", bg = "lightcyan", font=("Calibri", 12), width=33)
result_label.place(x=20,y=20)
result_label.pack()

window.mainloop()
