
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

from main import vaults_frame


class VaultObject:
    def __init__(self, vault_name, contribiution_amount):
        self.vault_name = vault_name
        self.contribiution_amount = contribiution_amount







