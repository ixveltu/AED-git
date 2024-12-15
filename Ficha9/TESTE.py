"""Abre no centro da tela"""
import customtkinter

listaIdade = ["1","2","3"]


app = customtkinter.CTk()
app.title("Migas")

appwidth = 800
appheight = 800

screenWidth = app.winfo_screenwidth()
screenHeight = app.winfo_screenheight()

x = (screenWidth/2) - (appwidth/2)
y = (screenHeight/2) - (appheight/2)
app.geometry(f"{appheight}x{appwidth}+{int(x)}+{int(y)}")
app.resizable(False,False)
app.configure(fg_color = "white")

labelNome = customtkinter.CTkLabel(app, text="Nome", text_color="black", font=("Arial",16))
labelNome.place(x=15, y=30)

labelIdade = customtkinter.CTkLabel(app, text="Idade", text_color="black", font=("Arial",16))
labelIdade.place(x=15, y=70)

entryNome = customtkinter.CTkEntry(app, placeholder_text="Seu nome", width=200)
entryNome.place(x=60, y=30)

comboIdade = customtkinter.CTkComboBox(app, values=listaIdade, width=30, command="")
comboIdade.place(x=60, y=70)
comboIdade.set("0")

print(entryNome.get())


app.mainloop()
"""Abre no canto da tela"""
# import customtkinter

# app = customtkinter.CTk()
# app.title("Migas")


# appwidth = 800
# appheight = 800

# screenWidth = app.winfo_screenwidth()
# screenHeight = app.winfo_screenheight()

# x=0
# y=0
# app.geometry(f"{appheight}x{appwidth}+{int(x)}+{int(y)}")
# app.resizable(False,False)


# app.mainloop()