
import psutil
import subprocess


#Haremos un bucle buscando el notepad ya que sera el proceso que queremos eliminar
#Si el bucle encuentra el notepad nos imprime por consola el id del proceso
#Si no lo encuentra, terminamos el programa
notepad = False
try:
    for proc in psutil.process_iter():
        processName = proc.name()
        processID = proc.pid
        #Buscamos notepad.exe
        if processName == 'notepad.exe':
            print('Nombre del proceso. ', processName, '; ID del proceso: ', processID)
            notepad = True
            #Simulación de introducción el valor por consola
            print("Ingresame el PID del proceso el cual quieres terminar")
            value = int(input())

            # Une vez recibidos los datos debemos de recorrer los procesos comprobando que hay algun ID que existe como el introducido
            try:
                for proc in psutil.process_iter():
                    processName = proc.name()
                    processID = proc.pid

                    if processID == value:
                        proc.kill()
            except:
                print("error")
except:
    print("error")

if notepad == False:
    print('Notepad no encontrado')


