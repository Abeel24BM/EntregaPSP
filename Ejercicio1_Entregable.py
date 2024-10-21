

import psutil

#Queremos mostrar por consola todos los procesos con su respectivo ID
#En el caso de que, encontremos un proceso llamado notepad.exe, lo mostraremos por pantalla
#Para ello, crearemos un booleano para establecer una condición
try:
    notepad = False
    for proc in psutil.process_iter():
        processName = proc.name()
        processID = proc.pid

        print('Nombre del proceso. ',processName, '; ID del proceso: ', processID)

        if processName == 'notepad.exe':
            notepad = True
            notepadID = processID

    if notepad == True:
        print("Hemos encontrado el bloc de notas con el PID: ", notepadID)

except:
    print("error")

