import customtkinter
from PIL import Image
from file_management import generate_path, _internal, assets_folder

class AppTitle(customtkinter.CTkFrame):
    def __init__(self, *args,
                 title_font: None,
                 subtitle_font: None,
                 **kwargs):
        super().__init__(*args, **kwargs)

        self.grid_columnconfigure((0, 1), weight=1)

        internal_folder = _internal()
        file_name = 'logo.png'
        if internal_folder:
            src = generate_path(internal_folder.as_posix(), 'assets', file_name)
        elif not internal_folder:
            src = generate_path(assets_folder().as_posix(), file_name)
        if src:
            pil_src = Image.open(src)
            pil_img = customtkinter.CTkImage(None, pil_src, (200, 200))
        self.appLogo = customtkinter.CTkLabel(self, text='', image=pil_img)
        self.appLogo.grid(row=0, column=0, padx=(20, 0), pady=(20, 0), sticky="ew")

        self.title = customtkinter.CTkLabel(self, text='Password Generator', font=title_font, fg_color='transparent')
        self.title.grid(row=0, column=1, padx=(20, 0), pady=(20, 0), sticky="ew")

        self.subTitle = customtkinter.CTkLabel(self, text='Generates passwords, duh', font=subtitle_font)
        self.subTitle.grid(row=1, column=1, padx=20, pady=(0, 0), sticky="ew")

class Footer(customtkinter.CTkFrame):
    def __init__(self, *args,
                 font: customtkinter.CTkFont = None,
                 **kwargs):
        super().__init__(*args, **kwargs)

        self.author = customtkinter.CTkLabel(self, text='Copyright (c) 2024 Stalot', font=font)
        self.author.grid(row=0, column=0, padx=20, pady=(18, 0), sticky='w')

        self.version = customtkinter.CTkLabel(self, text='0.0.1 beta', font=font)
        self.version.grid(row=0, column=1, padx=20, pady=(18, 0), sticky='e')

class Spinbox(customtkinter.CTkFrame):
    def __init__(self, *args,
                 width: int = 100,
                 height: int = 32,
                 step_size: 1,
                 command: None,
                 font: None,
                 max: 100,
                 min: 0,
                 **kwargs):
        super().__init__(*args, width=width, height=height, **kwargs)

        self.step_size = step_size
        self.max = max
        self.min = min
        self.command = command

        self.configure(fg_color=("gray78", "gray28"))  # set frame color

        self.grid_columnconfigure((0, 2), weight=0)  # buttons don't expand
        self.grid_columnconfigure(1, weight=1)  # entry expands

        self.subtract_button = customtkinter.CTkButton(self, text="-", width=height+6, height=height-6, font=font,
                                                       command=self.subtract_button_callback)
        self.subtract_button.grid(row=0, column=0, padx=(3, 0), pady=3)

        self.entry = customtkinter.CTkEntry(self, width=width-(2*height), height=height-6, border_width=0, font=font)
        self.entry.grid(row=0, column=1, columnspan=1, padx=3, pady=3, sticky="ew")

        self.add_button = customtkinter.CTkButton(self, text="+", width=height+6, height=height-6, font=font,
                                                  command=self.add_button_callback)
        self.add_button.grid(row=0, column=2, padx=(0, 3), pady=3)

        # default value
        self.entry.insert(0, "8")

    def add_button_callback(self):
        if self.command is not None:
            self.command()
        try:
            value = int(self.entry.get())
            new_value = value + self.step_size
            if new_value <= self.max:
                self.entry.delete(0, "end")
                self.entry.insert(0, new_value)
        except ValueError:
            return

    def subtract_button_callback(self):
        if self.command is not None:
            self.command()
        try:
            value = int(self.entry.get())
            new_value = value - self.step_size
            if new_value >= self.min:
                self.entry.delete(0, "end")
                self.entry.insert(0, new_value)
        except ValueError:
            return

    def get(self) -> int:
        try:
            return int(self.entry.get())
        except ValueError:
            return None

    def set(self, value: int):
        self.entry.delete(0, "end")
        self.entry.insert(0, str(int(value)))

class optionsFrame(customtkinter.CTkFrame):
    def __init__(self, *args,
                 command: None,
                 font: None,
                 **kwargs):
        super().__init__(*args, **kwargs)

        self.command = command

        switch_w = 50
        switch_h = 25

        self.lowercase = customtkinter.CTkSwitch(self, switch_width=switch_w, switch_height=switch_h, text='Lower case', font=font, command=self.lower_callback)
        self.lowercase.grid(row=0, column=0, padx=0, pady=6, sticky='w')

        self.uppercase = customtkinter.CTkSwitch(self, switch_width=switch_w, switch_height=switch_h, text='Upper case', font=font, command=self.upper_callback)
        self.uppercase.grid(row=1, column=0, padx=0, pady=6, sticky="w")

        self.numberplace = customtkinter.CTkSwitch(self, switch_width=switch_w, switch_height=switch_h, text='Numbers', font=font, command=self.numbers_callback)
        self.numberplace.grid(row=2, column=0, padx=0, pady=6, sticky="w")

        self.specialChars = customtkinter.CTkSwitch(self, switch_width=switch_w, switch_height=switch_h, text='Special', font=font, command=self.special_callback)
        self.specialChars.grid(row=3, column=0, padx=0, pady=6, sticky="w")

    lower: bool = False
    upper: bool = False
    numbers: bool = False
    special: bool = False

    def lower_callback(self):
        if self.command is not None:
            self.command()
        try:
            value = bool(self.lowercase.get())
            self.lower = value
        except ValueError:
            return

    def upper_callback(self):
        if self.command is not None:
            self.command()
        try:
            value = bool(self.uppercase.get())
            self.upper = value
        except ValueError:
            return

    def numbers_callback(self):
        if self.command is not None:
            self.command()
        try:
            value = bool(self.numberplace.get())
            self.numbers = value
        except ValueError:
            return

    def special_callback(self):
        if self.command is not None:
            self.command()
        try:
            value = bool(self.specialChars.get())
            self.special = value
        except ValueError:
            return

    def get(self) -> dict:
        try:
            return dict(lower=self.lower, upper=self.upper, numbers=self.numbers, special=self.special)
        except ValueError:
            return None

class Display(customtkinter.CTkFrame):
    def __init__(self, *args,
                 command: None,
                 font: None,
                 **kwargs):
        super().__init__(*args, **kwargs)

        self.grid_columnconfigure((0, 1), weight=1)
    
        self.display = customtkinter.CTkEntry(self, height=40, font=font, placeholder_text='Your password')
        self.display.grid(row=0, column=0, padx=20, pady=20, sticky="ew")