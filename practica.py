
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
	#ingresa la clavepl
	inputKey = input("Ingrese la clave para cifrar: \n")
	clave = list(inputKey) #Crea un arreglo serapando cada caracter
	# todo crear doble confirmacion
	i = 0
	# Crear archivo  Criptograma
	with open("criptograma.txt","w",encoding="utf-8") as textFile:
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
				resultado = int(binarioA ^ binarioB)
				R = bin(resultado)
				validacion = int(resultado ^ binarioB)
				#print(binarioA," = ", validacion)
				i=i+1
				if(binarioA != validacion):
					print("omg")

				#imprimir en criptograma
				textFile.write(int(R,2).to_bytes(8,'big').decode())
	textFile.close


if __name__ == '__main__':
    
    a = ord('z')#String a ASCCI
    A = bin(a)#ASCCi a Binario
   # print(a," = ",A)
    aA = int(A,2).to_bytes(8,'big').decode()#binario a String
    print(aA)
    b = ord('f')#String a ASCCI
    B = bin(b)#ASCCi a Binario
    bB = int(B,2).to_bytes(8,'big').decode()#binario a String
    print(bB)
    r = a ^ b
    R = bin(r)
    rR = int(R,2).to_bytes(8,'big').decode()
    print(r)
    print(aA," ",bB," ",rR)
    cifrar()
