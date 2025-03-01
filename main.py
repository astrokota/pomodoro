import tkinter as tk
from PIL import Image, ImageTk
from playsound import playsound
from tkinter import messagebox

#initialize global variables for minutes, seconds, root, timer flag to check if timer is active, current timer will be countdown values as time ticks down.
min_var = None
sec_var = None
root = None
timer_running = False 
current_timer = 0  

def update_clock():

    #timer display update sequence and checks the running timer by using quotient and remainder of minutes/seconds (divmod) and stops timer once current timer is 0.
    global current_timer, timer_running

    if current_timer >= 0 and timer_running:
        minutes, seconds = divmod(current_timer, 60)
        min_var.set(f"{minutes:02d}")
        sec_var.set(f"{seconds:02d}")
        
        if current_timer == 0:
            playsound("alarm.wav")
            messagebox.showinfo("Session is over.")
            timer_running = False  

        else:
            current_timer -= 1
            root.after(1000, update_clock)

def start_timer(seconds):

    #starts countdown for given time and preventings instances of multiple timers, then starts the clock again at the end
    global current_timer, timer_running

    if not timer_running:  
        current_timer = seconds
        timer_running = True
        update_clock()  

def stop_timer():

    #stops timer and makes sure clock doesn't start again.
    global timer_running
    timer_running = False  

def main():
    #initilize and create GUI window
    global min_var, sec_var, root

    root = tk.Tk()
    root.geometry("1280x720")
    root.resizable(False, False)
    root.title("Dakota's Pomodoro")

    min_var = tk.StringVar(root, value="25")
    sec_var = tk.StringVar(root, value="00")

    #labels for the timers
    min_label = tk.Label(root, textvariable = min_var, font = ("roboto", 25, "bold"), bg = "red", fg = "black")
    min_label.pack()

    sec_label = tk.Label(root, textvariable = sec_var, font = ("roboto", 25, "bold"), bg = "black", fg = "white")
    sec_label.pack()

    #application background image
    canvas = tk.Canvas(root, width = 1280, height = 720)
    canvas.pack(expand = True, fill = "both")
    img = Image.open("pomodoro (1).png")
    bg = ImageTk.PhotoImage(img)
    canvas.create_image(640, 260, image = bg, anchor = "center")

    #various buttons for different times, pause, and stop.
    btn_clock_A = tk.Button(root, text = "25min Session", bd = 5, command = lambda: start_timer(25*60), bg = "red", font = ("roboto", 20, "bold"))
    btn_clock_A.place(x = 480, y = 580)

    btn_pause = tk.Button(root, text = "Pause", bd=5, command = lambda: start_timer(5*60), bg = "red", font = ("roboto", 20, "bold"))
    btn_pause.place(x = 580, y = 580)

    btn_stop = tk.Button(root, text = "Stop", bd = 5, command = stop_timer, bg = "red", font = ("roboto", 20, "bold"))
    btn_stop.place(x = 680, y = 580)

    root.mainloop()

if __name__ == "__main__":
    main()
