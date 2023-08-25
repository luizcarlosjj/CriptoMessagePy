import segno
import os

arq = "./arquivo.txt"

with open(arq, "r") as arquivo:
	texto = arquivo.read()
	
    
qrcode_seq = segno.make_sequence(texto, version=1)
qrcode_seq.save('Qrcode/qr2.png', scale=10)