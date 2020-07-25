"""Screen View"""

#Utils
import os


#Kivy config
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.app import App
from kivy.config import Config
from kivy.lang import Builder

#Widgets
from app.widgets.startscreen import StartScreenWid

#classes
from .widgets.main_screenwid import MainScreenWidget

#Screen start config
Config.set("graphics", "width", "980")
Config.set("graphics", "height", "720")
Config.set("graphics", "minimum_width", "860")
Config.set("graphics", "minimum_height", "600")

Builder.load_file('app/workbox.kv')

class weCo(App):
    """Class to implement the functionality of
    the weco App."""

    title = "Welcome to WeCo"
    def build(self):
        return MainScreenWidget()
