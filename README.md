# Dakota's Pomodoro Timer - User Manual

**Version:** 1.0  
**Developer:** Dakota Mitchell / SDEV140 Final Project  
**Date:** March 2025  

## Table of Contents
- [Introduction](#introduction)
- [Installation & Requirements](#installation--requirements)
- [How to Use the Application](#how-to-use-the-application)
  - [Launching the Application](#launching-the-application)
  - [Main Timer (25-Minute Session)](#main-timer-25-minute-session)
  - [10-Minute Timer Session](#10-minute-timer-session)
  - [Pause, Resume, and Stop Functions](#pause-resume-and-stop-functions)
  - [Exiting the Application](#exiting-the-application)
- [Troubleshooting & FAQs](#troubleshooting--faqs)
- [Contact & Support](#contact--support)

---

## Introduction
Dakota's Pomodoro Timer is a simple time-management application based on the Pomodoro Technique, which helps improve focus and productivity. It includes a 25-minute session and a 10-minute session, allowing users to efficiently use their time while solving problems or working on tasks. The Pomodoro technique helps mitigate fatigue and burnout by segmenting work into focused intervals with breaks.

---

## Installation & Requirements

### System Requirements
- **Operating System:** Windows, macOS, or Linux  
- **Python Version:** Python 3.x  

### Dependencies
- `tkinter` (for GUI)
- `PIL` (Pillow) (for handling images)
- `playsound` (for playing the alarm sound)

### Installation Steps
1. Install Python (if not already installed) from [python.org](https://www.python.org).
2. Install the required dependencies by running:

   
   pip install pillow playsound tk
   

3. Download the program files, including the `alarm.wav` sound file and background images.

---

## How to Use the Application

### Launching the Application
1. Open a terminal or command prompt.
2. Navigate to the folder containing the `main` file.
3. Run the script with:

   
   python -m main
   

4. The main application window will appear with the 25-minute Pomodoro timer and control buttons.

### Main Timer (25-Minute Session)
- The main window features a **25-minute countdown timer** by default.
- To start a 25-minute session, click:
  **🔴 "Start 25min"**
- The timer will count down from **25:00 to 00:00**.
- When the time reaches 0, an **alarm sound** will play, and a message will notify you that the session is over.

### 10-Minute Timer Session
- Click **🔴 "10min Session"** to open a separate window with a **10-minute countdown timer**.
- In this new window, click **"Start 10min"** to begin the 10-minute session.
- The countdown will start from **10:00 to 00:00**.
- Once time runs out, an alarm sound will play, and a message will appear.

### Pause, Resume, and Stop Functions

#### **Pausing the Timer**
You can pause the countdown at any time by clicking:  
- 🔴 **"Pause"** (for 25-minute timer)  
- 🔴 **"Pause"** (for 10-minute timer)  

#### **Resuming a Paused Timer**
To continue the countdown from where you left off, click:  
- 🔴 **"Resume"**  

#### **Stopping the Timer**
- Clicking **"Stop"** will reset the timer to **00:00** and halt the session.
- To start a new session, click **"Start 25min"** or **"Start 10min"** again.

### Exiting the Application
- Click **🔴 "Exit"** to close the application.
- If using the **10-minute session window**, clicking **"Exit"** will only close that window while keeping the **main timer running**.

### Testing the Application
1. Open a terminal or command prompt.
2. Navigate to the folder containing the `main` file.
3. Run the script with:

   
   python -m unittest test
   

4. The console should display "OK" without errors/failures.
---

## Troubleshooting & FAQs

### **Q1: The alarm sound is not playing.**
✅ Ensure the file **"alarm.wav"** is in the same folder as the script.  
✅ Check if your system audio is enabled and volume is up.  
✅ Reinstall `playsound` using:


pip install playsound


### **Q2: Can I change the session durations?**
✅ The default session times are **25 minutes** and **10 minutes**, but you can modify the script by changing:


start_timer(25*60)  # Change 25 to your preferred minutes  
start_timer_10(10*60)  # Change 10 to your preferred minutes  


---

## Contact & Support
For questions, suggestions, or bug reports, contact:  

🔗 [https://github.com/astrokota](https://github.com/astrokota)

---
