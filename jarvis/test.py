import customtkinter as ctk
import tkinter

class App(ctk.CTk):
	def __init__(self):
		super().__init__()

		self.geometry("400x400")
		self.title("Jarvis")

app = App()
app.mainloop()



