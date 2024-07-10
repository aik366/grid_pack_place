import customtkinter as ctk

ctk.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

app = ctk.CTk()
app.geometry("+600+350")
app.resizable(False, False)

def color_button(button, fg_color, hover_color):
    button.configure(fg_color=fg_color, hover_color=hover_color)


# def grid_forget(frame):
#     frame.grid_forget()


def if_forget_2():
    if frame2.grid_info():
        frame2.grid_forget()
        color_button(button1, "#56743D", "#718C35")
    else:
        frame3.grid_forget()
        frame2.grid(row=0, column=1, ipadx=20, ipady=20, sticky="NSEW")
        button1.configure(fg_color=frame2.cget("fg_color"), hover_color=frame2.cget("fg_color"), )
        color_button(button1_1, "#56743D", "#718C35")


def if_forget_3():
    if frame3.grid_info():
        frame3.grid_forget()
        color_button(button1_1, "#56743D", "#718C35")
    else:
        frame2.grid_forget()
        frame3.grid(row=0, column=1, ipadx=20, ipady=20, sticky="NSEW")
        button1_1.configure(fg_color=frame3.cget("fg_color"), hover_color=frame3.cget("fg_color"))
        color_button(button1, "#56743D", "#718C35")


frame1 = ctk.CTkFrame(app, fg_color="#473363", corner_radius=0, border_width=0)
frame1.grid(row=0, column=0, ipadx=20, ipady=20, sticky="NSEW")
label1 = ctk.CTkLabel(frame1, text="frame1 label", font=("Arial", 30))
label1.pack(pady=10)
entry1 = ctk.CTkEntry(frame1, placeholder_text="frame1 entry", height=40)
entry1.pack(pady=10)
button1 = ctk.CTkButton(frame1, text="grid_forget(frame2)", height=40, corner_radius=0, command=if_forget_2)
button1.pack(pady=10, fill="x")
button1_1 = ctk.CTkButton(frame1, text="grid_forget(frame3)", height=40, corner_radius=0, command=if_forget_3)
button1_1.pack(pady=10, fill="x")

frame2 = ctk.CTkFrame(app, fg_color="#6C0D49", corner_radius=0, border_width=0)
frame2.grid(row=0, column=1, ipadx=20, ipady=20, sticky="NSEW")
label2 = ctk.CTkLabel(frame2, text="frame2 label", font=("Arial", 30))
label2.pack(pady=10)
entry2 = ctk.CTkEntry(frame2, placeholder_text="frame2 entry", height=40)
entry2.pack(pady=10)
button2 = ctk.CTkButton(frame2, text="frame2 button", height=40)
button2.pack(pady=10)

frame3 = ctk.CTkFrame(app, fg_color="#525BD2", corner_radius=0, border_width=0)
frame3.grid(row=0, column=1, ipadx=20, ipady=20, sticky="NSEW")
label3 = ctk.CTkLabel(frame3, text="frame3 label", font=("Arial", 30))
label3.pack(pady=10)
entry3 = ctk.CTkEntry(frame3, placeholder_text="frame3 entry", height=40)
entry3.pack(pady=10)
button3 = ctk.CTkButton(frame3, text="frame3 button", height=40, )
button3.pack(pady=10)

color_button(button1, "#56743D", "#718C35")
color_button(button1_1, "#56743D", "#718C35")
color_button(button2, "#56743D", "#718C35")
color_button(button3, "#56743D", "#718C35")

frame2.grid_forget()
frame3.grid_forget()

if __name__ == '__main__':
    app.mainloop()