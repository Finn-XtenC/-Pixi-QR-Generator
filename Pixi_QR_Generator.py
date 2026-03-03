import time
import qrcode
from colorama import init, Fore
init()
import sys

def animate():
    for i in range(101):
        print(Fore.YELLOW + f"\rchecking {i}%", end="" + Fore.WHITE)
        time.sleep(0.05)

animate()


def loading():

    for i in range(101):
        print(Fore.YELLOW + f"\rloading {i}%", end="" + Fore.WHITE)
        time.sleep(0.05)
    print('\n<------------------------------>')
    print(Fore.GREEN + "\nSuccessfull!")

print('\n<------------------------------>')
print(Fore.GREEN + '\nPIXI QR GENERATOR' + Fore.WHITE)
print('\n<------------------------------>')
namaUser = input(Fore.CYAN + '\nMasukan Usename: ')
password = input (Fore.CYAN + 'Masukan Password: ' + Fore.WHITE)
if password == 'antiName':
    print('\n<------------------------------>')
    print(Fore.GREEN+ f'\nWellcome back {namaUser}!' + Fore.WHITE)
    print('\n<------------------------------>')
    url = input(Fore.BLUE + '\nMasukan URL: ')
    qrname = input(Fore.BLUE + 'Masukan nama file: ' + Fore.WHITE)
    print('\n<------------------------------>')
    loading()
    generate = qrcode.make(url)
    generate.save(qrname + '.png')
else:
    print(Fore.RED + 'INVALID')
    sys.exit()