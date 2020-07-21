""" Screen model widget for all the screens except startscreen."""

#Layputs
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

#Graphics
from kivy.graphics import *

#components
from app.widgets.components.header import headerWidget



class ScreenModelWidget(BoxLayout):
    """ Screen Model that content all the boxlayouts
    to give a model for all the screens."""

    def __init__(self, *args, **kwargs):
        super(ScreenModelWidget, self).__init__(*args, **kwargs)
        self.orientation = 'vertical' 
        self.work_box = BoxLayout(
            size_hint=[1, .8],
            orientation='vertical'     
        )
        self.work_box.add_widget(Label(text='Ricardo'))
        self.header = headerWidget()
        # self.header.add_widget(Label(text='Header'))
        self.add_widget(self.header)
        self.add_widget(self.work_box)