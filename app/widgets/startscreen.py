""" Start screen view."""

#config
from app.config import DatabaseManagement

from kivy.uix.boxlayout import BoxLayout


class StartScreenWid(BoxLayout):
    """ Start screen"""
    def __init__(self, **kwargs):
        super(StartScreenWid, self).__init__()

    def create_or_connect_to_database(self):
        db = DatabaseManagement()
        db.connect_to_database()