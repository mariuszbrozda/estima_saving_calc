
from tkinter import *

from PIL import Image,ImageTk
from pandas import *
import glob

from tkcalendar import Calendar, DateEntry
try:
    import tkinter as tk
    from tkinter import ttk
except ImportError:
    import Tkinter as tk
    import ttk




class vault_object():
    def __init__(self, vault_name, contribiution_amount, ):
        self.vault_name = vault_name
        self.contribiution_amount = contribiution_amount
        # self.chart_data_connection




def create_vault():
    vault_window = Tk()
    vault_window.title("Create vault")
    vault_window.minsize(width=240, height=280)
    vault_window.config(padx=0, pady=0, border=2, background='#f3f4f1')

    vault_data_input_frame = LabelFrame(vault_window, text="Add vault", font=('Helvetica', 13, 'bold'), bg='#f3f4f1',
                                  padx=5, pady=10, bd=1, width=240, height=280, highlightbackground='black',
                                  highlightthickness=1)

    vault_data_input_frame.pack(side=BOTTOM)

    income_label = Label(vault_data_input_frame, text="Vault name", font=('Helvetica', 12,))
    income_label.config(padx=2, pady=2, relief='flat', bg='#f3f4f1')
    income_label.place(x=25, y=15)

    label_2 = Label(vault_data_input_frame, text="Contribiution amount", font=('Helvetica', 12,))
    label_2.config(padx=2, pady=2, relief='flat', bg='#f3f4f1')
    label_2.place(x=25, y=45)


    contribute_label = Label(vault_data_input_frame, text="Contribute", font=('Helvetica', 12,))
    contribute_label.config(padx=2, pady=2, relief='flat', bg='#f3f4f1')
    contribute_label.place(x=25, y=110)

    # INPUTS
    income_input = Entry(vault_data_input_frame, width=10, relief='groove', highlightbackground='white', highlightthickness=1)
    income_input.place(x=100, y=15)

    input_2 = Entry(vault_data_input_frame, width=10, relief='groove', highlightbackground='white', highlightthickness=1)
    input_2.place(x=100, y=45)

    expenses_input = Entry(vault_data_input_frame, width=10, relief='groove', highlightbackground='white',
                           highlightthickness=1)
    expenses_input.place(x=100, y=75)

    calculate_btn = Button(vault_data_input_frame, text='Create', fg='black', relief='raised', padx=3, pady=3)
    calculate_btn.place(x=140, y=200)