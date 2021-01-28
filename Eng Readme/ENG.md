# Subnet Calculator
The Program, after it has been inserted a IP address, it gives you back: **Network Name** and **Broadcast Address**.
This version of the program has been coded with **Python 3** programming language.

## Menu

 1. [Graphic Example](#graphic-example)
 2. [Warning](#warning)
 3. [Programm Explanation](#programm-explanation)
	 - [IP Address Binary Convertion](#ip-address-binary-convertion)
		 - [ipBinary Function](#ipbinary-function)
	- [Subnet Mask Binary Convertion](#subnet-mask-binary-convertion)
		- [maskBinary function](#maskbinary-function)
		- [dottedMask function](#dottedmask-function)
	- [Reduce function](#reduce-function)
	- [CIDR Calculation](#cidr-calculation)
		- [cidr Function](#cidr-function)
	- [Network Name Calculation](#network-name-calculation-bynary-and-decimal)
		- [network Function ](#network-function)
	- [Broadcast Address Calculation](#broadcast-address-calculation-binary-and-decimal)
		- [NOR Function](#nor-function)
 4. [Errors Control](#errors-control)
 5. [GUI Example](#gui-example)

## Graphic Example

![How the Output of the code is](https://cdn.discordapp.com/attachments/802486048088391720/803273440857030677/unknown.png)

### Warning
To make the following code part clearer we have removed some lines of code with comments, useful only into the program
## Programm Explanation
***IP Address Binary Convertion***
~~~python
126	ip = input("Insert IP --> ")

129	ip = ip.split(".")
130	list(ip)

134	print("IP Binary --> ", ipBinary(ip))
~~~
The previus lines of code are used to take in input a IP adress and split it into lists.
Inserted in Input a string
~~~
'87.250.78.5'
~~~
It'll be split by the "." character
~~~
['87', '250', '78', '5']
~~~
And a list is done.

#### ipBinary Function
At the 134th line we recall the following function:
~~~python
40	def  ipBinary(ip):

41		binary = [] 
			
43		fill = "{:>08}"
			
45		for i in  range(4):

47			binary.append(fill.format(bin(int(ip[i]))[2:]))
			
51		dot_ipBin = ".".join(binary)
			
53		return dot_ipBin
~~~    
This function has the purpose of convert every IP address part into bynary, by the following format
~~~
['01010111', '11111010', '01001110', '00000101']
~~~
Cells we'll be put reunited using "." as the separation character
~~~
'01010111.11111010.01001110.00000101'
~~~
fill.format function has the purpose of completing the binary convertion of every valor previusly inserted in input by adding to the left of the number many 0 required to reach 8 bit
***
#### Subnet Mask Binary Convertion
***
~~~python
138	netmask = input("\n\nInsert Subnet Mask --> ")

141	netmask = netmask.split(".") # Split in a list

142	list(netmask)
  
146 maskBin = maskBinary()
	
150	checkMask(netmask, maskBin)

152 print("Subnet Mask --> ", dottedMask(maskBin))
~~~   
The last lines of code take in input the Subnet Mask and, even in this case, they dived it.
Taken a string in input
~~~
'255.255.240.0'
~~~
It'll be split by the "." character
~~~
['255', '255', '240', '0']
~~~
And a list is done.
#### maskBinary function
At the 146th line it's recalled the following function wich purpose is converting the Subnet Mask and add many 0s necessary to reach 8 bit.
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
This function will return a string with all the results in binary put together.
In this function 0s are placed at the bottom of the line to reach 32 bit and complete the Subnet Mask.
~~~
'11111111111111111111000000000000'
~~~
#### dottedMask function
The only purpose of the following function is combine the Subnet Mask in 4 byte splitted by "." character.
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
We can notice that in the last function we recall another one called *"reduce"*
#### Reduce function
This function will be recalled other times in the programm
~~~python
72	def  reduce(ls):
73		ls[0:8]  =  ["".join(ls[0:8])]
74		ls[1:9]  =  ["".join(ls[1:9])]
75		ls[2:10]  =  ["".join(ls[2:10])]
76		ls[3:11]  =  ["".join(ls[3:11])
77		
78		return ls
~~~
The following lines resemble step by step what happens in the the last lines of code.
Before line 34 we found ourselves in this situation:
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
#### CIDR Calculation
***
~~~python
152	print("\nCIDR --> ",  cidr(maskBin))
~~~
With this line of code we recall the following function
#### cidr Function
This function has the purpose of calculating the CIDR by counting the 1s in the Subnet Mask
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
#### Network Name Calculation (Bynary and Decimal)
***
~~~python
160	nameBin, netName =  network(ip, netmask)
~~~
In 2 variables are saved the valors returned in Tuple form by the following function
#### network Function 
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
In the construct
~~~python
106	for i in  range(4):
107		bitwise =  int(ip[i])  &  int(netmask[i])
~~~
It is performed an AND operation in bitwise,  *"&"*,  by the the IP cell and the Subnet Mask cell in the *i* position. 
~~~
['87', '250', '78', '5']
   &	 &		&	  &
['255', '255', '240', '0']
~~~
The operation, done with binary valors, it will return a list of valor in base 10.
~~~
['87', '250', '64', '0']
~~~
Next it converts in binary a single element of the list.
It returnes than a Tuple composed of 2 variables that will be presented by the following format
~~~
('01010111111110100100000000000000', [87, 250, 64, 0])
~~~
Then we esc from the function and we return to code.
Then we format the variables to adapt them to printing
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
From line 164 to line 167
~~~python
164	dot_netName =  [str(num)  for num in netName]
165	dot_netName =  ".".join(dot_netName)
166
167	print("\n\nNetwork Name --> ", dot_netName)
~~~
It formats the output by correcting the printing errors made by using Integer number. It follows a more detailed explanation of the error and the adopted solution

From line 171 to line 176
~~~python
171	dot_nameBin = list(nameBin)
172
173	reduce(dot_nameBin)
174
175	dot_nameBin = ".".join(dot_nameBin)
176	print("Network Name Binary --> "  + dot_nameBin)
~~~
It formats the output by adding the "." character as form of separation of the *dot_nameBin* list
[Detailed Explanation](#dottedmask-function)

The output will be the following:

Network Name
~~~
87.250.64.0
~~~
Binary Network Name
~~~
01010111.11111010.01000000.00000000
~~~
***
#### Broadcast Address Calculation (Binary and Decimal)
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
In the last lines of code we divide, bit by bit, the Network Mask and the Network Name.
By doing this we'll get, as the following format, two lists where every cells are composed by a single bit.
~~~
['1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0']
~~~
~~~
['0', '1', '0', '1', '0', '1', '1', '1', '1', '1', '1', '1', '1', '0', '1', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0']
~~~
It follows the part of code which purpose is calculating the Network Mask.
We'll analyze in detail some part of code.
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

194	for i in  range(4):
195		broadcast[i]  =  int(broadcast[i],  2)  
196	dot_broadcast =  [str(num)  for num in broadcast]
197	dot_broadcast =  ".".join(dot_broadcast)
198
199	print("\n\nBroadcast Address --> ", dot_broadcast)
200	print("Broadcast Binary --> ", dot_broadcastBin)
~~~
In the first part of the code, from line 192 to line 196
~~~python
192	broadcast =  []
193
194	for i in  range(32):
195		broadcast.append(str(NOR(subSplit[i], nameSplit[i])))
196		broadcast[i]  =  str(int(broadcast[i])  |  int(nameSplit[i]))
~~~
To calculate the Broadcast Address we use the logical operator NOR by the Network Mask and the Network Name to make every host dedicated bit to 1 and leave to 0 all the others bit by the following metod
~~~
01010111.11111010.0100 0000.00000000
NOR
11111111.11111111.1111 0000.00000000
~~~
#### NOR Function
~~~python
def  NOR(a, b):
	if  (a ==  "0")  and  (b ==  "0"):
		return  1
	else:
		return  0
~~~
We can notice that the function operates with the singles bit by giving back the valor 1 only when every bit are 0s.
The following will be the result of the operation:
~~~
01010111.11111010.0100 0000.00000000
NOR
11111111.11111111.1111 0000.00000000

00000000.00000000.0000 1111.11111111
~~~
Number that matches the Wildcard

To end the calculus of the Broadcast Address it is required combine the Wildcard with the Network Name, operation done with in the line 154.
~~~python
154	broadcast[i]  =  str(int(broadcast[i])  |  int(nameSplit[i]))
~~~
To do so it's used the logic operator OR ( | ) that operates in the following metod:
~~~
01010111.11111010.0100 0000.00000000
OR
00000000.00000000.0000 1111.11111111

01010111.11111010.0100 1111.11111111
~~~
We get the Broadcast Address

In the following lines we format the output by adding the "." character as a form of separation of the cells of the *dot_broadcastBin* list.
~~~python
200	dot_broadcastBin = broadcast
201
202	reduce(dot_broadcastBin)
203
204	dot_broadcastBin =  ".".join(dot_broadcastBin)
~~~
[Detailed Explanation](#dottedmask-function)
The Broadcast Address that we have got before still results in Binary format.
In line 207 and in line 208
~~~python
207	for i in  range(4):
208		broadcast[i]  =  int(broadcast[i],  2)
~~~
We convert from Binary to Decimal every block of the *broadcast* list
It follows a rappresentation of what happens
~~~
Prima --> 01010111.11111010.0100 1111.11111111
Dopo --> ['87', '250', '64', '255']
~~~
After we have formatted the output this we'll be the result
~~~
87.250.64.255
~~~
The programm ends here its execution
## Errors Control
#### IP Address Control
~~~python
2	def  checkIp(input):
3		cont =  0
4		for i in  input:
5			cont = cont +  1
6			if not 0 <= int(i) <= 255:
	7			print("Insert an IP between 0 and 255!!")
	8			exit()
9		
10		if cont !=  4:
11			print("Insert an IP made by 4 byte!!")
12			exit()
~~~
#### Subnet Mask Control
~~~python
16	def  checkMask(input, bin):
17		cont =  0
18		for i in  input:
19			cont = cont +  1
20			if not 0 <= int(i) <= 255:
21				print("Insert a Subnet Mask between 0 and 255!!")
22				exit()
23
24		if cont !=  4:
25			print("Insert an IP made by 4 byte!!")
26			exit()

29		isZero =  False  
30
31		for bit in  bin:
32			if bit ==  "0":
33				isZero =  True
34			else:
35				if isZero ==  True:
36					print("Insert a valid Subnet Mask valor!!")
37					exit()
~~~
The first group of lines of the two blocks of code might look identical.
This is because we do the same control of the validity of the Input.

The control taken are the following:

 - The number must'nt be over 255
 - The user must enter 4 byte, no more, no less

In *checkMask* function, starting from line 29, we control that the Subnet Mask is in the category of the possible Subnet Mask.
The control is done with the binary version of the Subnet Mask.
To be valid a Subnet Mask has to have the first binary 0 followed by other 0s.

Not Valid Subnet Mask
~~~
11101101.01101101.10110000.00000000
~~~
Valid Subnet Mask
~~~
11111111.11111111.11110000.00000000
~~~
## GUI Example
![GUI Example](https://cdn.discordapp.com/attachments/802486048088391720/804438459355758622/unknown.png)