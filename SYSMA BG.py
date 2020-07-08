import os
import time

import psutil

from sysmalibs import redprint,CPU_VM,speak
import datetime
now = datetime.datetime.now()

current_time=(now.strftime("%Y-%m-%d %H:%M:%S"))

try:
 os.startfile('Console.py')
except FileNotFoundError:
    redprint('Console not found')
    log = open('logs/Console.log', 'a')
    log.write(
        "\n=============================================================================================================================\nConsole File was not found\nerror occurred during " + current_time)
    log.close()
    quit()
except :
    redprint('UNABLE TO OPEN CONSOLE')
    log=open('logs/Console.log', 'a')
    log.write(
        "\n=============================================================================================================================\nConsole was not opened in specified time\nerror occurred during " + current_time)
    log.close()
    quit()


def ramerr():
  y=open('/logs/RAMERR.log','a')
  y.write("\n=============================================================================================================================\nRam usage was above 90% at" + current_time)


  #___________________________________________________________________________________________________________________________________________________________________________________________-
###################MAIN#########################
###############SYSTEM CHECKER###################
#___________________________________________________________________________________________________________________________________________



while 0==0:
    current_time = (now.strftime("%Y-%m-%d %H:%M:%S"))
    CPUstat = dict(psutil.cpu_stats()._asdict())
    VM = dict(psutil.virtual_memory()._asdict())
    time.sleep(1)
    RAM=VM.get('percent')
    print(RAM)
    if RAM > 90.0 :
        current_time = (now.strftime("%Y-%m-%d %I:%M:%S"))
        print('RAM Usage is Above 90 %')
        print('Scanning for unused processes')
        x=open('/logs/RAM.json','a')
        x.write('{"RAMERR":"1"}')
        x.close()
        ramerr()
        size=os.stat('/logs/RAM.log').st_size
        if size > (25000000):
            os.remove('/logs/RAM.log')
    else:
        current_time = (now.strftime("%Y-%m-%d %H:%M:%S"))
        x=open('logs/RAM.json','w+')
        x.write('{"RAMERR":"0"}')
        x.close()
        log=open('logs/RAM.log','a')
        log.write( "\n=============================================================================================================================\nRAM usage was normal\nit was "+str(RAM)+" during " + current_time)
        log.close()
