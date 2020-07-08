import os
import psutil
def copyright():
    print(
"""System Management agent (SYSMA) [Version 1.0.9.210]
(c) 2020 SasTech corporation. All rights reserved.""")


copyright()
print('type ? for help')
while 1 == 1:
    CPUstat = dict(psutil.cpu_stats()._asdict())
    VM = dict(psutil.virtual_memory()._asdict())
    CPUfreq=dict(psutil.cpu_freq()._asdict())

    x = input('Root@SYSMA:~$ ')
    if x == 'cpuusage':
        print(CPUstat)

    elif x == 'ramusage':
        print(VM)

    elif x == 'cmd':
        os.system('cmd')
    elif x=='taskmgr':
        os.system('taskmgr')
        pass
    elif x=='cls':
        os.system('cls')
    elif x=='reset':
        print('SYSMA was successfully reset')
    elif x=='whoami':
        y=str(os.system('whoami'))
    elif x=='assist':
        print('SYSMA UI is already running')
        print('SYSMA Assistant is already running')
    elif x=="sysma":
       copyright()
    elif x=="start":
        os.startfile('Console.py')
    elif x=="cpufreq":
        print(CPUfreq)
    elif x=="cpuper":
        inter=int(input('Enter the interval for CPU percent ~::~'))
        print(psutil.cpu_percent(interval=inter))
    elif x=='?':
        print("""
        taskmgr - opens task manager
        ramusage - tells ram's status
        cpuusage - tells cpu's status
        cpupercent-tells cpu's usage
        sysma [task to be killed] - kills specified task
        """)
    elif x=="":
        print('')
    else:
        print("command not found : " + x)
