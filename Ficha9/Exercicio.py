import customtkinter

#Variaveis
listaContinentes = ["Ásia", "Africa", "Europa", "Ocêania", "América", "Antártica"]
app = customtkinter.CTk()
app.title("Países do Mundo!")

appwidth = 600
appheight = 300

screenWidth = app.winfo_screenwidth()
screenHeight = app.winfo_screenheight()

#Resoluçao
x = (screenWidth/2) - (appwidth/2)
y = (screenHeight/2) - (appheight/2)
app.geometry(f"{appheight}x{appwidth}+{int(x)}+{int(y)}")
app.resizable(False,False)
app.configure(fg_color = "white")

#Textos
labelPaís = customtkinter.CTkLabel(app, text="País", text_color="black", font=("Helvetica",14))
labelPaís.place(x=15, y=30)

#Textos
labelContinente = customtkinter.CTkLabel(app, text="Continente", text_color="black", font=("Helvetica",14))
labelContinente.place(x=15, y=70)

#Entrytext
entryPais = customtkinter.CTkEntry(app, placeholder_text="Portugal", width=150, font=("Helvitica",14))
entryPais.place(x=60, y=30)

#ComboBox
comboContinentes = customtkinter.CTkComboBox(app, values=listaContinentes, width=150, command="")
comboContinentes.place(x=60, y=70)
comboContinentes.set("Europa")

#RadioButton
radioVariable = customtkinter.StringVar(value="Norte")
radioButton1 = customtkinter.CTkRadioButton(app, text="Norte", variable=radioVariable, value="Norte")
radioButton1.place(x=150, y=200)

radioButton2 = customtkinter.CTkRadioButton(app, text="Sul", variable=radioVariable, value="Sul")
radioButton2.place(x=150, y=300)

#CheckBox
checkVar1 = customtkinter.StringVar(value="on")
checkVar2 = customtkinter.StringVar(value="off")
checkVar3 = customtkinter.StringVar(value="on")
checkVar4 = customtkinter.StringVar(value="off")

checkboxIN = customtkinter.CTkCheckBox(app, text="Inglês", variable=checkVar1, onvalue="on", offvalue="off")
checkboxPT = customtkinter.CTkCheckBox(app, text="Português", variable=checkVar2, onvalue="on", offvalue="off")
checkboxFR = customtkinter.CTkCheckBox(app, text="Francês", variable=checkVar3, onvalue="on", offvalue="off")
checkboxOU = customtkinter.CTkCheckBox(app, text="Outro", variable=checkVar4, onvalue="on", offvalue="off")

checkboxIN.place(x=220, y=120)
checkboxPT.place(x=220, y=150)
checkboxFR.place(x=260, y=120)
checkboxOU.place(x=260, y=150)

app.mainloop()