import tkinter as tk
import pygame
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
from pyzbar.pyzbar import decode

class QRReader:
    def __init__(self, root):
        self.root = root
        self.root.title("QR Reader")
        self.root.geometry("400x450+100+200")
        self.root.resizable(False, False)
        
        self.icon_path = "./qr/0608.png"
        self.icon_image = tk.PhotoImage(file=self.icon_path)
        self.root.iconphoto(False,self.icon_image)
        
        self.init = pygame.mixer
        self.load = self.init.music
        self.play = self.load 
        self.init.init()
        self.load.load("./qr/0613.mp3")
        self.play.play(-1)
        self.image_label = tk.Label(self.root)
        self.image_label.pack(expand=True, fill='both')
        
        self.button_frame = tk.Frame(self.root)
        self.button_frame.pack(pady=20)
        
        self.open_button = tk.Button(self.button_frame, text="Open QR Image", command=self.open_qr_image)
        self.open_button.pack(side='left', padx=10)
        
        self.read_button = tk.Button(self.button_frame, text="Read QR Image", command=self.read_qr_image)
        self.read_button.pack(side='left', padx=10)
        self.read_button.config(state=tk.DISABLED)  # يتم تعطيل الزر حتى يتم فتح الصورة الأولى
        
        self.clear_button = tk.Button(self.button_frame, text="Clear Image", command=self.clear_image)
        self.clear_button.pack(side='left', padx=10)
        self.clear_button.config(state=tk.DISABLED)  # يتم تعطيل الزر حتى يتم فتح الصورة الأولى
        
        self.current_image = None
    
    def open_qr_image(self):
        self.init.init()
        self.load.load("./qr/0610.mp3")
        self.play.play()
        file_path = filedialog.askopenfilename(
            title="Open QR Image",
            filetypes=(("Image Files", "*.png;*.jpg;*.jpeg;*.bmp"), ("All files", "*.*"))
        )
        if file_path:
            try:
                img = Image.open(file_path)
                img.thumbnail((250, 250))  # Resize image to fit in the window
                self.current_image = img
                img = ImageTk.PhotoImage(img)
                self.image_label.config(image=img)
                self.image_label.image = img
                self.read_button.config(state=tk.NORMAL)  # تفعيل زر قراءة الصورة
                self.clear_button.config(state=tk.NORMAL)  # تفعيل زر مسح الصورة
            except Exception as e:
                messagebox.showerror("Error", f"Failed to open image: {e}")
    
    def read_qr_image(self):
        if self.current_image:
            data = self.decode_qr(self.current_image)
            if data:
                self.init.init()
                self.load.load("./qr/0611.mp3")
                self.play.play() 
                messagebox.showinfo("QR Data", f"Data: {data}")
            else:
                self.init.init()
                self.load.load("./qr/0612.mp3")
                self.play.play()
                messagebox.showerror("Error", "No QR code found in the image.")
        self.init.init()
        self.load.load("./qr/0613.mp3")
        self.play.play(-1)
    def decode_qr(self, img):
        decoded_objects = decode(img)
        if decoded_objects:
            return decoded_objects[0].data.decode('utf-8')
        return None
    
    def clear_image(self):
        self.image_label.config(image='')
        self.image_label.image = None
        self.current_image = None
        self.read_button.config(state=tk.DISABLED)  # يتم تعطيل الزر بعد مسح الصورة
        self.clear_button.config(state=tk.DISABLED)  # يتم تعطيل الزر بعد مسح الصورة
        self.init.init()
        self.load.load("./qr/0614.mp3")
        self.play.play(3)
        messagebox.showinfo("Clear", "Image and data cleared.")
        self.init.init()
        self.load.load("./qr/0613.mp3")
        self.play.play(-1)
    def run_read():
        if __name__ == "__main__":
            root = tk.Tk()
            QRReader(root)
            root.mainloop()