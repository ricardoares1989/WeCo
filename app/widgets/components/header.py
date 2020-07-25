"""header for all the screens except the startscreen"""

#widgets
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image

#Dabase management
from app.config import DatabaseManagement

#Properties
from kivy.properties import OptionProperty, ListProperty


class headerWidget(BoxLayout):
    def __init__(self, *args, **kwargs):
        super(headerWidget, self).__init__(*args, **kwargs)
        self.db = DatabaseManagement()
        self.orientation = 'horizontal'
        self.size_hint = (1, 0.15)
        self.connection = BoxLayout(
            orientation='horizontal',
            size_hint=[0.2,1],
        )
        if self.db.proof_database():
            self.connection.add_widget(Image(
                source='media/500-512.png',
                size_hint=[None,1],
                width=60
                ))       
        self.add_widget(self.connection)
        self.logo = BoxLayout(
            orientation='horizontal',
            size_hint=[0.8,1],
        )
        self.logo.add_widget(Image(
            source='media/logo.png',
            allow_stretch='True',
            size_hint_x=.2,
            size_hint_y=None,
            height=110,
            pos=(0,80)
            ))
        self.add_widget(self.logo)
        self.add_widget(BoxLayout(
            orientation='horizontal',
            size_hint=[0.2,1],
        ))