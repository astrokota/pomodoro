import tkinter as tk
from PIL import Image, ImageTk
from playsound import playsound
from tkinter import messagebox

# ==========================
# GLOBAL VARIABLES
# ==========================

#Variables for timer logic and GUI elements
min_var = None #Minutes display variable
sec_var = None #Seconds display variable
root = None #Main application window
timer_running = False #Flag to track if timer is running
current_timer = 0 #Current countdown value
paused_timer = 0 #Stores paused time

# ==========================
# TIMER FUNCTIONS
# ==========================

def update_clock():

    """Updates the timer display every second and stops when zero is reached."""
    global current_timer, timer_running

    if current_timer >= 0 and timer_running:
        minutes, seconds = divmod(current_timer, 60) #Gets minutes and seconds
        min_var.set(f"{minutes:02d}")
        sec_var.set(f"{seconds:02d}")
        
        if current_timer == 0:
            playsound("alarm.wav")
            messagebox.showinfo("Session is over.")
            timer_running = False #Stops the timer

        else:
            current_timer -= 1
            root.after(1000, update_clock) #Call again after 1 second

def start_timer(seconds):

    """Starts the countdown timer for a given number of seconds."""
    global current_timer, timer_running

    if not timer_running:  
        current_timer = seconds
        timer_running = True
        update_clock()  

def pause_timer():

    """Pauses the timer and stores the remaining time."""
    global timer_running, paused_timer

    if timer_running:
        timer_running = False
        paused_timer = current_timer #Store remaining time

def resume_timer():

    """Resumes the timer from the paused time."""
    global timer_running, paused_timer

    if not timer_running and paused_timer > 0:
        start_timer(paused_timer)

def stop_timer():

    """Stops the timer and resets the display to 00:00."""
    global timer_running, current_timer, paused_timer
    timer_running = False
    current_timer = 0
    paused_timer = 0
    min_var.set("00")
    sec_var.set("00")

# ==========================
# 10-MINUTE SESSION WINDOW
# ==========================

def window_10min():

    """Creates a new window (720x480) for a 10-minute timer session."""
    new_window = tk.Toplevel(root)
    new_window.geometry("720x480")
    new_window.title("10min Timer")

    #Creates canvas with background image
    canvas_10 = tk.Canvas(new_window, width = 720, height = 480)
    canvas_10.pack(expand = True, fill = "both")
    img_10 = Image.open("10min_pomodoro_background.png") #Alt text provided
    bg_10 = ImageTk.PhotoImage(img_10)
    canvas_10.create_image(0, 0, image = bg_10, anchor = "nw")

    new_window.bg_image = bg_10 #Prevents garbage collection from removing image

    #Timer variables for 10-minute window.
    min_var_10 = tk.StringVar(new_window, value = "10")
    sec_var_10 = tk.StringVar(new_window, value = "00")
    timer_running_10 = [False] #Lists used to store mutable values to modify local variables within nested functions
    current_timer_10 = [0]
    paused_timer_10 = [0]

    # ==========================
    # 10-MINUTE TIMER FUNCTIONS
    # ==========================

    def update_clock_10():
        
        """Updates the 10-minute timer display."""
        if current_timer_10[0] >= 0 and timer_running_10[0]:
            minutes, seconds = divmod(current_timer_10[0], 60)
            min_var_10.set(f"{minutes:02d}")
            sec_var_10.set(f"{seconds:02d}")

            #If timer is 0, sound plays and text displays. If not, timer updates until reaching 0.
            if current_timer_10[0] == 0:
                playsound("alarm.wav")
                messagebox.showinfo("Session is over.")
                timer_running_10[0] = False
            else:
                current_timer_10[0] -= 1
                new_window.after(1000, update_clock_10)

    def start_timer_10(seconds):

        """Starts the 10-minute timer."""
        if not timer_running_10[0]:
            current_timer_10[0] = seconds
            timer_running_10[0] = True
            update_clock_10()

    def pause_timer_10():

        """Pauses the 10-minute timer."""
        if timer_running_10[0]:
            timer_running_10[0] = False
            paused_timer_10[0] = current_timer_10[0]

    def resume_timer_10():

        """Resumes the 10-minute timer."""
        if not timer_running_10[0] and paused_timer_10[0] > 0:
            start_timer_10(paused_timer_10[0])

    def stop_timer_10():

        """Stops the 10-minute timer and resets it to 00:00."""
        timer_running_10[0] = False
        current_timer_10[0] = 0
        paused_timer_10[0] = 0
        min_var_10.set("00")
        sec_var_10.set("00")

    # ==========================
    # 10-MINUTE TIMER UI ELEMENTS
    # ==========================

    #Timer display labels during 10-minute session
    min_label_10 = tk.Label(new_window, textvariable=min_var_10, font=("roboto", 25, "bold"), bg="red", fg="black")
    sec_label_10 = tk.Label(new_window, textvariable=sec_var_10, font=("roboto", 25, "bold"), bg="black", fg="white")

    #Control buttons for timer in 10-minute session
    btn_start_10 = tk.Button(new_window, text="Start 10min", bd=5, command=lambda: start_timer_10(10*60), bg="red", font=("roboto", 20, "bold"))
    btn_pause_10 = tk.Button(new_window, text="Pause", bd=5, command=pause_timer_10, bg="red", font=("roboto", 20, "bold"))
    btn_resume_10 = tk.Button(new_window, text="Resume", bd=5, command=resume_timer_10, bg="red", font=("roboto", 20, "bold"))
    btn_stop_10 = tk.Button(new_window, text="Stop", bd=5, command=stop_timer_10, bg="red", font=("roboto", 20, "bold"))
    btn_exit_10 = tk.Button(new_window, text = "Exit", bd = 5, command = new_window.destroy, bg = "red", font = ("roboto", 20, "bold"))

    #Place elements on canvas so they aren't "behind" the background image
    canvas_10.create_window(360, 150, window = min_label_10)
    canvas_10.create_window(360, 200, window = sec_label_10)
    canvas_10.create_window(600, 60, window = btn_start_10)
    canvas_10.create_window(600, 155, window = btn_pause_10)
    canvas_10.create_window(600, 250, window = btn_resume_10)
    canvas_10.create_window(600, 345, window = btn_stop_10)
    canvas_10.create_window(600, 435, window = btn_exit_10)
    
# ==========================
# MAIN APPLICATION
# ==========================

def main():

    """Initializes and creates the main Pomodoro application and populates initial GUI window"""
    global min_var, sec_var, root

    root = tk.Tk()
    root.geometry("1280x720") #Sets window size to 1280x720
    root.resizable(False, False)
    root.title("Dakota's Pomodoro")

    min_var = tk.StringVar(root, value="25")
    sec_var = tk.StringVar(root, value="00")


    #Application background image
    canvas = tk.Canvas(root, width = 1280, height = 720)
    canvas.pack(expand = True, fill = "both")
    img = Image.open("25min_pomodoro_background.png") #Alt text provided
    bg = ImageTk.PhotoImage(img)
    canvas.create_image(0, 0, image = bg, anchor = "nw")

    #Timer display labels during 25-minute session
    min_label = tk.Label(root, textvariable = min_var, font = ("roboto", 50, "bold"), bg = "red", fg = "black")
    sec_label = tk.Label(root, textvariable = sec_var, font = ("roboto", 50, "bold"), bg = "black", fg = "white")

    canvas.create_window(600, 100, window = min_label)
    canvas.create_window(700, 100, window = sec_label)

    #Various buttons for 25min timer, pause, resume, stop, 10min timer session, and exit.
    btn_clock_25 = tk.Button(root, text="Start 25min", bd=5, command=lambda: start_timer(25*60), bg="red", font=("roboto", 20, "bold"))
    btn_clock_25.place(x=150, y=580)

    btn_pause = tk.Button(root, text="Pause", bd=5, command=pause_timer, bg="red", font=("roboto", 20, "bold"))
    btn_pause.place(x=350, y=580)

    btn_resume = tk.Button(root, text="Resume", bd=5, command=resume_timer, bg="red", font=("roboto", 20, "bold"))
    btn_resume.place(x=475, y=580)

    btn_stop = tk.Button(root, text="Stop", bd=5, command=stop_timer, bg="red", font=("roboto", 20, "bold"))
    btn_stop.place(x=625, y=580)

    btn_10min = tk.Button(root, text="10min Session", bd=5, command=window_10min, bg="red", font=("roboto", 20, "bold"))
    btn_10min.place(x=825, y=580)

    btn_exit = tk.Button(root, text="Exit", bd=5, command=root.destroy, bg="red", font=("roboto", 20, "bold"))
    btn_exit.place(x=1075, y=580)

    root.mainloop()

if __name__ == "__main__":
    main()
