
from calendar import Calendar
from tkinter import *

from PIL import Image,ImageTk

import glob

from tkcalendar import Calendar, DateEntry
try:
    import tkinter as tk
    from tkinter import ttk
except ImportError:
    import Tkinter as tk
    import ttk

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk


# CREATE GUI

window = Tk()
window.title("ESTIMA")
window.minsize(width=600, height=750)
window.config(padx=20, pady=20,  border=2, background='#f3f4f1')
window.geometry("600x600")


data_input_frame = LabelFrame(window, text="Input data", font=('Helvetica', 13, 'bold'), bg='#f3f4f1',
                   padx=5, pady=10,bd=1, width=240, height=280, highlightbackground='black', highlightthickness=1)
data_input_frame.place(x=15, y=15)

vaults_frame = LabelFrame(window, text="Saving vaults", font=('Helvetica', 13, 'bold'), bg='#f3f4f1',
                   padx=5, pady=10,bd=1, width=260, height=280, highlightbackground='black', highlightthickness=1)
vaults_frame.place(x=280, y=15)


separator_1 = ttk.Separator(window, orient='horizontal')
separator_1.pack(fill='x')

separator_2 = ttk.Separator(window, orient='vertical')
separator_2.pack(fill='y', side=TOP)

# LABELS


income_label = Label(data_input_frame, text="Income", font=('Helvetica', 12, ))
income_label.config(padx=2, pady=2, relief='flat', bg='#f3f4f1')
income_label.place(x=25, y=15)

label_2 = Label(data_input_frame, text="Saving goal", font=('Helvetica', 12, ))
label_2.config(padx=2, pady=2, relief='flat', bg='#f3f4f1')
label_2.place(x=25, y=45)

expenses_label = Label(data_input_frame, text="Expenses", font=('Helvetica', 12, ))
expenses_label.config(padx=2, pady=2, relief='flat', bg='#f3f4f1')
expenses_label.place(x=25, y=75)

contribute_label = Label(data_input_frame, text="Contribute", font=('Helvetica', 12, ))
contribute_label.config(padx=2, pady=2, relief='flat', bg='#f3f4f1')
contribute_label.place(x=25, y=110)


# INPUTS
income_input = Entry(data_input_frame, width=10, relief='groove', highlightbackground='white', highlightthickness=1)
income_input.place(x=100, y=15)

input_2 = Entry(data_input_frame, width=10, relief='groove', highlightbackground='white', highlightthickness=1)
input_2.place(x=100, y=45)

expenses_input = Entry(data_input_frame, width=10, relief='groove', highlightbackground='white', highlightthickness=1)
expenses_input.place(x=100, y=75)

input_4 = Entry(data_input_frame, width=10, relief='groove', )
# input_4.place(x=100, y=105)


# BUTTONS:

# Vaults frame
forecast_btn = Button(vaults_frame, text='Forecast', fg='black', relief='raised', padx=3, pady=3)
print_btn = Button(vaults_frame, text='Print',  fg='black', relief='raised', padx=3, pady=3)
# settings_btn = Button(vaults_frame, text='Settings', command=show_settings_frame,  fg='black', relief='raised', padx=3, pady=3)
create_vault = Button(vaults_frame, command='create_vault', text='Create vault',  fg='black', relief='raised', padx=3, pady=3)

# Input data frame
calculate_btn = Button(data_input_frame, text='Calculate',  fg='black', relief='raised', padx=3, pady=3)

forecast_btn.place(x=5, y=0)
# settings_btn.place(x=140, y=0)
create_vault.place(x=100, y=0)
print_btn.place(x=290, y=0)
calculate_btn.place(x=140, y=200)







window.mainloop()