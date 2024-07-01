from make import QRMaker
import tkinter as tk
def run_make():
    root = tk.Tk()
    QRMaker(root)
    root.mainloop()
run_make()