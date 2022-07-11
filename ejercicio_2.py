import time

hora = int(time.strftime('%H'))
minutos = int(time.strftime('%M'))

if (hora >= 19):
    print("Es hora de volver a casa!! :)")
else:
    print("Quedan " + str(18 - hora) + " hs " + str(59 - minutos) + " minutos.")
