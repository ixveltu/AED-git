import customtkinter
import os
def calcularPeso():
    peso = (int(altura.get())-100)-(int(altura.get())-150)/int(k.get())
    labelResposta.configure(text=str(peso))


#Abrir app
app = customtkinter.CTk()
app.title("My Notepad")

#Resoluçao
appwidth = 370
appheight = 430

screenWidth = app.winfo_screenwidth()
screenHeight = app.winfo_screenheight()

x = (screenWidth/2) - (appwidth/2)
y = (screenHeight/2) - (appheight/2)
app.geometry(f"{appwidth}x{appheight}+{int(x)}+{int(y)}")
app.resizable(False,False)
#app.configure(fg_color = "white")

#Textos
labelAltura = customtkinter.CTkLabel(app, text="Altura em cm", text_color="black", font=("Helvetica",14))
labelAltura.place(x=15, y=30)

labelGenero = customtkinter.CTkLabel(app, text="Genero", text_color="black", font=("Helvetica",14))
labelGenero.place(x=50, y=60)

labelPesoIdeal = customtkinter.CTkLabel(app, text="O seu peso ideal é", text_color="red", font=("Helvetica",14))
labelPesoIdeal.place(x=120, y=220)

labelResposta = customtkinter.CTkLabel(app, text="", text_color="red", font=("Helvetica",14))
labelResposta.place(x=50, y=260)

#RadioButton
k = customtkinter.StringVar(value=4)
radioButton1 = customtkinter.CTkRadioButton(app, text="Masculino", variable=k, value=4)
radioButton1.place(x=150, y=80)

radioButton2 = customtkinter.CTkRadioButton(app, text="Feminino", variable=k, value=2)
radioButton2.place(x=150, y=110)

#Entry
altura = customtkinter.StringVar()
entryAltura = customtkinter.CTkEntry(app, textvariable=altura, placeholder_text="100", width=150, font=("Helvitica",14))
entryAltura.place(x=120, y=30)

#Button
buttonCalcular = customtkinter.CTkButton(app, command=calcularPeso, width=370, height=50, bg_color="black", text="Calcular IMC", text_color="blue")
buttonCalcular.place(y=160) 




app.mainloop()