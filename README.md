# Subnet Calculator
Il Programma, inserito in input un indirizzo IP, restituisce in output: **Nome di Rete** e **Indirizzo di Broadcast**.
Questa versione è stata realizzata con linguaggio di programmazione **Python 3**. 

## Esempio Grafico

![Graphic](https://cdn.discordapp.com/attachments/802486048088391720/803273440857030677/unknown.png)

### Avvertenza
***
Per rendere maggiormente chiaro le seguenti parti di codice sono state rimosse alcune righe contenenti commenti, utili solo all'interno del programma stesso.

## Blocchi di Codice
#### Conversione Binaria dell'indirizzo IP
~~~python
90	ip = input("Inserire IP --> ")

93	ip = ip.split(".")
94	list(ip)

97	print("IP Binary --> ", ipBinary(ip))
~~~
Il codice sopra riportato si occupa di prendere in input un indirizzo IP e di suddividerlo.
Ottenuta in input una stringa 
~~~
'87.250.78.5'
~~~
Essa viene suddivisa in corrispondenza del carattere "."
~~~
['87', '250', '78', '5']
~~~
Viene così a crearsi una lista.

#### Funzione ipBinary
Alla riga 97 viene richiamata la funzione seguente
~~~python
1	def  ipBinary(ip):
2		binary = [] 
			
4		fill = "{:>08}"
			
6		for i in  range(4):

8			binary.append(fill.format(bin(int(ip[i]))[2:]))
			
12		dot_ipBin = ".".join(binary)
			
14		return dot_ipBin
~~~    
Questa funzione ha lo scopo di convertire in binario ogni singola parte dell'indirizzo IP, secondo seguente formato
~~~
['01010111', '11111010', '01001110', '00000101']
~~~
Le celle verranno poi riunite utilizzando "." come carattere di separazione
~~~
'01010111.11111010.01001110.00000101'
~~~
La funzione *fill.format* ha lo scopo di completare la conversione in binario del valore prima inserito aggiungendo in testa quanti 0 necessari per arrivare a 8 bit
***
#### Conversione Binaria della Maschera di Rete
***
~~~python
98	netmask = input("\n\nInserire Maschera di Rete --> ")

101	netmask = netmask.split(".") # Split in a list
102	list(netmask)
  
106	maskBin = maskBinary()

110	print("Subnet Mask --> ", dottedMask(maskBin))
~~~
Il codice sopra riportato, si occupa di prendere in input una Maschera di Rete e, anche in questo caso, di suddividerla.
Ottenuta in input una stringa 
~~~
'255.255.240.0'
~~~
Essa viene suddivisa in corrispondenza del carattere "."
~~~
['255', '255', '240', '0']
~~~
Viene così a crearsi una lista.

#### Funzione maskBinary
Alla riga 106 viene richiamata la seguente funzione il cui scopo è quello di convertire la maschera di rete in binario e, come accadeva con l'indirizzo IP, aggiungere in testa il numero necessario di 0 per raggiungere gli 8 bit.
~~~python
17	def  maskBinary():
18		binary =  []
19		
20		for i in netmask:
21			binary.append(bin(int(i))[2:])
22		
23		maskBin =  "".join(binary)
24		
25		fill =  "{:<032}"
26		maskBin = fill.format(maskBin)
27		
28		int(maskBin)
29		
30		return maskBin
~~~
Questa funzione ritornerà una stringa composta da tutti i risultati binari uniti insieme.
A differenza dell'indirizzo IP, in questa funzione gli 0 vengono aggiunti in coda per raggiungere 32 bit e quindi completare la Subnet Mask.
~~~
'11111111111111111111000000000000'
~~~
#### Funzione dottedMask
L'unico scopo della funzione che segue è quello di unire la Maschera di Rete, in 4 byte separati dal segno ".".
~~~python
42	def  dottedMask(mk):
43		dot_maskBin =  list(mk)
44
45		reduce(dot_maskBin)
46
47		dot_maskBin =  ".".join(dot_maskBin)
48
49		return dot_maskBin
~~~
Si può notare che nella precedente funzione ne venga richiamata una ulteriore chiamata *"reduce"*

#### Funzione Reduce
Questa funzione verrà richiamata diverse altre volte nel corso del programma
~~~python
33	def  reduce(ls):
34		ls[0:8]  =  ["".join(ls[0:8])]
35		ls[1:9]  =  ["".join(ls[1:9])]
36		ls[2:10]  =  ["".join(ls[2:10])]
37		ls[3:11]  =  ["".join(ls[3:11])
38		
39		return ls
~~~
Segue il procedimento grafico, passo per passo, di ciò che avviene nel blocco di codice precedente.
Prima della riga 34 ci troviamo in questa situazione:
~~~
['1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0']
~~~
~~~
['11111111', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0']
~~~
~~~
['11111111', '11111111', '1', '1', '1', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0']
~~~
~~~
['11111111', '11111111', '11110000', '0', '0', '0', '0', '0', '0', '0', '0']
~~~
~~~
['11111111', '11111111', '11110000', '00000000']
~~~
***
#### Calcolo del CIDR
***
~~~python
114	print("\nCIDR --> ",  cidr(maskBin))
~~~
Tramite questa unica riga di codice richiamo la funzione seguente

#### Funzione cidr
Questa funzione ha lo scopo di calcolare il CIDR contando il numero di "1" presenti nella Subnet Mask
~~~python
52	def cidr(mk):
53		count =  0
54		
55		for digit in mk:
56			if digit ==  "1":
57				count +=  1
58		
59		return count
~~~
***
#### Calcolo del Nome di Rete (Binario e Decimale)
***
~~~python
118	nameBin, netName =  network(ip, netmask)
~~~
Vengono salvati in due variabili i valori ritornati sotto forma di Tupla dalla funzione seguente
#### Funzione network
~~~python
62	def  network(ip, netmask):
63		nameBin =  []
64		netName =  []
65		fill =  "{:>08}"		  
66
67		for i in  range(4):
68			bitwise =  int(ip[i])  &  int(netmask[i])
69
70			netName.append(bitwise)
71			nameBin.append(fill.format(bin(bitwise)[2:]))
72
73		nameBin =  "".join(nameBin)
74		
75		return nameBin, netName
~~~
Nel costrutto
~~~python
67	for i in  range(4):
68		bitwise =  int(ip[i])  &  int(netmask[i])
~~~
Eseguo un'operazione di AND in bitwise, *"&"*, tra la cella in posizione *i* dell' IP e della Subnet Mask.
~~~
['87', '250', '78', '5']
   &	 &		&	  &
['255', '255', '240', '0']
~~~
L'operazione, effettuata su valori binari, restituirà una lista di valori in base 10.
~~~
['87', '250', '64', '0']
~~~
Successivamente converto in binario ogni singolo elemento della lista.
Ritorno quindi una Tupla composta da due variabili che si presenterà sotto il seguente formato
~~~
('01010111111110100100000000000000', [87, 250, 64, 0])
~~~
Usciamo quindi dalla funzione e torniamo al codice.
Formatto poi le due variabili in modo da adattarle alla stampa
~~~python
122	dot_netName =  [str(num)  for num in netName]
123	dot_netName =  ".".join(dot_netName)
124
125	print("\n\nNetwork Name --> ", dot_netName)

129	dot_nameBin =  list(nameBin)
130
131	reduce(dot_nameBin)
132
133	dot_nameBin =  ".".join(dot_nameBin)
134	print("Network Name Binary --> "  + dot_nameBin)
~~~
Da riga 122 a riga 125
~~~python
122	dot_netName =  [str(num)  for num in netName]
123	dot_netName =  ".".join(dot_netName)
124
125	print("\n\nNetwork Name --> ", dot_netName)
~~~
Formatto l'output correggendo alcuni errori di stampa dovuti all'utilizzo di numeri interi. Segue, più avanti nel file, una spiegazione più dettagliata dell'errore e della soluzione adottata

Da riga 129 a riga 134
~~~python
129	dot_nameBin = list(nameBin)
130
131	reduce(dot_nameBin)
132
133	dot_nameBin = ".".join(dot_nameBin)
134	print("Network Name Binary --> "  + dot_nameBin)
~~~
Come avveniva nel caso precedente per la Maschera di Rete, formatto l'output aggiungendo il carattere "." come forma di separazione tra le celle della lista *dot_nameBin*

[Spiegazione Dettagliata](#funzione-dottedmask)

L'output sarà quindi il seguente:

Nome di Rete
~~~
87.250.64.0
~~~
Nome di Rete Binario
~~~
01010111.11111010.01000000.00000000
~~~

***
#### Calcolo dell'Indirizzo di Broadcast (Binario e Decimale)
***
~~~python
139	subSplit =  []
140
141	for digit in maskBin:
142		subSplit.append(digit)
143
144	nameSplit =  []
145
146	for digit in nameBin:
147		nameSplit.append(digit)
~~~
Nel blocco di codice precedente suddivido, bit a bit, la maschera di rete ed il nome di rete.
Facendo così otterrò, secondo il formato seguente due liste distinte dove ogni cella è costituita da un singolo bit.
~~~
['1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0']
~~~
~~~
['0', '1', '0', '1', '0', '1', '1', '1', '1', '1', '1', '1', '1', '0', '1', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0']
~~~
Segue il codice il cui scopo è quello di calcolare la Maschera di Rete.
Analizzeremo nel dettaglio alcuni pezzi del codice.
~~~python
150	broadcast =  []
151
152	for i in  range(32):
153		broadcast.append(str(NOR(subSplit[i], nameSplit[i])))
154		broadcast[i]  =  str(int(broadcast[i])  |  int(nameSplit[i]))

158	dot_broadcastBin = broadcast
159
160	reduce(dot_broadcastBin)
161
162	dot_broadcastBin =  ".".join(dot_broadcastBin)

165	for i in  range(4):
166		broadcast[i]  =  int(broadcast[i],  2)  

170	dot_broadcast =  [str(num)  for num in broadcast]
171	dot_broadcast =  ".".join(dot_broadcast)
172
173	print("\n\nBroadcast Address --> ", dot_broadcast)
174	print("Broadcast Binary --> ", dot_broadcastBin)
~~~
Nella prima parte di codice, da riga 150 a riga 154
~~~python
150	broadcast =  []
151
152	for i in  range(32):
153		broadcast.append(str(NOR(subSplit[i], nameSplit[i])))
154		broadcast[i]  =  str(int(broadcast[i])  |  int(nameSplit[i]))
~~~
Per calcolare l'indirizzo di Broadcast ho optato per utilizzare l'operatore logico NOR tra la Maschera di Rete ed il Nome di Rete in modo da porre a 1 tutti i bit dedicati agli host e lasciare a 0 tutti quelli restanti secondo quanto segue
~~~
01010111.11111010.0100 0000.00000000
NOR
11111111.11111111.1111 0000.00000000
~~~
#### Funzione NOR
~~~python
def  NOR(a, b):
	if  (a ==  "0")  and  (b ==  "0"):
		return  1
	else:
		return  0
~~~
Notare come la funzione operi sui singoli bit restituendo il valore 1 solo quando entrambe i bit sono posti a "0"
Il risultato dell'operazione sarà il seguente:
~~~
01010111.11111010.0100 0000.00000000
NOR
11111111.11111111.1111 0000.00000000

00000000.00000000.0000 1111.11111111
~~~
Numero che corrisponde alla Wildcard

Per terminare il calcolo dell'Indirizzo di Broadcast è quindi necessario "unire" la Wildcard con il Nome della Rete, operazione eseguita alla riga 154.
~~~python
154	broadcast[i]  =  str(int(broadcast[i])  |  int(nameSplit[i]))
~~~
Per fare ciò viene utilizzato l'operatore logico OR (|) che opera nel modo che segue:
~~~
01010111.11111010.0100 0000.00000000
OR
00000000.00000000.0000 1111.11111111

01010111.11111010.0100 1111.11111111
~~~
Otteniamo così l'Indirizzo di Broadcast 

Nelle seguenti righe, come già avvenuto in precedenza, formatto l'output aggiungendo il carattere "." come forma di separazione tra le celle della lista *dot_broadcastBin*.
~~~python
158	dot_broadcastBin = broadcast
159
160	reduce(dot_broadcastBin)
161
162	dot_broadcastBin =  ".".join(dot_broadcastBin)
~~~
[Spiegazione Dettagliata](#funzione-dottedmask)

L'indirizzo di Broadcast precedentemente ottenuto risulta ancora essere in formato binario, come mostrato poco sopra.
Nelle righe 165 e 166
~~~python
165	for i in  range(4):
166		broadcast[i]  =  int(broadcast[i],  2)
~~~
Converto da Binario a Decimale ogni blocco della lista *broadcast*
Segue una rappresentazione di ciò che avviene
~~~
Prima --> 01010111.11111010.0100 1111.11111111
Dopo --> ['87', '250', '64', '255']
~~~
Formattando poi l'output nelle righe seguenti questo sarà il risultato
~~~
87.250.64.255
~~~
Il programma termina qui la sua esecuzione

***
#### Interfaccia Grafica

