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

#classes
from .widgets.main_screenwid import MainScreenWidget

#Screen start config
Config.set("graphics", "width", "980")
Config.set("graphics", "height", "720")
Config.set("graphics", "minimum_width", "860")
Config.set("graphics", "minimum_height", "600")



class weCo(App):
    """Class to implement the functionality of
    the weco App."""

    title = "Welcome to WeCo"
    def build(self):
        #nos regresara el widget principal que regresa el contenedor de todos los widgets.
        return MainScreenWidget()
