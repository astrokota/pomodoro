import unittest
from unittest.mock import patch
import tkinter as tk
import main

# ==========================
# VALIDATION/UNIT TESTING
# ==========================

class TestPomodoroTimer(unittest.TestCase):

    def setUp(self):
        """Reset timer states and mock GUI variables before each test"""
        main.root = tk.Tk()  #Creates a Tk instance for testing
        main.min_var = tk.StringVar(main.root, value="25")
        main.sec_var = tk.StringVar(main.root, value="00")

        main.current_timer = 0
        main.timer_running = False
        main.paused_timer = 0

    def tearDown(self):
        """Destroy the Tk instance after tests"""
        main.root.destroy()

    def test_start_timer(self):
        """Test if the timer starts correctly"""
        main.start_timer(1500)  #25 minutes
        self.assertIn(main.current_timer, [1500, 1499])  #Allows for immediate decrement to avoid timing error
        self.assertTrue(main.timer_running)

    def test_pause_timer(self):
        """Test if the timer pauses correctly"""
        main.start_timer(1500)
        main.pause_timer()
        self.assertFalse(main.timer_running)
        self.assertIn(main.paused_timer, [1500, 1499])  #Allows for immediate decrement to avoid timing error

    def test_resume_timer(self):
        """Test if the timer resumes correctly"""
        main.start_timer(1500)
        main.pause_timer()
        main.resume_timer()
        self.assertIn(main.current_timer, [1500, 1498])  #Allows for 2-second difference to avoid timing error
        self.assertTrue(main.timer_running)

    def test_stop_timer(self):
        """Test if the timer stops and resets correctly"""
        main.start_timer(1500)
        main.stop_timer()
        self.assertFalse(main.timer_running)
        self.assertEqual(main.current_timer, 0)
        self.assertEqual(main.paused_timer, 0)

    @patch("main.playsound")  #Mocks playsound to prevent errors
    @patch("main.messagebox.showinfo")  #Mocks messagebox to avoid GUI popups
    def test_update_clock(self, mock_messagebox, mock_playsound):
        """Test if update_clock stops timer and plays sound at 0"""
        main.current_timer = 1
        main.timer_running = True
        main.update_clock()  #Sets current_timer to 0
        main.update_clock()  #Ensures timer fully stops

        self.assertEqual(main.current_timer, 0)
        self.assertFalse(main.timer_running)  #Timer is stopped
        mock_playsound.assert_called_once_with("alarm.wav")
        mock_messagebox.assert_called_once_with("Session is over.")

if __name__ == '__main__':
    unittest.main()

