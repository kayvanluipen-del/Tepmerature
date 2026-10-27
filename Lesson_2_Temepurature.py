from tkinter import *

Gui_temp = Tk()
Gui_temp.config(background="white")
Gui_temp.title("Tempurature")
Gui_temp.geometry("600x400")
def convert():
    temp = input_Celsius.get()
    temp_fahrenheit = (float(temp)*9/5)+32
    output_Fahrenheit.config(text="Temperature in fahrenheit   :" + str(temp_fahrenheit))
title_label = Label(Gui_temp, text="Celsius -> Fahrenheit",bg= "white",fg= "black")
input_label = Label(Gui_temp, text= "Enter Temperature in Celsius   :",bg= "White", fg= "black")
input_Celsius = Entry()
output_Fahrenheit = Label(Gui_temp)
convert_button = Button(Gui_temp, text= "convert",width= 30, bg= "red", fg= "black", padx= 20, pady=10, command=convert)


title_label.grid(row=0,column=0)
input_label.grid(row=1,column=0)
input_Celsius.grid(row=1,column=1)
output_Fahrenheit.grid(row=3,column=0)
convert_button.grid(row=4,column=0)



Gui_temp.mainloop()