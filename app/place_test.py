import customtkinter as ctk

ctk.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

app = ctk.CTk()
app.geometry("640x420+600+350")
app.resizable(False, False)


def place_forget():
    frame3.place_forget()
    app.geometry("430x420+600+350")


def place():
    frame3.place(x=430, y=10, )
    app.geometry("640x420+600+350")


frame1 = ctk.CTkFrame(app, fg_color="red", width=200, height=400)
frame1.place(x=10, y=10, )

button1 = ctk.CTkButton(frame1, text="Button 1", height=40, width=160, command=place_forget)
button1.place(x=20, y=20)

button1_1 = ctk.CTkButton(frame1, text="Button 1.1", height=40, width=160, command=place_forget)
button1_1.place(x=20, y=70)

button1_2 = ctk.CTkButton(frame1, text="Button 1.2", height=40, width=160, command=place)
button1_2.place(x=20, y=120)

frame2 = ctk.CTkFrame(app, fg_color="green", width=200, height=400)
frame2.place(x=220, y=10, )

button2 = ctk.CTkButton(frame2, text="Button 2", height=40, width=160, command=place)
button2.place(x=20, y=20)

frame3 = ctk.CTkFrame(app, fg_color="blue", width=200, height=400)
frame3.place(x=430, y=10, )

button3 = ctk.CTkButton(frame3, text="Button 3", height=40, width=160)
button3.place(x=20, y=20)

if __name__ == '__main__':
    app.mainloop()
