import pyperclip
import time
import pyautogui
import pygetwindow as gw
import sys
import tkinter as tk
from tkinter import messagebox
def on_closing():
    sys.exit()
def disable_button():
    start_button.config(state=tk.DISABLED)
def enable_button():
    start_button.config(state=tk.NORMAL)
def show_whatsapp_not_open():
    root = tk.Tk()
    root.withdraw()
    root.attributes("-topmost", True)
    messagebox.showerror("WOMI-NUKER", "WhatsApp or Messenger isn't opened. Please open app, and try again.")
def show_whatsapp_not_open1():
    root = tk.Tk()
    root.withdraw()
    root.attributes("-topmost", True)
    messagebox.showerror("WOMI-NUKER", "WhatsApp or Messenger has been closed. Please open app, and try again")
def program_exit_msg():
    root = tk.Tk()
    root.withdraw()
    root.attributes("-topmost", True)
    messagebox.showinfo("WOMI-NUKER", "App finished work.")
    root.destroy()
    sys.exit()
def start_sending():
    try:
        message = message_entry.get("1.0", "end-1c")
        count = count_entry.get().strip()
        if not message:
            raise ValueError("Fill field with text!")
        if not count:
            raise ValueError("Field cannot be empty.")
        count = int(count_entry.get())
        if count <= 0:
            raise ValueError("Number must be higher.")
    except ValueError as e:
        messagebox.showerror("WOMI-NUKER", f"{e}")
        return
    def send_messages():
        pyperclip.copy(message)
        for _ in range(count):
            pyautogui.hotkey('ctrl', 'v')
            time.sleep(0.01)
            pyautogui.press('enter')
            time.sleep(0.10)
            whatsapp_window = None
            for window in gw.getWindowsWithTitle('WhatsApp' or 'Messenger'):
                if window.isActive:
                    whatsapp_window = window
                    break
            if whatsapp_window is None:
                    show_whatsapp_not_open1()
                    enable_button()
                    return start_sending
    def show_messages_sent():
        root = tk.Tk()
        root.withdraw()
        root.attributes("-topmost", True)
        messagebox.showinfo("WOMI-NUKER", "Sending finished.")
        root.destroy()
    disable_button()
    time.sleep(5)
    whatsapp_window = None
    for window in gw.getWindowsWithTitle('WhatsApp' or 'Messenger'):
        if window.isActive:
            whatsapp_window = window
            break
    if whatsapp_window is None:
        show_whatsapp_not_open()
        enable_button()
        return start_sending
    if check_var.get():
        pyperclip.copy("""
        ```+-+-+-+-+-+-+-+-+-+-+
|W|O|M|I|-|N|U|K|E|R|
+-+-+-+-+-+-+-+-+-+-+```
        """)
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.press('enter')
        time.sleep(1)
    send_messages()
    show_messages_sent()
    enable_button()
root = tk.Tk()
root.attributes("-topmost", True)
root.title("WOMI-NUKER")
root.iconbitmap('favicon.ico')
root.protocol("WM_DELETE_WINDOW", on_closing)
window_width = 550
window_height = 290
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
position_top = int(screen_height / 2 - window_height / 2)
position_right = int(screen_width / 2 - window_width / 2)
root.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")
root.resizable(False, False)
tk.Label(root, text="Text:").pack(anchor="w", padx=10, pady=5)
message_entry = tk.Text(root, height=5, width=60)
message_entry.pack(padx=10, pady=5)
frame = tk.Frame(root)
frame.pack(anchor="w", padx=10, pady=5, fill="x")
tk.Label(frame, text="Count:").pack(side="left", padx=10, pady=5)
count_entry = tk.Entry(frame, width=20)
count_entry.pack(side="left", fill="x", expand=True, padx=10, pady=5)
check_var = tk.BooleanVar(value=True)
checkbox = tk.Checkbutton(root, text="Logo on start", variable=check_var)
checkbox.pack(side="left", padx=30)
start_button = tk.Button(root, text="Start", command=start_sending, 
                         bg="#4CAF50",
                         fg="white",
                         font=("Arial", 12, "bold"),
                         padx=20, pady=10,
                         relief="raised",
                         bd=3,
                         cursor="hand2")
start_button.pack(anchor="se", padx=20, pady=20)
root.mainloop()
sys.exit()