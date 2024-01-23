import telnetlib
import time


# Variáveis

user = "admin"
password = ""


# Funções

def configura_telnet(host):
    print(f"Tentando acessar a impressora {host}...")

    #Login
    tn = telnetlib.Telnet(host)

    time.sleep(0.5)
    tn.read_until(b"login:")
    tn.write(user.encode('ascii') + b"\n")

    time.sleep(0.5)
    tn.read_until(b"Password:")
    tn.write(password.encode('ascii') + b"\n")
    time.sleep(0.5)

    #Habilita NTLMV2
    tn.write(b"smb client auth 1\n")

    #Desabilita FTP
    tn.write(b"set ftp down\n")

    #Desabilita SSH
    tn.write(b"set ssh down\n")

    #Desabilita WSD
    tn.write(b"set wsprn down\n")

    #Configura NTP
    tn.write(b"sntp server \"a.st1.ntp.br\" \n")

    # Salva e fecha.
    tn.write(b"logout\n")
    time.sleep(0.5)

    tn.write(b"yes\n")

    print(f"A impressora {host} foi configurada!\n")

    

    ##DEBUG##
    #print(tn.read_all().decode('ascii'))




# Execução

with open("lista_exemplo.txt","r") as lista:
    for hostnl in lista:
        host = hostnl.rstrip()
        try:
            configura_telnet(host)
        except:
            with open('telnet_erro.txt', 'a') as f:
                f.write(hostnl)
            print("Ocorreu algum erro!\n")
