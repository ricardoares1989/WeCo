""" Start screen view."""

#config
from app.config import DatabaseManagement

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.button import Button


class StartScreenWid(BoxLayout):
    """ Start screen"""
    def __init__(self, main_wid, **kwargs):
        super(StartScreenWid, self).__init__()
        db = DatabaseManagement()
        db_connection = BoxLayout(
            orientation='vertical',
            size_hint_x=None,
            width=200,
        )
        img = BoxLayout(
            size_hint_y=0.2,
        )
        img.add_widget(Image(
            source='media/500-512.png',
            size_hint=[None,None],
            width=100,
            height=100
            ))
        if db.proof_database():
            db_connection.add_widget(img)
        db_connection.add_widget(BoxLayout(
            size_hint_y=.8
        ))
        self.add_widget(db_connection)
        logo = BoxLayout(orientation='vertical')
        icono = BoxLayout(
            orientation='vertical',
            size_hint_y=0.6
        )
        icono.add_widget(Image(source='media/logo.png',size_hint=[1,None],size=[400,400]))
            
        logo.add_widget(BoxLayout(size_hint_y=.2))
        logo.add_widget(icono)
        logo.add_widget(Button(
            size_hint_y=.2,
            height=300,
            background_color=[0,0,0,0],
            text="Empezar a pesar",
            font_size='30sp',
            color=[.03,.23,.46,1],
            on_press=self.create_or_connect_to_database()
            ))
        logo.add_widget(BoxLayout(size_hint_y=.2))
        self.add_widget(logo)
        self.add_widget(BoxLayout(
            orientation='vertical',
            size_hint_x=None,
            width=200,
        ))


        

    def create_or_connect_to_database(self):
        db = DatabaseManagement()
        db.connect_to_database()
       
