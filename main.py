
from calendar import Calendar
from tkinter import *
import pandas


from tkcalendar import Calendar, DateEntry
try:
    import tkinter as tk
    from tkinter import ttk
except ImportError:
    import Tkinter as tk
    import ttk

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from gui import EstimaInterface



# Add Calendar
def calendar():
    calendar_root = Tk()
    calendar_root.title("Calendar")
    calendar_root.minsize(width=400, height=320)
    calendar_root.config(padx=15, pady=15, border=2, background='#f3f4f1')

    def print_sel():
        print(calendar.selection_get())
        calendar.see(datetime.date(year=2022, month=4, day=5))
        # to_date_forecast()

    # top = tk.Toplevel(window)

    import datetime
    today = datetime.date.today()

    mindate = datetime.date(year=2020, month=1, day=1)
    maxdate = datetime.date(year=2040, month=1, day=1)
    print(mindate, maxdate)

    calendar = Calendar(calendar_root,  font=("Arial",17, 'bold'),  selectmode='day', locale='en_US',
                   mindate=mindate, maxdate=maxdate, disabledforeground='red',
                   cursor="", year=2022, month=4, day=2)

    calendar.place(x=0, y=10)
    Button(calendar_root, text="OK",fg='green', relief='raised', bd=1, command=print_sel).pack(side=BOTTOM)
    # date.config(text=f'Today date is:{calendar.get_date()}')


estima_gui = EstimaInterface()

# CREATING VAULTS



def create_vault_form():
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

    def add_vault(self):
        new_vault = VaultObject('EDUCATION','weekly')
        new_vault_frame = LabelFrame(estima_gui.vaults_frame, text=new_vault.vault_name, fg='black', relief='raised', padx=3, pady=3)
        new_vault_frame.pack()

    create_vault_btn = Button(vault_data_input_frame, command=add_vault, text='Create', fg='black', relief='raised', padx=3, pady=3)
    create_vault_btn.place(x=140, y=200)

