from read import QRReader
import tkinter as tk
def run_read():
    root = tk.Tk()
    QRReader(root)
    root.mainloop()
run_read()