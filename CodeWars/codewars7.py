"""
Write a function named setAlarm/set_alarm/set-alarm/setalarm 
(depending on language) which receives two parameters. The first 
parameter, employed, is true whenever you are employed and the 
second parameter, vacation is true whenever you are on vacation.

The function should return true if you are employed and not on 
vacation (because these are the circumstances under which you 
need to set an alarm). It should return false otherwise.
"""
def setAlarm(estado):
    if estadoTrabalho.upper()=="v" and estadoFerias.upper()=="f":
        employed=True
    elif estadoTrabalho.upper=="f":
        employed=False
    else:
        print("Falha")
    if estadoFerias.upper()=="v":
        Ferias=True
    elif estadoFerias.upper()=="f":
        Ferias=False
    else:
        print("Falha volte a tentar")
    

estadoTrabalho=str(input("Empregado V/F: "))
estadoFerias=str(input("Ferias V/F:"))