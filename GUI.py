import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from threading import Thread
from selenium import webdriver
from helpers.scraper import Scraper
from helpers.csv_helper import get_data_from_csv
from helpers.listing_helper import update_listings

# Global variable to indicate whether to stop the program
stop_program = False

# Function to run your code


def run_code():
    global stop_program
    try:
        # Get data for item type listings from csvs/items.csv
        messagebox.showinfo("Stopped", "Program runingn")

        # Check if the program should stop
        if stop_program:
            messagebox.showinfo("Stopped", "Program has been stopped.")
            return
        if stop_program:
            messagebox.showinfo("Stopped", "Program has been stopped.")
        else:
            messagebox.showinfo("Success", "Code executed successfully!")
    except Exception as e:
        if stop_program:
            messagebox.showinfo("Stopped", "Program has been stopped.")
        else:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

# Function to stop the program


def stop_program_func():
    global stop_program
    stop_program = True


# Create the main application window
root = tk.Tk()
root.title("Facebook Marketplace Scraper")
root.geometry("400x200")

# Create a frame for widgets
frame = ttk.Frame(root)
frame.pack(pady=20)

# Create a "Run" button
run_button = ttk.Button(frame, text="Run", command=run_code)
run_button.pack()

# Create a "Stop" button
stop_button = ttk.Button(frame, text="Stop", command=stop_program_func)
stop_button.pack()

# Start the GUI event loop
root.mainloop()
