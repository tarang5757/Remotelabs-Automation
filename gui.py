
import customtkinter as ctk
import subprocess
import main
from main import Automation

class LoginApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title('Login')
        self.geometry('400x250')
        self.resizable(False, False)


        # Configure the grid layout manager
        self.grid_columnconfigure(1, weight=1)

        # Create widgets
        self.create_widgets()

    def create_widgets(self):
        # Username
        ctk.CTkLabel(self, text="Username:").grid(row=0, column=0, padx=20, pady=(20, 10), sticky="w")
        self.username_entry = ctk.CTkEntry(self, placeholder_text="Enter your username")
        self.username_entry.grid(row=0, column=1, padx=20, pady=(20, 10), sticky="ew")

        # Password
        ctk.CTkLabel(self, text="Password:").grid(row=1, column=0, padx=20, pady=10, sticky="w")
        self.password_entry = ctk.CTkEntry(self, placeholder_text="Enter your password", show="*")
        self.password_entry.grid(row=1, column=1, padx=20, pady=10, sticky="ew")

        # Login button
        login_button = ctk.CTkButton(self, text="Login", command=self.login)
        login_button.grid(row=2, column=1, padx=20, pady=(10, 20), sticky="e")

        

        self.grid_rowconfigure(3, weight=1)  #this makes the rows above expand to fill space, pushing the label to the bottom
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        author_label = ctk.CTkLabel(self, text="Created By Tarang", font=("Roboto", 16), text_color="#E83845")
        author_label.grid(row=3, column=0, columnspan=2, sticky="s")  

        
        author_label.grid(padx=20, pady=(0, 10))




    def login(self):
        # Placeholder for login action
        username = self.username_entry.get()
        password = self.password_entry.get()


        self.destroy()

        Automation(username, password)




if __name__ == "__main__":
    app = LoginApp()
    app.mainloop()
