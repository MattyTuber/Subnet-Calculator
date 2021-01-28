import tkinter as tk
import webbrowser
from tkinter import PhotoImage


def reduce(ls):
    ls[0:8] = ["".join(ls[0:8])]
    ls[1:9] = ["".join(ls[1:9])]
    ls[2:10] = ["".join(ls[2:10])]
    ls[3:11] = ["".join(ls[3:11])]

    return ls


def checkIp(input):
    cont = 0
    mex = "INSERT VALID IP"
    for i in input:
        cont = cont + 1
        if not 0 <= int(i) <= 255:
            input_IP.delete(0, 1000)
            input_IP.insert(0, mex)

    if cont != 4:
        input_IP.delete(0, 1000)
        input_IP.insert(0, mex)


def checkMask(input, bin):
    cont = 0
    mex = "INSERT VALID SUBNET MASK"
    for i in input:
        cont = cont + 1
        if not 0 <= int(i) <= 255:
            input_MASK.delete(0, 1000)
            input_MASK.insert(0, mex)

    if cont != 4:
        input_MASK.delete(0, 1000)
        input_MASK.insert(0, mex)

    isZero = False

    for bit in bin:
        if bit == "0":
            isZero = True
        else:
            if isZero == True:
                input_MASK.delete(0, 1000)
                input_MASK.insert(0, mex)


def NOR(a, b):
    if (a == "0") and (b == "0"):
        return 1
    else:
        return 0


def ShowOutput():

    # INPUT
    ip = input_IP.get()
    netmask = input_MASK.get()

    # CALCOLO IP
    # Split IP into picies
    ip = ip.split(".")  # Split in a list
    list(ip)
    checkIp(ip)

    # Binary Conversion
    binary = []

    fill = "{:>08}"

    for i in range(4):
        # Converts to Binary and Removes 0b from the start
        binary.append(
            fill.format(bin(int(ip[i]))[2:])
        )  # Add 0 at the start to fill the number

    ipBin = "".join(binary)
    int(ipBin)

    dot_ipBin = ".".join(binary)

    # Split Netmask into picies
    netmask = netmask.split(".")  # Split in a list
    list(netmask)

    binary = []

    for i in netmask:
        binary.append(bin(int(i))[2:])

    maskBin = "".join(binary)

    fill = "{:<032}"
    maskBin = fill.format(maskBin)  # Add trailing 0 to fill the number with 32 digits

    int(maskBin)

    checkMask(netmask, maskBin)

    dot_maskBin = list(maskBin)

    reduce(dot_maskBin)

    dot_maskBin = ".".join(dot_maskBin)

    # CALCOLO CIDR

    count = 0
    for digit in maskBin:
        if digit == "1":
            count += 1

    # CALCOLO NOME RETE

    netName = []
    nameBin = []
    fill = "{:>08}"

    for i in range(4):
        bitwise = int(ip[i]) & int(netmask[i])

        netName.append(bitwise)
        nameBin.append(fill.format(bin(bitwise)[2:]))

    nameBin = "".join(nameBin)

    # DOTTED NETWORK NAME

    dot_netName = [str(num) for num in netName]
    dot_netName = ".".join(dot_netName)

    # DOTTED BINARY NETWORK NAME

    dot_nameBin = list(nameBin)

    reduce(dot_nameBin)

    dot_nameBin = ".".join(dot_nameBin)

    # CALCOLO INDIRIZZO BROADCAST

    # Split binaries in digits
    subSplit = []

    for digit in maskBin:
        subSplit.append(digit)

    nameSplit = []

    for digit in nameBin:
        nameSplit.append(digit)

    # Calculates the Broadcast Address
    broadcast = []

    for i in range(32):
        broadcast.append(str(NOR(subSplit[i], nameSplit[i])))
        broadcast[i] = str(int(broadcast[i]) | int(nameSplit[i]))

    # DOTTED BROADCAST BIN

    dot_broadcastBin = broadcast

    reduce(dot_broadcastBin)

    dot_broadcastBin = ".".join(dot_broadcastBin)

    # To BASE 10 Conversion
    for i in range(4):
        broadcast[i] = int(broadcast[i], 2)

    # DOTTED BROADCAST

    dot_broadcast = [str(num) for num in broadcast]
    dot_broadcast = ".".join(dot_broadcast)

    # OUTPUT

    Output_BINARYIP = tk.Entry(width=38)
    Output_BINARYIP.insert(0, dot_ipBin)
    Output_BINARYIP.grid(row=3, column=0, padx=7, pady=5, sticky="E")

    Output_BINARYMASK = tk.Entry(width=38)
    Output_BINARYMASK.insert(0, dot_maskBin)
    Output_BINARYMASK.grid(row=4, column=0, padx=7, pady=5, sticky="E")

    Output_CIDR = tk.Entry(width=38)
    Output_CIDR.insert(0, count)
    Output_CIDR.grid(row=5, column=0, padx=7, pady=5, sticky="E")

    Output_Network = tk.Entry(width=38)
    Output_Network.insert(0, dot_netName)
    Output_Network.grid(row=6, column=0, padx=7, pady=5, sticky="E")

    Output_NetworkBinary = tk.Entry(width=38)
    Output_NetworkBinary.insert(0, dot_nameBin)
    Output_NetworkBinary.grid(row=7, column=0, padx=7, pady=5, sticky="E")

    Output_Brodcast = tk.Entry(width=38)
    Output_Brodcast.insert(0, dot_broadcast)
    Output_Brodcast.grid(row=8, column=0, padx=7, pady=5, sticky="E")

    Output_BrodcastBinary = tk.Entry(width=38)
    Output_BrodcastBinary.insert(0, dot_broadcastBin)
    Output_BrodcastBinary.grid(row=9, column=0, padx=7, pady=5, sticky="E")


# INIZIO PARTE GRAFICA!!!!

window = tk.Tk()
window.geometry("585x467")
window.title("Subnet Calculator")
window.grid_columnconfigure(0, weight=1)
window.resizable(False, False)
window.configure(background="#0C090A")
window.iconbitmap(r"Ico/fauser.ico")

fb = PhotoImage(file="Ico/facebook.png")
ig = PhotoImage(file="Ico/ig.png")

IP = tk.Label(
    window,
    text="IP Address: ",
    font=("Abadi", 12),
    background="#0C090A",
    foreground="white",
)
IP.grid(row=0, column=0, padx=7, sticky="W")

input_IP = tk.Entry(width=38)
input_IP.grid(row=0, column=0, padx=7, pady=5, sticky="E")

MASK = tk.Label(
    window,
    text="Subnet Mask: ",
    font=("Abadi", 12),
    background="#0C090A",
    foreground="white",
)
MASK.grid(row=1, column=0, padx=7, sticky="W")

input_MASK = tk.Entry(width=38)
input_MASK.grid(row=1, column=0, padx=7, pady=5, sticky="E")

calcola = tk.Button(
    window,
    text="------------------------------------------------COMPUTE!------------------------------------------------",
    font=("Abadi Bold", 10),
    command=ShowOutput,
)
calcola.grid(row=2, column=0, pady=20, padx=7, sticky="WE")


BINARYIP = tk.Label(
    window,
    text="IP Binary: ",
    font=("Abadi", 12),
    background="#0C090A",
    foreground="white",
)
BINARYIP.grid(row=3, column=0, padx=7, pady=1, sticky="W")


BINARYMASK = tk.Label(
    window,
    text="Subnet Mask: ",
    font=("Abadi", 12),
    background="#0C090A",
    foreground="white",
)
BINARYMASK.grid(row=4, column=0, padx=7, pady=1, sticky="W")


CIDR = tk.Label(
    window, text="CIDR: ", font=("Abadi", 12), background="#0C090A", foreground="white"
)
CIDR.grid(row=5, column=0, padx=7, pady=1, sticky="W")

NetworkName = tk.Label(
    window,
    text="Network Name: ",
    font=("Abadi", 12),
    background="#0C090A",
    foreground="white",
)
NetworkName.grid(row=6, column=0, padx=7, pady=1, sticky="W")

NetworkNameBinary = tk.Label(
    window,
    text="Network Name Binary: ",
    font=("Abadi", 12),
    background="#0C090A",
    foreground="white",
)
NetworkNameBinary.grid(row=7, column=0, padx=7, pady=1, sticky="W")

Brodcast = tk.Label(
    window,
    text="Broadcast Adress: ",
    font=("Abadi", 12),
    background="#0C090A",
    foreground="white",
)
Brodcast.grid(row=8, column=0, padx=7, pady=1, sticky="W")

BrodcastBinary = tk.Label(
    window,
    text="Broadcast Binary: ",
    font=("Abadi", 12),
    background="#0C090A",
    foreground="white",
)
BrodcastBinary.grid(row=9, column=0, padx=7, pady=1, sticky="W")

credists_Label = tk.Label(
    window,
    text="\nProgrammer: Broglio Matteo \nGraphic Desing: Sean Galuzzi Colombo Alessio \nTechnical Documentation: Garripoli Fabio Roberto Lucca Davide",
    font=("Abadi BOLD", 7),
    background="#0C090A",
    foreground="white",
)
credists_Label.grid(row=10, column=0, sticky="S", pady=10)

credists_Label = tk.Label(
    window,
    text="\nCOPYRIGHT© 2077 ITT FAUSER. ALL RIGHTS RESERVED",
    font=("Abadi BOLD", 7),
    background="#0C090A",
    foreground="white",
)
credists_Label.grid(row=12, column=0, sticky="N")


def Open_ig():
    webbrowser.open("https://www.instagram.com/itt_fauser/")


def Open_fb():
    webbrowser.open("https://www.facebook.com/ittfauser")


def help():
    webbrowser.open("https://github.com/MattyTuber/Subnet-Calculator.git")


Help = tk.Button(
    window,
    text="--->HELP<---",
    background="#0C090A",
    foreground="light blue",
    command=help,
)
Help.grid(row=11, column=0, sticky="S", padx=10)

instagram = tk.Button(window, image=ig, background="#0C090A", command=Open_ig)
instagram.grid(row=12, column=0, sticky="SE")

facebook = tk.Button(window, image=fb, background="#0C090A", command=Open_fb)
facebook.grid(row=12, column=0, sticky="SW")

window.mainloop()
