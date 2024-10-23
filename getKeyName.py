import customtkinter as ctk

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Key Event Logger")
        self.geometry("300x200")

        # Label to display instructions
        self.label = ctk.CTkLabel(self, text="Press any key...", font=("Arial", 16))
        self.label.pack(pady=20)

        # Bind all key events to a function
        self.bind_all("<KeyPress>", self.print_key_name)

    def print_key_name(self, event):
        # Print the name of the key to the console
        print(f"Key pressed: {event.keysym}")

if __name__ == "__main__":
    app = App()
    app.mainloop()
