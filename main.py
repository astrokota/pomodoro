import time
import tkinter as tk
from PIL import Image, ImageTk
from playsound import playsound
from tkinter import messagebox

min = None
sec = None
root = None

def clock(timer):
    minutes, seconds = divmod(timer, 60)
    min.set(f"{minutes:02d}")
    sec.set(f"{seconds:02d}")
    root.update()
    time.sleep(1)

def main():
    global min, sec, root

    root = tk.Tk()
    root.geometry("1280x720")
    root.resizable(False, False)
    root.title("Dakota's Pomodoro")

    root.mainloop()

if __name__ == "__main__":
    main()