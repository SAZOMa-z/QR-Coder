import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog, colorchooser
from PIL import Image, ImageTk, ImageDraw
import qrcode
import os
import pygame
class QRMaker:
    def __init__(self, root):
        self.root = root
        self.root.title("QR Maker")
        self.root.geometry("400x500+100+100")
        self.root.resizable(False, False)
        
        self.icon_path = "./qr/files/0608.png"
        self.icon_image = tk.PhotoImage(file=self.icon_path)
        self.root.iconphoto(False,self.icon_image)
        
        self.init = pygame.mixer
        self.load = self.init.music
        self.play = self.load
        self.init.init()
        self.load.load("./qr/files/0613.mp3")
        self.play.play(-1)
        self.qr_type_var = tk.StringVar()
        self.qr_type_var.set("WiFi")
        
        self.qr_types = [
            "WiFi", "URL", "Text", "Email", "Phone", "SMS", "Geo", "Event",
            "Contact", "YouTube", "Instagram", "Twitter", "LinkedIn", "Bitcoin",
            "PayPal", "Skype", "WhatsApp", "Telegram", "Spotify", "Snapchat",
            "Pinterest", "Tumblr", "Twitch", "GitHub", "Reddit", "Vimeo", "Website", "Custom"
        ]
        
        self.qr_type_menu = tk.OptionMenu(self.root, self.qr_type_var, *self.qr_types)
        self.qr_type_menu.pack(pady=20)
        
        self.create_qr_button = tk.Button(self.root, text="Create QR", command=self.create_qr)
        self.create_qr_button.pack(pady=20)
        
        self.qr_image_label = tk.Label(self.root)
        self.qr_image_label.pack(pady=20)
    def create_qr(self):
        self.init.init()
        self.load.load("./qr/files/0610.mp3")
        self.play.play()
        qr_type = self.qr_type_var.get()
        try:
            if qr_type == "WiFi":
                ssid = simpledialog.askstring("Input", "Enter SSID:")
                password = simpledialog.askstring("Input", "Enter Password:")
                security = simpledialog.askstring("Input", "Enter Security (WPA/WEP):")
                if not ssid or not password or not security:
                    messagebox.showerror("Error", "Please enter all WiFi details.")
                    return
                img = qrcode.make(f"WIFI:S:{ssid};T:{security};P:{password};;")
            elif qr_type == "URL":
                url = simpledialog.askstring("Input", "Enter URL:")
                if not url:
                    messagebox.showerror("Error", "Please enter a URL.")
                    return
                img = qrcode.make(url)
            elif qr_type == "Text":
                text = simpledialog.askstring("Input", "Enter Text:")
                if not text:
                    messagebox.showerror("Error", "Please enter text.")
                    return
                img = qrcode.make(text)
            elif qr_type == "Email":
                email = simpledialog.askstring("Input", "Enter Email:")
                if not email:
                    messagebox.showerror("Error", "Please enter an email.")
                    return
                img = qrcode.make(f"mailto:{email}")
            elif qr_type == "Phone":
                phone = simpledialog.askstring("Input", "Enter Phone Number:")
                if not phone:
                    messagebox.showerror("Error", "Please enter a phone number.")
                    return
                img = qrcode.make(f"tel:{phone}")
            elif qr_type == "SMS":
                phone = simpledialog.askstring("Input", "Enter Phone Number:")
                message = simpledialog.askstring("Input", "Enter Message:")
                if not phone or not message:
                    messagebox.showerror("Error", "Please enter phone number and message.")
                    return
                img = qrcode.make(f"smsto:{phone}:{message}")
            elif qr_type == "Geo":
                latitude = simpledialog.askstring("Input", "Enter Latitude:")
                longitude = simpledialog.askstring("Input", "Enter Longitude:")
                if not latitude or not longitude:
                    messagebox.showerror("Error", "Please enter both latitude and longitude.")
                    return
                img = qrcode.make(f"geo:{latitude},{longitude}")
            elif qr_type == "Event":
                event = simpledialog.askstring("Input", "Enter Event details (Format: SUMMARY;LOCATION;DESCRIPTION;START;END):")
                if not event:
                    messagebox.showerror("Error", "Please enter event details.")
                    return
                img = qrcode.make(f"BEGIN:VEVENT\n{event}\nEND:VEVENT")
            elif qr_type == "Contact":
                contact = simpledialog.askstring("Input", "Enter Contact details (Format: N;ORG;TEL;EMAIL):")
                if not contact:
                    messagebox.showerror("Error", "Please enter contact details.")
                    return
                img = qrcode.make(f"BEGIN:VCARD\n{contact}\nEND:VCARD")
            elif qr_type == "YouTube":
                youtube_url = simpledialog.askstring("Input", "Enter YouTube URL:")
                if not youtube_url:
                    messagebox.showerror("Error", "Please enter YouTube URL.")
                    return
                img = qrcode.make(youtube_url)
            elif qr_type == "Instagram":
                instagram_username = simpledialog.askstring("Input", "Enter Instagram Username:")
                if not instagram_username:
                    messagebox.showerror("Error", "Please enter Instagram Username.")
                    return
                img = qrcode.make(f"https://www.instagram.com/{instagram_username}")
            elif qr_type == "Twitter":
                twitter_username = simpledialog.askstring("Input", "Enter Twitter Username:")
                if not twitter_username:
                    messagebox.showerror("Error", "Please enter Twitter Username.")
                    return
                img = qrcode.make(f"https://www.twitter.com/{twitter_username}")
            elif qr_type == "LinkedIn":
                linkedin_profile = simpledialog.askstring("Input", "Enter LinkedIn Profile URL:")
                if not linkedin_profile:
                    messagebox.showerror("Error", "Please enter LinkedIn Profile URL.")
                    return
                img = qrcode.make(linkedin_profile)
            elif qr_type == "Bitcoin":
                bitcoin_address = simpledialog.askstring("Input", "Enter Bitcoin Address:")
                if not bitcoin_address:
                    messagebox.showerror("Error", "Please enter Bitcoin Address.")
                    return
                img = qrcode.make(f"bitcoin:{bitcoin_address}")
            elif qr_type == "PayPal":
                paypal_me = simpledialog.askstring("Input", "Enter PayPal.me URL:")
                if not paypal_me:
                    messagebox.showerror("Error", "Please enter PayPal.me URL.")
                    return
                img = qrcode.make(paypal_me)
            elif qr_type == "Skype":
                skype_username = simpledialog.askstring("Input", "Enter Skype Username:")
                if not skype_username:
                    messagebox.showerror("Error", "Please enter Skype Username.")
                    return
                img = qrcode.make(f"skype:{skype_username}?call")
            elif qr_type == "WhatsApp":
                whatsapp_number = simpledialog.askstring("Input", "Enter WhatsApp Number:")
                if not whatsapp_number:
                    messagebox.showerror("Error", "Please enter WhatsApp Number.")
                    return
                img = qrcode.make(f"https://wa.me/{whatsapp_number}")
            elif qr_type == "Telegram":
                telegram_username = simpledialog.askstring("Input", "Enter Telegram Username:")
                if not telegram_username:
                    messagebox.showerror("Error", "Please enter Telegram Username.")
                    return
                img = qrcode.make(f"https://t.me/{telegram_username}")
            elif qr_type == "Spotify":
                spotify_uri = simpledialog.askstring("Input", "Enter Spotify URI:")
                if not spotify_uri:
                    messagebox.showerror("Error", "Please enter Spotify URI.")
                    return
                img = qrcode.make(spotify_uri)
            elif qr_type == "Snapchat":
                snapchat_username = simpledialog.askstring("Input", "Enter Snapchat Username:")
                if not snapchat_username:
                    messagebox.showerror("Error", "Please enter Snapchat Username.")
                    return
                img = qrcode.make(f"https://www.snapchat.com/add/{snapchat_username}")
            elif qr_type == "Pinterest":
                pinterest_profile = simpledialog.askstring("Input", "Enter Pinterest Profile URL:")
                if not pinterest_profile:
                    messagebox.showerror("Error", "Please enter Pinterest Profile URL.")
                    return
                img = qrcode.make(pinterest_profile)
            elif qr_type == "Tumblr":
                tumblr_blog = simpledialog.askstring("Input", "Enter Tumblr Blog URL:")
                if not tumblr_blog:
                    messagebox.showerror("Error", "Please enter Tumblr Blog URL.")
                    return
                img = qrcode.make(tumblr_blog)
            elif qr_type == "Twitch":
                twitch_username = simpledialog.askstring("Input", "Enter Twitch Username:")
                if not twitch_username:
                    messagebox.showerror("Error", "Please enter Twitch Username.")
                    return
                img = qrcode.make(f"https://www.twitch.tv/{twitch_username}")
            elif qr_type == "GitHub":
                github_profile = simpledialog.askstring("Input", "Enter GitHub Profile URL:")
                if not github_profile:
                    messagebox.showerror("Error", "Please enter GitHub Profile URL.")
                    return
                img = qrcode.make(github_profile)
            elif qr_type == "Reddit":
                reddit_profile = simpledialog.askstring("Input", "Enter Reddit Profile URL:")
                if not reddit_profile:
                    messagebox.showerror("Error", "Please enter Reddit Profile URL.")
                    return
                img = qrcode.make(reddit_profile)
            elif qr_type == "Vimeo":
                vimeo_url = simpledialog.askstring("Input", "Enter Vimeo URL:")
                if not vimeo_url:
                    messagebox.showerror("Error", "Please enter Vimeo URL.")
                    return
                img = qrcode.make(vimeo_url)
            elif qr_type == "Website":
                website_url = simpledialog.askstring("Input", "Enter Website URL:")
                if not website_url:
                    messagebox.showerror("Error", "Please enter Website URL.")
                    return
                img = qrcode.make(website_url)
            elif qr_type == "Custom":
                custom_data = simpledialog.askstring("Input", "Enter Custom Data:")
                if not custom_data:
                    messagebox.showerror("Error", "Please enter custom data.")
                    return
                img = qrcode.make(custom_data)
            else:
                messagebox.showerror("Error", "Unsupported QR type.")
                return

            # تحديد لون الخلفية ولون رمز QR
            background_color = colorchooser.askcolor(title="Choose Background Color")[1]
            qr_color = colorchooser.askcolor(title="Choose QR Color")[1]
            
            if not background_color or not qr_color:
                messagebox.showerror("Error", "Please select both background and QR colors.")
                return
            
            # تغيير الألوان
            img = img.convert("RGB")
            qr_pixels = img.load()
            for y in range(img.size[1]):
                for x in range(img.size[0]):
                    if qr_pixels[x, y] == (0, 0, 0):
                        qr_pixels[x, y] = tuple(int(qr_color.lstrip('#')[i:i+2], 16) for i in (0, 2, 4))
                    else:
                        qr_pixels[x, y] = tuple(int(background_color.lstrip('#')[i:i+2], 16) for i in (0, 2, 4))

            # إضافة شعار إذا كان النوع يدعم ذلك
            if qr_type in ["WiFi", "YouTube", "Instagram", "Twitter", "LinkedIn", "Bitcoin",
                           "PayPal", "Skype", "WhatsApp", "Telegram", "Spotify", "Snapchat",
                           "Pinterest", "Tumblr", "Twitch", "GitHub", "Reddit", "Vimeo", "Website"]:
                logo_filename = f"{qr_type.lower()}_logo.png"  # اسم الملف الموجود في المجلد logo
                logo_path = os.path.join("logo", logo_filename)  # مسار الملف المطلق
                if os.path.exists(logo_path):
                    logo = Image.open(logo_path)
                    logo.thumbnail((30, 30))
                    img.paste(logo, (img.size[0] // 2 - 15, img.size[1] // 2 - 15))
                else:
                    messagebox.showwarning("WARNING", f"Logo file {logo_filename} not found in 'logo' folder!")
            else:
                messagebox.showwarning("WARNING", "The QR code has been successfully made but without logo!!!")
            
            save_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
            if save_path:
                img.save(save_path)
                self.init.init()
                self.load.load("./qr/files/0611.mp3")
                self.play.play()
                messagebox.showinfo("Success", f"QR code saved at {save_path}")
                
                # عرض الصورة المحفوظة في النافذة
                saved_image = Image.open(save_path)
                self.init.init()
                self.load.load("./qr/files/0609.mp3")
                self.play.play()
                qr_image = ImageTk.PhotoImage(saved_image)
                self.qr_image_label.config(image=qr_image)
                self.qr_image_label.image = qr_image
        except Exception as e:
            messagebox.showerror("Error", str(e))

if __name__ == "__main__":
    root = tk.Tk()
    QRMaker(root)
