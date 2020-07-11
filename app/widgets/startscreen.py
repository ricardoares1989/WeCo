""" Start screen view."""


from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager

class StartScreenWidget(ScreenManager):
    """Class which contains the widget for initialize the app."""
    def __init__(self, **kwargs):
        super(StartScreenWidget, self).__init__(**kwargs)
