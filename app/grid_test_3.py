import customtkinter as cst

cst.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
cst.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"


class Pack(cst.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("500x400")

        self.frame_1 = cst.CTkFrame(self)
        self.frame_1.pack(side=cst.LEFT, fill="both", expand=True, padx=(10, 5), pady=10)

        self.frame_2 = cst.CTkFrame(self)
        self.frame_2.pack(side=cst.LEFT, fill="both", expand=True, padx=(5, 10), pady=10)


class Grid(cst.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("500x400")
        self.columnconfigure((0, 1), weight=1, uniform='a')
        self.rowconfigure(0, weight=3, uniform='a')
        self.rowconfigure(1, weight=1, uniform='a')

        self.frame_1 = cst.CTkFrame(self)
        self.frame_1.grid(row=0, column=0, sticky=cst.NSEW, padx=(10, 5), pady=10)

        self.frame_2 = cst.CTkFrame(self)
        self.frame_2.grid(row=0, column=1, sticky=cst.NSEW, padx=(5, 10), pady=10)

        self.frame_3 = cst.CTkFrame(self)
        self.frame_3.grid(row=1, column=0, columnspan=2, sticky=cst.NSEW, padx=10, pady=(0, 10))


class Place(cst.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("500x400")

        self.frame_1 = cst.CTkFrame(self)
        self.frame_1.place(x=10, y=10, relheight=0.95, relwidth=0.47)

        self.frame_2 = cst.CTkFrame(self)
        self.frame_2.place(relx=0.51, y=10, relheight=0.95, relwidth=0.47)


app = Grid()
app.mainloop()
