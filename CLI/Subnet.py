# Controllo validità Indirizzo IP
def checkIp(input):
    cont = 0
    for i in input:
        cont = cont + 1
        if not 0 <= int(i) <= 255:
            print("Inserire IP compreso tra 0 e 255!!")
            exit()

    if cont != 4:
        print("Inserire IP composto da 4 Byte!!")
        exit()


# Controllo Validità Subnet mask
def checkMask(input, bin):
    cont = 0
    for i in input:
        cont = cont + 1
        if not 0 <= int(i) <= 255:
            print("Inserire Subnet Mask compresa tra 0 e 255!!")
            exit()

    if cont != 4:
        print("Inserire IP composto da 4 Byte!!")
        exit()

    # Controllo Subnet Mask Valida
    isZero = False

    for bit in bin:
        if bit == "0":
            isZero = True
        else:
            if isZero == True:
                print("Inserire Valore Subnet Mask Valido!!")
                exit()


def ipBinary(ip):
    binary = []

    fill = "{:>08}"

    for i in range(4):
        # Converts to Binary and Removes 0b from the start
        binary.append(
            fill.format(bin(int(ip[i]))[2:])
        )  # Add 0 at the start to fill the number

    dot_ipBin = ".".join(binary)

    return dot_ipBin


def maskBinary():
    binary = []

    for i in netmask:
        binary.append(bin(int(i))[2:])

    maskBin = "".join(binary)

    fill = "{:<032}"
    maskBin = fill.format(maskBin)  # Add trailing 0 to fill the number with 32 digits

    int(maskBin)

    return maskBin


def reduce(ls):
    ls[0:8] = ["".join(ls[0:8])]
    ls[1:9] = ["".join(ls[1:9])]
    ls[2:10] = ["".join(ls[2:10])]
    ls[3:11] = ["".join(ls[3:11])]

    return ls


def dottedMask(mk):
    dot_maskBin = list(mk)

    reduce(dot_maskBin)

    dot_maskBin = ".".join(dot_maskBin)

    return dot_maskBin


def cidr(mk):
    count = 0

    for digit in mk:
        if digit == "1":
            count += 1

    return count


def network(ip, netmask):
    nameBin = []
    netName = []
    fill = "{:>08}"

    for i in range(4):
        bitwise = int(ip[i]) & int(netmask[i])

        netName.append(bitwise)
        nameBin.append(fill.format(bin(bitwise)[2:]))

    nameBin = "".join(nameBin)

    return nameBin, netName


def NOR(a, b):
    if (a == "0") and (b == "0"):  # Checks string instead of integers
        return 1
    else:
        return 0


# CALCOLO IP

ip = input("Inserire IP --> ")

# Split IP into picies
ip = ip.split(".")  # Split in a list
list(ip)
checkIp(ip)

# Binary Conversion
print("IP Binary --> ", ipBinary(ip))

# CALCOLO SUBNET MASK

netmask = input("\n\nInserire Maschera di Rete --> ")

# Split Netmask into picies
netmask = netmask.split(".")  # Split in a list
list(netmask)

# Binary Conversion

maskBin = maskBinary()

# DOTTED SUBNET MASK

checkMask(netmask, maskBin)

print("Subnet Mask --> ", dottedMask(maskBin))

# CALCOLO CIDR

print("\nCIDR --> ", cidr(maskBin))

# CALCOLO NOME RETE

nameBin, netName = network(ip, netmask)

# DOTTED NETWORK NAME

dot_netName = [str(num) for num in netName]
dot_netName = ".".join(dot_netName)

print("\n\nNetwork Name --> ", dot_netName)

# DOTTED BINARY NETWORK NAME

dot_nameBin = list(nameBin)

reduce(dot_nameBin)

dot_nameBin = ".".join(dot_nameBin)
print("Network Name Binary --> " + dot_nameBin)

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

print("\n\nBroadcast Address --> ", dot_broadcast)
print("Broadcast Binary --> ", dot_broadcastBin)
