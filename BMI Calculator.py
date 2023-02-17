'''
By:Sabin Poudel
Date:17/02/2023
This GUI takes weight in kg and height in meter and calculates BMI 
'''
import tkinter as tk
from tkinter import ttk
class Calculator:
    def __init__(self):
        root=tk.Tk()
        #----title-------#
        root.title("BMI Calculator")
        root.iconbitmap()
        #---icon---#
        root.iconbitmap('icon.ico')
        #----dimensions---#
        root.geometry("250x250")
        root.maxsize(250,250)
        root.minsize(250,250)
        #---weight----#
        weight_var=tk.StringVar()
        weight_label=tk.Label(root,text="Weight(KG): ",padx=10,pady=10)
        weight_label.grid(row=0,column=0,sticky=tk.W)
        weight_entry=tk.Entry(root,textvariable=weight_var,width=25)
        weight_entry.grid(row=0,column=1,sticky=tk.W)
        weight_entry.focus()
        #---height----#
        height_var=tk.StringVar()
        height_label=tk.Label(root,text="Height(m): ",padx=10,pady=10)
        height_label.grid(row=1,column=0,sticky=tk.W)
        height_entry=tk.Entry(root,textvariable=height_var,width=25)
        height_entry.grid(row=1,column=1,sticky=tk.W)
        #---callback function---#
        def calculate():
            weight=float(weight_var.get())
            height=float(height_var.get())
            bmi=round(weight/(height**2),2)
            bmi_label=tk.Label(root,text="Your BMI is {}".format(bmi),fg='black')
            bmi_label.grid(row=3,column=1,sticky=tk.W,padx=25)
            height_entry.delete(0,tk.END)
            weight_entry.delete(0,tk.END)
        #---button----#
        calculate_button=ttk.Button(root,text="Calculate BMI",command=calculate)
        calculate_button.grid(row=2,column=1,sticky=tk.W,padx=25,pady=10)
        root.mainloop()

#------------------------#
if __name__=="__main__":
    bmi=Calculator()
