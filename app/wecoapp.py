"""Screen View"""

#Kivy
from kivy.app import App
from kivy.uix.label import Label


#Widgets
from app.widgets import StartScreenWidget

class weCo(App):
    """Class to implement the functionality of
    the weco App."""

    title = "Welcome to WeCo"
    def build(self):
        #nos regresara el widget principal que regresa el contenedor de todos los widgets.
        return StartScreenWidget()
