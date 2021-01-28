# Subnet Calculator
Il Programma, inserito in input un indirizzo IP, restituisce in output: **Nome di Rete** e **Indirizzo di Broadcast**.
Questa versione è stata realizzata con linguaggio di programmazione **Python 3**. 

## Menu

 1. [Esempio CLI](#esempio-cli)
 2. [Avvertenza](#avvertenza)
 3. [Spiegazione del Codice](#funzionamento-codice)
	 - [Conversione Binaria IP](#conversione-binaria-dellindirizzo-ip)
		 - [Funzione ipBinary](#funzione-ipbinary)
	- [Conversione Binaria Maschera di Rete](#conversione-binaria-della-maschera-di-rete)
		- [Funzione maskBinary](#funzione-maskbinary)
		- [Funzione dottedMask](#funzione-dottedmask)
	- [Funzione Reduce](#funzione-reduce)
	- [Calcolo CIDR](#calcolo-del-cidr)
		- [Funzione CIDR](#funzione-cidr)
	- [Calcolo Nome di Rete](#calcolo-del-nome-di-rete-binario-e-decimale)
		- [Funzione Network](#funzione-network)
	- [Calcolo Indirizzo di Broadcast](#calcolo-dellindirizzo-di-broadcast-binario-e-decimale)
		- [Funzione NOR](#funzione-nor)
 4. [Controllo Errori](#controllo-errori)
 5. [Esempio GUI](#esempio-gui)

## Esempio CLI

![Graphic](https://cdn.discordapp.com/attachments/802486048088391720/803273440857030677/unknown.png)

### Avvertenza
***
Per rendere maggiormente chiaro le seguenti parti di codice sono state rimosse alcune righe contenenti commenti, utili solo all'interno del programma stesso.

## Funzionamento Codice
#### Conversione Binaria dell'indirizzo IP
~~~python
126	ip = input("Inserire IP --> ")

129	ip = ip.split(".")
130	list(ip)

134	print("IP Binary --> ", ipBinary(ip))
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
Alla riga 134 viene richiamata la funzione seguente
~~~python
40	def  ipBinary(ip):
41		binary = [] 
42		
43		fill = "{:>08}"
44
45		for i in  range(4):
46
47			binary.append(fill.format(bin(int(ip[i]))[2:]))
			
51		dot_ipBin = ".".join(binary)
52			
53		return dot_ipBin
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
138	netmask = input("\n\nInserire Maschera di Rete --> ")

141	netmask = netmask.split(".") # Split in a list
142	list(netmask)
  
146	maskBin = maskBinary()

150	checkMask(netmask, maskBin)
151
152	print("Subnet Mask --> ", dottedMask(maskBin))
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
Alla riga 146 viene richiamata la seguente funzione il cui scopo è quello di convertire la maschera di rete in binario e, come accadeva con l'indirizzo IP, aggiungere in testa il numero necessario di 0 per raggiungere gli 8 bit.
~~~python
56	def  maskBinary():
57		binary =  []
58		
59		for i in netmask:
60			binary.append(bin(int(i))[2:])
61		
62		maskBin =  "".join(binary)
63		
64		fill =  "{:<032}"
65		maskBin = fill.format(maskBin)
66		
67		int(maskBin)
68		
69		return maskBin
~~~
Questa funzione ritornerà una stringa composta da tutti i risultati binari uniti insieme.
A differenza dell'indirizzo IP, in questa funzione gli 0 vengono aggiunti in coda per raggiungere 32 bit e quindi completare la Subnet Mask.
~~~
'11111111111111111111000000000000'
~~~
#### Funzione dottedMask
L'unico scopo della funzione che segue è quello di unire la Maschera di Rete, in 4 byte separati dal segno ".".
~~~python
81	def  dottedMask(mk):
82		dot_maskBin =  list(mk)
83
84		reduce(dot_maskBin)
85
86		dot_maskBin =  ".".join(dot_maskBin)
87
88		return dot_maskBin
~~~
Si può notare che nella precedente funzione ne venga richiamata una ulteriore chiamata *"reduce"*

#### Funzione Reduce
Questa funzione verrà richiamata diverse altre volte nel corso del programma
~~~python
72	def  reduce(ls):
73		ls[0:8]  =  ["".join(ls[0:8])]
74		ls[1:9]  =  ["".join(ls[1:9])]
75		ls[2:10]  =  ["".join(ls[2:10])]
76		ls[3:11]  =  ["".join(ls[3:11])
77		
78		return ls
~~~
Segue il procedimento grafico, passo per passo, di ciò che avviene nel blocco di codice precedente.
Prima della riga 85 ci troviamo in questa situazione:
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
152	print("\nCIDR --> ",  cidr(maskBin))
~~~
Tramite questa unica riga di codice richiamo la funzione seguente

#### Funzione cidr
Questa funzione ha lo scopo di calcolare il CIDR contando il numero di "1" presenti nella Subnet Mask
~~~python
91	def cidr(mk):
92		count =  0
93		
94		for digit in mk:
95			if digit ==  "1":
96				count +=  1
97		
98		return count
~~~
***
#### Calcolo del Nome di Rete (Binario e Decimale)
***
~~~python
160	nameBin, netName =  network(ip, netmask)
~~~
Vengono salvati in due variabili i valori ritornati sotto forma di Tupla dalla funzione seguente
#### Funzione network
~~~python
101	def  network(ip, netmask):
102		nameBin =  []
103		netName =  []
104		fill =  "{:>08}"		  
105
106		for i in  range(4):
107			bitwise =  int(ip[i])  &  int(netmask[i])
108
109			netName.append(bitwise)
110			nameBin.append(fill.format(bin(bitwise)[2:]))
111
112		nameBin =  "".join(nameBin)
113		
114		return nameBin, netName
~~~
Nel costrutto
~~~python
106	for i in  range(4):
107		bitwise =  int(ip[i])  &  int(netmask[i])
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
164	dot_netName =  [str(num)  for num in netName]
165	dot_netName =  ".".join(dot_netName)
166
167	print("\n\nNetwork Name --> ", dot_netName)

171	dot_nameBin =  list(nameBin)
172
173	reduce(dot_nameBin)
174
175	dot_nameBin =  ".".join(dot_nameBin)
176	print("Network Name Binary --> "  + dot_nameBin)
~~~
Da riga 164 a riga 167
~~~python
164	dot_netName =  [str(num)  for num in netName]
165	dot_netName =  ".".join(dot_netName)
166
167	print("\n\nNetwork Name --> ", dot_netName)
~~~
Formatto l'output correggendo alcuni errori di stampa dovuti all'utilizzo di numeri interi. Segue, più avanti nel file, una spiegazione più dettagliata dell'errore e della soluzione adottata

Da riga 171 a riga 176
~~~python
171	dot_nameBin = list(nameBin)
172
173	reduce(dot_nameBin)
174
175	dot_nameBin = ".".join(dot_nameBin)
176	print("Network Name Binary --> "  + dot_nameBin)
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
181	subSplit =  []
182
183	for digit in maskBin:
184		subSplit.append(digit)
185
186	nameSplit =  []
187
188	for digit in nameBin:
189		nameSplit.append(digit)
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
192	broadcast =  []
193
194	for i in  range(32):
195		broadcast.append(str(NOR(subSplit[i], nameSplit[i])))
196		broadcast[i]  =  str(int(broadcast[i])  |  int(nameSplit[i]))

200	dot_broadcastBin = broadcast
201
202	reduce(dot_broadcastBin)
203
204	dot_broadcastBin =  ".".join(dot_broadcastBin)

207	for i in  range(4):
208		broadcast[i]  =  int(broadcast[i],  2)  

212	dot_broadcast =  [str(num)  for num in broadcast]
213	dot_broadcast =  ".".join(dot_broadcast)
214
215	print("\n\nBroadcast Address --> ", dot_broadcast)
216	print("Broadcast Binary --> ", dot_broadcastBin)
~~~
Nella prima parte di codice, da riga 192 a riga 196
~~~python
192	broadcast =  []
193
194	for i in  range(32):
195		broadcast.append(str(NOR(subSplit[i], nameSplit[i])))
196		broadcast[i]  =  str(int(broadcast[i])  |  int(nameSplit[i]))
~~~
Per calcolare l'indirizzo di Broadcast ho optato per utilizzare l'operatore logico NOR tra la Maschera di Rete ed il Nome di Rete in modo da porre a 1 tutti i bit dedicati agli host e lasciare a 0 tutti quelli restanti secondo quanto segue
~~~
01010111.11111010.0100 0000.00000000
NOR
11111111.11111111.1111 0000.00000000
~~~
#### Funzione NOR
~~~python
117	def  NOR(a, b):
118		if  (a ==  "0")  and  (b ==  "0"):
119			return  1
120		else:
121			return  0
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

Per terminare il calcolo dell'Indirizzo di Broadcast è quindi necessario "unire" la Wildcard con il Nome della Rete, operazione eseguita alla riga 196.
~~~python
196	broadcast[i]  =  str(int(broadcast[i])  |  int(nameSplit[i]))
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
200	dot_broadcastBin = broadcast
201
202	reduce(dot_broadcastBin)
203
204	dot_broadcastBin =  ".".join(dot_broadcastBin)
~~~
[Spiegazione Dettagliata](#funzione-dottedmask)

L'indirizzo di Broadcast precedentemente ottenuto risulta ancora essere in formato binario, come mostrato poco sopra.
Nelle righe 207 e 208
~~~python
207	for i in  range(4):
208		broadcast[i]  =  int(broadcast[i],  2)
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

## Controllo Errori
#### Controllo Indirizzo IP
~~~python
2	def  checkIp(input):
3		cont =  0
4		for i in  input:
5			cont = cont +  1
6			if not 0 <= int(i) <= 255:
	7			print("Inserire IP compreso tra 0 e 255!!")
	8			exit()
9		
10		if cont !=  4:
11			print("Inserire IP composto da 4 Byte!!")
12			exit()
~~~
#### Controllo Subnet Mask
~~~python
16	def  checkMask(input, bin):
17		cont =  0
18		for i in  input:
19			cont = cont +  1
20			if not 0 <= int(i) <= 255:
21				print("Inserire Subnet Mask compresa tra 0 e 255!!")
22				exit()
23
24		if cont !=  4:
25			print("Inserire IP composto da 4 Byte!!")
26			exit()

29		isZero =  False  
30
31		for bit in  bin:
32			if bit ==  "0":
33				isZero =  True
34			else:
35				if isZero ==  True:
36					print("Inserire Valore Subnet Mask Valido!!")
37					exit()
~~~
Le prime righe dei due blocchi di codice precedenti risultano essere identiche.
Questo è dovuto al fatto che viene effettuato lo stesso controllo sulla validità dell'input.

I controlli effettuati sono i seguenti:

 - Controllo che l'input sia valido in modo tale che il numero non sia maggiore di 255
 - Controllo che l'utente abbia inserito non più ne meno di 4 byte

Nella funzione *checkMask*, a partire da riga 29, controllo che la Subnet Mask inserita è appartentente alla categoria delle possibili Subnet Mask.
Il controllo viene effettuato sulla versione binaria della Maschera di Rete.
Perchè una Subnet Mask sia valida, il primo 0 binario deve essere esclusivamente seguito da altri 0.

Subnet Mask Non Valida
~~~
11101101.01101101.10110000.00000000
~~~
Subnet Mask Valida
~~~
11111111.11111111.11110000.00000000
~~~
## Esempio GUI

![GUI Example](https://cdn.discordapp.com/attachments/802486048088391720/804438459355758622/unknown.png)
