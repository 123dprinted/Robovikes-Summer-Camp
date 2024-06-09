from tkinter import *
import customtkinter as ctk

class RobotPanel():
    def __init__(self):
        self.root = ctk.CTk()
        self.root.geometry('820x450')
        
        ctk.set_appearance_mode("dark")


    def main(self):
        #empty main panel label
        label = ctk.CTkLabel(master=self.root, text="Select a robot to view its options.", font=("Arial", 25))
        label.grid(row=0, column=1)
        #construct connection frame
        frame = ctk.CTkFrame(master=self.root, width=200, height=450)
        frame.grid(row=0, column=0)

        self.root.mainloop()


if __name__ == "__main__":
    panel = RobotPanel()
    panel.main()