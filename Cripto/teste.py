from kivy.app import App
from kivy.lang import Builder
from kivy.uix.textinput import TextInput

import requests

GUI = Builder.load_file('tela.kv')

class MeuAplicativo(App):
    def build(self):
        textinput = TextInput(text='Hello world')
        return GUI
    
MeuAplicativo().run()