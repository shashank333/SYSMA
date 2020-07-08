import os

print('initiating Libraries')


try:
    import psutil
    import time
    from termcolor import colored, cprint
    from win10toast import ToastNotifier
    n=ToastNotifier()
except:
    print('A fatal error occured while importing modules')
    os.startfile('/error scripts/script errors/module error.vbs')

def notify(title,message,time):
    n.show_toast(title=title,msg=message,duration=time)

def initiatesuccess():
    print('===================================================================')
    time.sleep(2)
    print('=                 SYSMA was successfully initiated                =')
    time.sleep(1)
    print('===================================================================')
    time.sleep(1)
    print(colored('                   connecting to SYSMA console                    ', 'red'))


def redprint(text):
    print(colored(text,'red'))


def CPU_VM():
    CPUstat = dict(psutil.cpu_stats()._asdict())
    VM = dict(psutil.virtual_memory()._asdict())
    print(VM)
    print(CPUstat)


def speak(message):
    print(message)


initiatesuccess()
time.sleep(2)
redprint('successfully connected to SYSMA console')
time.sleep(2)
redprint('Getting SYS stats')
time.sleep(3)
CPU_VM()
time.sleep(2)
redprint('succesfully connected to System Root')
time.sleep(2)
redprint('switching to console, please wait')
