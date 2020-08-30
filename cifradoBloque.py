#!usr/bin/python
## -*- coding: utf-8 -*-
#funcion cifrar
def cifrar():
	print("Cifrado")
	# Nombre archivo y ubicacion
	inputFile = str(input("ingrese el archivo a cifrar :\n"))

	# Leer el contenido del archivo original
	try:
		with open(inputFile,"r",encoding="utf-8") as archivo:  #Con este archivo abralo solo como lectura "r" ("rw" ->lectura escritura) y cuardelo en "archivoOriginal"
			contenido = archivo.read()
		#	print(contenido)
		archivo.close()


	except FileNotFoundError:
		print("Archivo no encontrado,\n")
		return
	#ingresa la clave
	inputKey = input("Ingrese la clave para cifrar: \n")
	clave = list(inputKey) #Crea un arreglo serapando cada caracter
	# todo crear doble confirmacion
	i = 0
	# Crear archivo  Criptograma
	with open("criptograma.txt","w") as textFile:
		while i < len(contenido):
			# ciclo para definor el tamaño de la clave
			for j in range(len(clave)):
				if i < len(contenido):
				#	print(contenido[i])
					#convertir  de caracter a binario
					binarioA = ord(contenido[i])
				else:
					#pading
					binarioA = ord("0")
				binarioB = ord(clave[j])
				# operacion XOR
				resultado = binarioA ^ binarioB
				#print(chr(resultado))
				i=i+1
				# imprimir en criptograma
				textFile.write(str(chr(resultado)))
	textFile.close



#funcion descifrrar
def descifrar():
	print ("Descifrado")
	#ingrese el archivo a descifRAR
	inputFile = input("ingrese el archivo a descifrar: \n")
	
	#leer el contenido del archivo
	try:
		with open(inputFile,"r",encoding="utf-8") as fo:
			contenido = fo.read()
		fo.close() 

	except IOError:
		print("archivo no encontrado")
		return
	inputKey = input("Ingrese la calve: \n")
	clave = list(inputKey)

	i=0
	with open("descifrado.txt","w",encoding="utf-8") as textFile:
		while i < len(contenido):
			for j in range(len(clave)):
			
				if i < len(contenido):
					binarioA = ord(contenido[i])
				else:
					binarioA= ord("0")
				binarioB = ord(clave[j])
				#XOR
				resultado = binarioA ^ binarioB
				
				
				i=i+1
				textFile.write(str(chr(resultado)))
	textFile.close()

def comparar():
	print("COMPARADOR")
	inputFile1 = input("ingrese PRIMER archivo a Comparar: \n")
	inputFile2 = input("ingrese SEGUNDO archivo a Comparar: \n")
	try:
		with open(inputFile1,"r",encoding="utf-8") as fo1:
			contenido1 = fo1.read()
		fo1.close() 
		with open(inputFile2,"r",encoding="utf-8") as fo2:
			contenido2 = fo2.read()
		fo2.close()

	except IOError:
		print("archivo no encontrado")
		return
	cont1 = 0
	cont2 = 0
	for i in range(len(contenido1)):
		if contenido1[i] == contenido2[i]:
			cont1 = cont1+1
			#print("OK")
		else:
			cont2 = cont2+1
			print("error: ",contenido1[i]," != ",contenido2[i])
	if cont2 >= 1:
		print("Tiene ",cont2, " Discrepancias")
#Metodo princpal
if __name__ == '__main__':
	print('''
	 ________ .__          .__          __  .__                     ____.      .__                       
	\_   ___ \|  |_________|__| _______/  |_|__|____    ____       |    |____  |__| _____   ____   ______
	/    \  \/|  |  \_  __ \  |/  ___/\   __\  \__  \  /    \      |    \__  \ |  |/     \_/ __ \ /  ___/
	\     \___|   Y  \  | \/  |\___ \  |  | |  |/ __ \|   |  \ /\__|    |/ __ \|  |  Y Y  \  ___/ \___ \ 
	 \______  /___|  /__|  |__/____  > |__| |__(____  /___|  / \________(____  /__|__|_|  /\___  >____  >
	        \/     \/              \/               \/     \/                \/         \/     \/     \/ 	
	''')
	
	while True:
		command = str(input('''

		¿Que desea hacer?
		[1] Cifrar un achivo
		[2] Desfifraar un archivo
		[3] Comparar dos Archivos
		[4] Salir
		
		'''
		))
		if command == '1':
			cifrar()
		elif command == '2':
			descifrar()
		elif command =='3':
			comparar()
		elif command == '4':
			break
		else:
			print("Comando no encontrado, intente nuevamente \n")
		
