from PyQt5 import uic, QtWidgets
import clipboard as c

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
            tradutor = tradutor + '{'
        elif letra in "Qq":
            tradutor = tradutor + '|'
        elif letra in "Rr":
            tradutor = tradutor + '}'
        elif letra in "Ss":
            tradutor = tradutor + ';'
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

def showText():
    textLine = cripto(tela.lineEdit.text())
    tela.resultado.setText(textLine)
    tela.resultado_2.setText("")
    
    return textLine

def copyText():
    textCopied = showText()
    c.copy(textCopied)
    tela.resultado_2.setText("Copiado!")


app = QtWidgets.QApplication([])
tela = uic.loadUi("./tela01.ui")
tela.criptoButton.clicked.connect(showText)
tela.pasteButton.clicked.connect(copyText)

tela.show()
app.exec()