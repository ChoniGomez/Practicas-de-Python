from datetime import datetime


def dates():

    #fecha y hora actual
    date = datetime.now()
    #formatear la salida en anio, mes y dia
    fecha = datetime.strptime('%Y-%m-%d')
    #formatear la salida en horas, minutos segundos formato 24hs
    new_format_24 = date.strftime('%H:%M:%S')
    #formatear la salida en horas, minutos segundos formato 12hs. Con P para indicar si es AM o PM
    new_format_12 = date.strftime('%I:%M:%S %p')

    print("dia", fecha)
    print("date", date)
    print("24 Hours: ", new_format_24)
    print("AM/PM: ", new_format_12)