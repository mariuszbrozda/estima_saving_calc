
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


#RADIOBUTTONS

def pay_contrib_radio_btn():
    print(radio_state.get())


#Variable to hold on to which radio button value is checked.
radio_state = IntVar()
weekly_rb = Radiobutton(data_input_frame, text="Weekly", value=1,
                                           variable=radio_state, command=pay_contrib_radio_btn,
                                           highlightbackground='white', highlightthickness=1, bg='#f3f4f1')

fortnightly_rb = Radiobutton(data_input_frame, text="Fortnightly", value=2,
                                           variable=radio_state, command=pay_contrib_radio_btn,
                                           highlightbackground='white', highlightthickness=1, bg='#f3f4f1')

monthly_rb = Radiobutton(data_input_frame, text="Monthly", value=3,
                                            variable=radio_state, command=pay_contrib_radio_btn,
                                            highlightbackground='white', highlightthickness=1, bg='#f3f4f1')

weekly_rb.place(x=90, y=110)
fortnightly_rb.place(x=90, y=130)
monthly_rb.place(x=90, y=150)



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



# Add Button and Label
Button(data_input_frame, text="Pick date frame",fg='green',  relief='raised', padx=3, pady=3,
       highlightbackground='white', bg='green', highlightthickness=1, command=calendar).place(x=15, y=200)


window.mainloop()