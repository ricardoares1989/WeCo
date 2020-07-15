"""Screen View"""

#Utils
import os


#Kivy config
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.app import App
from kivy.config import Config

#Kivy Widgets

from kivy.uix.label import Label
from kivy.uix.image import Image

#Widgets
from app.widgets.startscreen import StartScreenWid

#Screen start config
Config.set("graphics", "width", "980")
Config.set("graphics", "height", "720")

class MainScreenWidget(ScreenManager):
    """Class which contains the widget for initialize the app."""
    def __init__(self, **kwargs):
        super(MainScreenWidget, self).__init__()
        self.StartScreenWidget = StartScreenWid()
        wid = Screen(name='start')
        wid.add_widget(self.StartScreenWidget)
        self.add_widget(wid)



class weCo(App):
    """Class to implement the functionality of
    the weco App."""

    title = "Welcome to WeCo"
    def build(self):
        #nos regresara el widget principal que regresa el contenedor de todos los widgets.
        return MainScreenWidget()
