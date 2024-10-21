import psutil
import time


#Creamos un bucle infinito y posteriormente un bucle para recorrer los procesos
while True:
    for proc in psutil.process_iter(attrs=['pid', 'name', 'cpu_percent', 'memory_info']):
        try:
            #Obtenemos la información de cada proceso
            pid = proc.info['pid']
            nombre = proc.info['name']
            cpu = proc.info['cpu_percent']
            memoria = proc.info['memory_info'].rss / (1024 * 1024)  #Convertimos la memoria en MB
            print(f"PID: {pid}, Nombre: {nombre}, CPU: {cpu}%, Memoria: {memoria:.2f} MB")
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue

    print("\nPresiona 'q' para salir o 'Enter' para refrescar.")
    opcion = input()
    #Salida del bucle si teclea q
    if opcion.lower() == 'q':
        break
    time.sleep(2)
