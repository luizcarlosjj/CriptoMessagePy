#IMPORTES
import os
import segno

print('='*50)
print(' ')
print(' Olá, Seja bem vindo ao CriptoMessage  \n Use o para criptografar suas mensagens  ')
print(' ')

fn = 'src/arquivo.txt'

# EVENTOS

if os.path.exists(fn):
    with open(fn) as file:
        text = file.read()
else:
    text = None

if not text:
    with open(fn,'w') as file:
        def cripto(frase):
            tradutor = ""
            for letra in frase:
                if letra in "Aa": 
                    tradutor = tradutor + '@'
                elif letra in "Bb":
                    tradutor = tradutor + '#'
                elif letra in "Cc":
                    tradutor = tradutor + '$'
                elif letra in "Dd":
                    tradutor = tradutor + '%'
                elif letra in "Ee":
                    tradutor = tradutor + '2'
                elif letra in "Ff":
                    tradutor = tradutor + '&'
                elif letra in "Gg":
                    tradutor = tradutor + '*'
                elif letra in "Hh":
                    tradutor = tradutor + '('
                elif letra in "Ii":
                    tradutor = tradutor + ')'
                elif letra in "Jj":
                    tradutor = tradutor + '+'
                elif letra in "Kk":
                    tradutor = tradutor + '='
                elif letra in "Ll":
                    tradutor = tradutor + '4'
                elif letra in "Mm":
                    tradutor = tradutor + '6'
                elif letra in "Nn":
                    tradutor = tradutor + '9'
                elif letra in "Oo":
                    tradutor = tradutor + '8'
                elif letra in "Pp":
                    tradutor = tradutor + '!'
                elif letra in "Qq":
                    tradutor = tradutor + '?'
                elif letra in "Rr":
                    tradutor = tradutor + '^'
                elif letra in "Ss":
                    tradutor = tradutor + '~'
                elif letra in "Tt":
                    tradutor = tradutor + '<'
                elif letra in "Uu":
                    tradutor = tradutor + '>'
                elif letra in "Vv":
                    tradutor = tradutor + '-'
                elif letra in "Ww":
                    tradutor = tradutor + '1'
                elif letra in "Xx":
                    tradutor = tradutor + '3'
                elif letra in "Yy":
                    tradutor = tradutor + '5'
                elif letra in "Zz":
                    tradutor = tradutor + '7'
                elif letra in " ":
                    tradutor = tradutor + '_'
                else: 
                    tradutor = tradutor + letra
            return tradutor
        #result = cripto(input(" Digite a frase a ser Criptografada: "))
        fraseNormal = input('Digite a frase a ser Criptografada: ')
        fraseMod = cripto(fraseNormal)
        file.write(fraseMod)
        print(' ')
        print(' A frase se tornou: ' +  fraseMod )
        print(' ')
        print('='*50)
        print(input('Pressione Enter para sair...'))
        
else:
    with open(fn, 'w') as file:
        def cripto(frase):
            tradutor = ""
            for letra in frase:
                if letra in "Aa": 
                    tradutor = tradutor + '@'
                elif letra in "Bb":
                    tradutor = tradutor + '#'
                elif letra in "Cc":
                    tradutor = tradutor + '$'
                elif letra in "Dd":
                    tradutor = tradutor + '%'
                elif letra in "Ee":
                    tradutor = tradutor + '2'
                elif letra in "Ff":
                    tradutor = tradutor + '&'
                elif letra in "Gg":
                    tradutor = tradutor + '*'
                elif letra in "Hh":
                    tradutor = tradutor + '('
                elif letra in "Ii":
                    tradutor = tradutor + ')'
                elif letra in "Jj":
                    tradutor = tradutor + '+'
                elif letra in "Kk":
                    tradutor = tradutor + '='
                elif letra in "Ll":
                    tradutor = tradutor + '4'
                elif letra in "Mm":
                    tradutor = tradutor + '6'
                elif letra in "Nn":
                    tradutor = tradutor + '9'
                elif letra in "Oo":
                    tradutor = tradutor + '8'
                elif letra in "Pp":
                    tradutor = tradutor + '!'
                elif letra in "Qq":
                    tradutor = tradutor + '?'
                elif letra in "Rr":
                    tradutor = tradutor + '^'
                elif letra in "Ss":
                    tradutor = tradutor + '~'
                elif letra in "Tt":
                    tradutor = tradutor + '<'
                elif letra in "Uu":
                    tradutor = tradutor + '>'
                elif letra in "Vv":
                    tradutor = tradutor + '-'
                elif letra in "Ww":
                    tradutor = tradutor + '1'
                elif letra in "Xx":
                    tradutor = tradutor + '3'
                elif letra in "Yy":
                    tradutor = tradutor + '5'
                elif letra in "Zz":
                    tradutor = tradutor + '7'
                elif letra in " ":
                    tradutor = tradutor + '_'
                else: 
                    tradutor = tradutor + letra
            return tradutor
        fraseNormal = input('Digite a frase a ser Criptografada: ')
        fraseMod = cripto(fraseNormal)
        file.write(fraseMod)
        print(' ')
        print(' A frase se tornou: ' +  fraseMod )
        print(' ')
        print('='*50)
        print(input('Pressione Enter para sair...'))

        
with open(fn, 'r') as file:
    Qrcode = file.read()
    qrcode_seq = segno.make_sequence(Qrcode, version=1)
    qrcode_seq.save('Qrcode/{}.png' .format(fraseNormal), scale=10)