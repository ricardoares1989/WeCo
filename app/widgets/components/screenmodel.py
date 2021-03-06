""" Screen model widget for all the screens except startscreen."""

#Layouts
from kivy.uix.boxlayout import BoxLayout

#components
from app.widgets.components.header import headerWidget
from app.widgets.components.workbox import WorkBoxWidget


class ScreenModelWidget(BoxLayout):
    """ Screen Model that content all the boxlayouts
    to give a model for all the screens."""

    def __init__(self, *args, **kwargs):
        super(ScreenModelWidget, self).__init__(*args, **kwargs)
        self.orientation = 'vertical' 
        self.work_box = WorkBoxWidget()
        self.header = headerWidget()
        self.add_widget(self.header)
        self.add_widget(self.work_box)