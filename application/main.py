import customtkinter
from generate import gen
from customElements import AppTitle, Spinbox, optionsFrame, Footer
from file_management import generate_path, _internal, assets_folder

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        title_font = customtkinter.CTkFont(family="Cascadia Code", size=80)
        default_font = customtkinter.CTkFont(family="Cascadia Code", size=24)
        footer_font = customtkinter.CTkFont(family="Cascadia Code", size=16)

        self.title('Password Generator')
        self.geometry('1280x720')
        self.minsize(1280, 720)
        internal_folder = _internal()
        file_name = 'logo.ico'
        if internal_folder:
            ico = generate_path(internal_folder.as_posix(), 'assets', file_name)
        elif not internal_folder:
            ico = generate_path(assets_folder().as_posix(), file_name)
        if ico:
            self.iconbitmap(ico)
    
        self.grid_columnconfigure((0, 1), weight=1)
        customtkinter.set_appearance_mode('dark')
        customtkinter.set_default_color_theme('green')

        self.title = AppTitle(self, title_font=title_font, subtitle_font=default_font, fg_color='transparent')
        self.title.grid(row=0, column=0, padx=20, pady=20, sticky="ew", columnspan=2)

        self.display = customtkinter.CTkEntry(self, height=40, font=default_font, placeholder_text='Your password')
        self.display.grid(row=2, column=0, padx=20, pady=20, sticky="ew", columnspan=2)

        self.title = customtkinter.CTkLabel(self, text='Length:', font=default_font)
        self.title.grid(row=3, column=0, padx=20, pady=(10, 10), sticky="w")

        self.spinBox = Spinbox(self, step_size=8, command=None, width=200, font=default_font, max=80, min=8)
        self.spinBox.grid(row=3, column=0, padx=20, pady=20, sticky="w", columnspan=2)

        self.optionsFrame = optionsFrame(self, fg_color='transparent', font=default_font, command=None)
        self.optionsFrame.grid(row=4, column=0, padx=20, pady=(0, 20), sticky='w', columnspan=2)

        self.button = customtkinter.CTkButton(self, height=40, text="Generate", font=default_font, command=self.generate_password)
        self.button.grid(row=2, column=1, pady=20, sticky="e")

        self.footer = Footer(self, font=footer_font, fg_color='transparent')
        self.footer.grid(row=10, column=0, pady=(0, 10), sticky="ew")

    def generate_password(self):
        try:
            config = self.optionsFrame.get()
            lower: bool = config['lower']
            upper: bool = config['upper']
            numbers: bool = config['numbers']
            special: bool = config['special']

            length: int = int(self.spinBox.get())

            result: str = gen(length=length, lower=lower, upper=upper, numbers=numbers, special=special)
            self.display.delete(0, 'end')
            self.display.insert(0, result)
        except:
            self.display.delete(0, 'end')
            self.display.insert(0, 'ERROR')

app = App()
app.mainloop()