import psutil


def recursos_usados():
    #nucleos fisicos
    nucleos = psutil.cpu_count(logical=False)
    print("Cantidad de núcleos fisicos:", nucleos)

    #nucleos fisicos logicos
    nucleos = psutil.cpu_count(logical=True)
    print("Cantidad de núcleos logicos:", nucleos)

    #procesos que se corren o estan esperando para correr en la CPU
    carga = psutil.getloadavg()
    print("Carga promedio:", carga)

    #procentaje de uso de la cpu durante un intervalo de tiempo
    uso = psutil.cpu_percent(interval=5, percpu=True)
    print("Porcentaje de uso de la CPU:", uso)


recursos_usados()