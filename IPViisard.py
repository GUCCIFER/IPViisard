from tkinter import *


def ipToBin(ip):
    ipBin = ""
    for part in ip.split("."):                      # splitib antud ip ära "." kohast muudab antud arvu
        ipBin += "{0:08b}".format(int(part)) + "."  # kaheksakohaliseks binaararvuks ning lisab selle ipBin-i otsa
    return ipBin[:-1]  # tagastab binaarse ip ning eemaldab lõpust punkti


# Wildcardi ja Netmaski jaoks funktsioon
def netmaskToBin(netmask, number1, number2):
    netmaskBin = ""
    i = 0
    while i < 32:  # ip aadress on binaarselt 32 kohaline
        if i % 8 == 0 and i != 0:  # 8 kaupa paneb punkti vahele
            netmaskBin += "."
        if i < int(netmask): # lisab nii kaua ühtesi või nulle kui vaja
            netmaskBin += str(number1)
        else:
            netmaskBin += str(number2)
        i += 1
    return netmaskBin

# Binaarse ip teeb kümnendsüsteemi
def binToIP(bin):
    ipBin = ""
    for part in bin.split("."):             # Splitib ära "." pealt ning muudab binaarsed arvud kümnendsüsteemi
        ipBin += str(int(part, 2)) + "."
    return ipBin[:-1] # kaotab viimase punkti ära

# Network
def network(ip, netmask):
    array = ipToBin(ip).split(".")
    binary = ''.join(array)
    num = 32 - int(netmask)
    zeroes = '0' * num
    binary = binary[:int(netmask)] # võtab netmaski suuruse osa
    binary += zeroes # lisab nullid lõppu
    return '{}.{}.{}.{}'.format(binary[:8], binary[8:16], binary[16:24], binary[24:])

# Broadcasti aadress
def broadcast(ip, netmask):
    array = ipToBin(ip).split(".")
    binary = ''.join(array)
    num = 32 - int(netmask)
    ones = '1' * num
    binary = binary[:int(netmask)]
    binary += ones
    return '{}.{}.{}.{}'.format(binary[:8], binary[8:16], binary[16:24], binary[24:])

# väikseim aadress networkis
def hostMIN(ip, netmask):
    address = network(ip, netmask)
    return address[:-1] + "1"

# suurim aadress networkis
def hostMAX(ip, netmask):
    address = broadcast(ip, netmask)
    return address[:-1] + "0"


def displayAll(ipAddr, netmask):
    infoArr = []
    bar1 = "#" * 40
    info = "IP: {} Netmask: {}".format(ipAddr, netmask)
    bar2 = "#" * 40

    ip = 'IP: {} {}'.format(ipAddr, ipToBin(ipAddr))

    nm = 'Netmask: {} {}'.format(binToIP(netmaskToBin(netmask, 1, 0)), netmaskToBin(netmask, 1, 0))

    wc = 'Wildcard: {} {}'.format(binToIP(netmaskToBin(netmask, 0, 1)), netmaskToBin(netmask, 0, 1))

    nw = 'Network: {} {}'.format(binToIP(network(ipAddr, netmask)), network(ipAddr, netmask))

    bc = 'Broadcast: {} {}'.format(binToIP(broadcast(ipAddr, netmask)), broadcast(ipAddr, netmask))

    hostmin = 'HostMIN: {} {}'.format(binToIP(hostMIN(ipAddr, netmask)), hostMIN(ipAddr, netmask))

    hostmax = 'HostMAX: {} {}'.format(binToIP(hostMAX(ipAddr, netmask)), hostMAX(ipAddr, netmask))

    infoArr.extend([bar1, info, bar2, ip, nm, wc, nw, bc, hostmin, hostmax])

    return infoArr


# print("IP aadress binaarses vormis: " + ipToBin(ipAddr))


# displayAll("192.168.2.1","24").get()

# #################TKINTER############################
window = Tk(screenName=None, baseName=None, className='Tk', useTk=1)
window.title("IP viisard")
window.geometry("600x500+10+20")

ipEntry = Entry()
ipEntry.place(x=80, y=380)
ipEntry.insert(END, "192.168.2.1")
ipLabel = Label(text="IPv4 Address")
ipLabel.place(x=80, y=350)

netmaskEntry = Entry(width=5)
netmaskEntry.place(x=220, y=380)
netmaskEntry.insert(END, "24")
netmaskLabel = Label(text="Netmask")
netmaskLabel.place(x=220, y=350)

outputtext = Text()
outputtext.config(width=60, height=20)
outputtext.place(x=20, y=20)


def display(array):
    outputtext.delete('1.0', END)
    outputtext.config(state=NORMAL)
    for word in array:
        outputtext.insert(END, word + "\n")
    outputtext.config(state=DISABLED)


calculateButton = Button(window, text="Calculate",
                         command=lambda: display(displayAll(ipEntry.get(), netmaskEntry.get())))
calculateButton.place(x=80, y=410)

window.mainloop()
