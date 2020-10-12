from tkinter import Tk
from tkinter.filedialog import askdirectory

Tk().withdraw()
path = askdirectory()

print(path)
