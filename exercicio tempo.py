tempoSegundos = int(input("Indique o tempo em segundos "))
tempoHoras = tempoSegundos/3600
tempoMinutos = (tempoHoras - int(tempoHoras))*60
tempoSegundo = (tempoMinutos - int(tempoMinutos))*60
print("{:.0f} horas {:.0f} minutos e {:.0f} segundos" .format(tempoHoras, tempoMinutos , tempoSegundo))
