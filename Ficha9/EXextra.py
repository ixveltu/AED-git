import customtkinter
import CTkMessagebox

#Funçao messagebox
def messageSair():
    #Definir resolucao de message box
    witdhMessage=200
    heightMessage=200
    x = (screenWidth/2) - (witdhMessage/2)
    y = (screenHeight/2) - (heightMessage/2)
    CTkMessagebox.CTkMessagebox(width=200, height=200)
    CTkMessagebox.CTkMessagebox.geometry((f"{widthMessage}x{heightMessage}+{int(x)}+{int(y)}"))
    #Formatar messagebox
    CTkMessagebox.CTkMessagebox(title="Sair da Aplicação?", message="Deseja sair da aplicação?", option_1="Sim", option_2="Não", option_3="Cancelar")



#Abrir app
app = customtkinter.CTk()
app.title("Demo dos containers")

#Resoluçao
appwidth = 400
appheight = 500
screenWidth = app.winfo_screenwidth()
screenHeight = app.winfo_screenheight()

x = (screenWidth/2) - (appwidth/2)
y = (screenHeight/2) - (appheight/2)
app.geometry(f"{appwidth}x{appheight}+{int(x)}+{int(y)}")
app.resizable(False,False)

#Definir tabview
tabview = customtkinter.CTkTabview(app, width=400, height=400, fg_color="black")
tabview.pack(padx=20, pady=20)

#Tabview
tabGestor = tabview.add("Gestor de faltas")
tabConsultar = tabview.add("Consultar")

#Buttons
buttonSair = customtkinter.CTkButton(app, command=messageSair, width=300, height=30, bg_color="blue", text="Sair da Aplicação", text_color="white")
buttonSair.place(x=50, y=350) 

buttonAdmin = customtkinter.CTkButton(app, command="", width=300, height=30, bg_color="blue", text="Ver Painel de Admin", text_color="white")
buttonAdmin.place(x=50, y=385)

#Label
labelImagem = customtkinter.CTkLabel(app, text="", text_color="red", font=("Helvetica",14), width=300, height=280)
labelImagem.place(x=50, y=60)


app.mainloop()