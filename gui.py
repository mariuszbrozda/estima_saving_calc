
from calendar import Calendar
from tkinter import *
import pandas
from vaults import VaultObject

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



class EstimaInterface:
    def __init__(self):
        self.window = Tk()
        self.window.title("ESTIMA")
        self.window.minsize(width=600, height=750)
        self.window.config(padx=20, pady=20, border=2, background='#f3f4f1')
        self.window.geometry("600x600")

        self.data_input_frame = LabelFrame(self.window, text="Input data", font=('Helvetica', 13, 'bold'), bg='#f3f4f1',
                                      padx=5, pady=10, bd=1, width=240, height=280, highlightbackground='black',
                                      highlightthickness=1)
        self.data_input_frame.place(x=15, y=15)

        self.vaults_frame = LabelFrame(self.window, text="Saving vaults", font=('Helvetica', 13, 'bold'), bg='#f3f4f1',
                                  padx=5, pady=10, bd=1, width=260, height=280, highlightbackground='black',
                                  highlightthickness=1)
        self.vaults_frame.place(x=280, y=15)

        self.separator_1 = ttk.Separator(self.window, orient='horizontal')
        self.separator_1.pack(fill='x')

        # LABELS
        self.income_label = Label(self.data_input_frame, text="Income", font=('Helvetica', 12,))
        self.income_label.config(padx=2, pady=2, relief='flat', bg='#f3f4f1')
        self.income_label.place(x=25, y=15)

        self.label_2 = Label(self.data_input_frame, text="Saving goal", font=('Helvetica', 12,))
        self.label_2.config(padx=2, pady=2, relief='flat', bg='#f3f4f1')
        self.label_2.place(x=25, y=45)

        self.expenses_label = Label(self.data_input_frame, text="Expenses", font=('Helvetica', 12,))
        self.expenses_label.config(padx=2, pady=2, relief='flat', bg='#f3f4f1')
        self.expenses_label.place(x=25, y=75)

        self.contribute_label = Label(self.data_input_frame, text="Contribute", font=('Helvetica', 12,))
        self.contribute_label.config(padx=2, pady=2, relief='flat', bg='#f3f4f1')
        self.contribute_label.place(x=25, y=110)

        # INPUTS
        self.income_input = Entry(self.data_input_frame, width=10, relief='groove', highlightbackground='white',
                             highlightthickness=1)
        self.income_input.place(x=100, y=15)

        self.input_2 = Entry(self.data_input_frame, width=10, relief='groove', highlightbackground='white', highlightthickness=1)
        self.input_2.place(x=100, y=45)

        self.expenses_input = Entry(self.data_input_frame, width=10, relief='groove', highlightbackground='white',
                               highlightthickness=1)
        self.expenses_input.place(x=100, y=75)

        self.input_4 = Entry(self.data_input_frame, width=10, relief='groove', )
        # input_4.place(x=100, y=105)

        # BUTTONS:

        # Vaults frame
        self.forecast_btn = Button(self.vaults_frame, text='Forecast', fg='black', relief='raised', padx=3, pady=3)
        self.print_btn = Button(self.vaults_frame, text='Print', fg='black', relief='raised', padx=3, pady=3)
        # settings_btn = Button(vaults_frame, text='Settings', command=show_settings_frame,  fg='black', relief='raised', padx=3, pady=3)
        self.form_create_vault = Button(self.vaults_frame, command='create_vault_form', text='Create vault', fg='black',
                                   relief='raised', padx=3, pady=3)

        # Input data frame
        self.calculate_btn = Button(self.data_input_frame, text='Calculate', fg='black', relief='raised', padx=3, pady=3)

        self.forecast_btn.place(x=5, y=0)
        # settings_btn.place(x=140, y=0)
        self.form_create_vault.place(x=100, y=0)
        self.print_btn.place(x=290, y=0)
        self.calculate_btn.place(x=140, y=200)

        # RADIOBUTTONS

        # Variable to hold on to which radio button value is checked.
        self.radio_state = IntVar()
        self.weekly_rb = Radiobutton(self.data_input_frame, text="Weekly", value=1,
                                variable=self.radio_state, command=self.pay_contrib_radio_btn,
                                highlightbackground='white', highlightthickness=1, bg='#f3f4f1')

        self.fortnightly_rb = Radiobutton(self.data_input_frame, text="Fortnightly", value=2,
                                     variable=self.radio_state, command=self.pay_contrib_radio_btn,
                                     highlightbackground='white', highlightthickness=1, bg='#f3f4f1')

        self.monthly_rb = Radiobutton(self.data_input_frame, text="Monthly", value=3,
                                 variable=self.radio_state, command=self.pay_contrib_radio_btn,
                                 highlightbackground='white', highlightthickness=1, bg='#f3f4f1')

        self.weekly_rb.place(x=90, y=110)
        self.fortnightly_rb.place(x=90, y=130)
        self.monthly_rb.place(x=90, y=150)

        # Add Button and Label
        Button(self.data_input_frame, text="Pick date frame", fg='green', relief='raised', padx=3, pady=3,
               highlightbackground='white', bg='green', highlightthickness=1, command='calendar').place(x=15, y=200)

        # CHARTS

        data1 = pandas.read_csv('data.csv')
        data1 = {
            'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
            'Saving': [250, 14, 8, 9, 15, 20, 22, 23, 30, 28, 29, 33]
        }

        data = {
            'Month': {
                'Jan': 1,
                'Feb': 2,
                'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6, 'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12},

        }

        df1 = pandas.DataFrame(data1, columns=['Month', 'Saving'])
        df2 = pandas.DataFrame(data, columns=['Month', 'Saving'])

        chart = plt.Figure(figsize=(6, 4), dpi=100)
        ax1 = chart.add_subplot(111)
        # ax2 = figure1.add_subplot(111)
        bar1 = FigureCanvasTkAgg(chart, self.window)
        bar1.get_tk_widget().place(x=15, y=325)
        df1 = df1[['Month', 'Saving']].groupby('Month').sum()
        df2 = df2[['Month', 'Saving']].groupby('Month').sum()

        df1.plot(kind='bar', legend=True, color='r', ax=ax1)
        df2.plot(kind='bar', legend=True, color='g', ax=ax1)
        # df1.plot(kind='line', legend=True, ax=ax1, color='r', marker='o', fontsize=12)
        # df2.plot(kind='line', legend=True, ax=ax1, color='b', marker='o', fontsize=12)
        ax1.set_title('Savings up to date')
        ax1.set_ylabel('')

        self.window.mainloop()

        def pay_contrib_radio_btn():
            print(self.radio_state.get())