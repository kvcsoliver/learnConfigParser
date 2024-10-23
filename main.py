import customtkinter as ctk
import configparser
import os
import platformdirs  # Use platformdirs to handle AppData path


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        # ---------------------------- Basic settings
        ctk.set_appearance_mode("Dark")
        ctk.set_default_color_theme("blue")
        self.title("Config Test")
        self.geometry(f"{400}x{200}")
        self.my_font = ctk.CTkFont(family="Segoe UI Bold", size=14)

        # ---------------------------- Grid layout
        self.grid_columnconfigure([0, 1, 2], weight=1)
        self.grid_rowconfigure([0], weight=1)

        # ---------------------------- Variables
        self.num_var = ctk.IntVar()
        self.num_var.set(1)

        # ---------------------------- Features
        self.value = ctk.CTkLabel(self, textvariable=self.num_var, font=ctk.CTkFont(family="Segoe UI Bold", size=30))
        self.value.grid(row=0, column=0)

        self.plus_btn = ctk.CTkButton(self, command=self.add_one, text="Add One", font=self.my_font)
        self.plus_btn.grid(row=0, column=1)

        self.minus_btn = ctk.CTkButton(self, command=self.sub_one, text="Subtract One", font=self.my_font)
        self.minus_btn.grid(row=0, column=2)

        # ---------------------------- Load key bindings from config file
        self.load_key_bindings()

    def load_key_bindings(self):
        config = configparser.ConfigParser()

        # Default key bindings
        default_key_bindings = {
            "add_one_keys": ["plus", "space"],
            "sub_one_keys": ["minus", "Control_L"]
        }

        # Get the user-specific AppData directory for the config file
        config_dir = platformdirs.user_config_dir("learnConfigParser", "Oliversion")
        os.makedirs(config_dir, exist_ok=True)  # Ensure the directory exists
        config_file = os.path.join(config_dir, "config.ini")

        # Check if the config file exists
        if os.path.exists(config_file):
            config.read(config_file)
            try:
                add_one_keys = config.get("KeyBindings", "add_one_keys").split(",")
                sub_one_keys = config.get("KeyBindings", "sub_one_keys").split(",")
            except (configparser.NoOptionError, configparser.NoSectionError) as e:
                print(f"Error loading config: {e}. Using default key bindings.")
                add_one_keys = default_key_bindings["add_one_keys"]
                sub_one_keys = default_key_bindings["sub_one_keys"]
        else:
            print(f"Config file not found. Creating a new one in {config_file} with default key bindings.")
            # Write default values to the new config.ini file
            config["KeyBindings"] = {
                "add_one_keys": ",".join(default_key_bindings["add_one_keys"]),
                "sub_one_keys": ",".join(default_key_bindings["sub_one_keys"]),
            }
            with open(config_file, "w") as configfile:
                config.write(configfile)

            # Use the default values since the config file is just created
            add_one_keys = default_key_bindings["add_one_keys"]
            sub_one_keys = default_key_bindings["sub_one_keys"]

        # Dictionary mapping functions to the keys loaded from the config file
        key_bindings = {
            self.add_one: add_one_keys,
            self.sub_one: sub_one_keys
        }

        # Loop through the dictionary to bind each key to its respective function
        for func, keys in key_bindings.items():
            for key in keys:
                key = f"<{key.strip()}>"  # Ensure the keys are wrapped with <>
                self.bind(key, func)

    def add_one(self, event=None) -> None:
        self.num_var.set(self.num_var.get() + 1)

    def sub_one(self, event=None) -> None:
        self.num_var.set(self.num_var.get() - 1)


if __name__ == "__main__":
    app = App()
    app.mainloop()
