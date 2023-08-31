print('='*50)
print(' ')
print(' Olá, Seja bem vindo ao DesCriptoMessage  \n Use o para Descriptografar suas mensagens')
print(' ')

def descripto(frase):
    tradutor = ""
    for letra in frase:
        if letra in "@": 
            tradutor = tradutor + 'A'
        elif letra in "#":
            tradutor = tradutor + 'B'
        elif letra in "$":
            tradutor = tradutor + 'C'
        elif letra in "%":
            tradutor = tradutor + 'D'
        elif letra in "2":
            tradutor = tradutor + 'E'
        elif letra in "&":
            tradutor = tradutor + 'F'
        elif letra in "*":
            tradutor = tradutor + 'G'
        elif letra in "(":
            tradutor = tradutor + 'H'
        elif letra in ")":
            tradutor = tradutor + 'I'
        elif letra in "+":
            tradutor = tradutor + 'J'
        elif letra in "=":
            tradutor = tradutor + 'K'
        elif letra in "4":
            tradutor = tradutor + 'L'
        elif letra in "6":
            tradutor = tradutor + 'M'
        elif letra in "9":
            tradutor = tradutor + 'N'
        elif letra in "8":
            tradutor = tradutor + 'O'
        elif letra in "{":
            tradutor = tradutor + 'P'
        elif letra in "|":
            tradutor = tradutor + 'Q'
        elif letra in "}":
            tradutor = tradutor + 'R'
        elif letra in ";":
            tradutor = tradutor + 'S'
        elif letra in "<":
            tradutor = tradutor + 'T'
        elif letra in ">":
            tradutor = tradutor + 'U'
        elif letra in "-":
            tradutor = tradutor + 'V'
        elif letra in "1":
            tradutor = tradutor + 'W'
        elif letra in "3":
            tradutor = tradutor + 'X'
        elif letra in "5":
            tradutor = tradutor + 'Y'
        elif letra in "7":
            tradutor = tradutor + 'Z'
        elif letra in "_":
            tradutor = tradutor + ' '
        else: 
            tradutor = tradutor + letra
    return tradutor

result = descripto(input(" Digite a frase Criptografada e a descubra: "))
print(' ')
print(' A frase era: ' +  result )
print(' ')
print('='*50)
print(input('Pressione Enter para sair...'))
