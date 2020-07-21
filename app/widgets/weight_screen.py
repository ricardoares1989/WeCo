"""Screen view for weight the products."""

#kivy
from kivy.uix.boxlayout import BoxLayout

#widget models
from app.widgets.components.screenmodel import ScreenModelWidget

class WeightScreenWid(BoxLayout):
    def __init__(self, main_wid, **kwargs):
        super(WeightScreenWid, self).__init__()
        self.add_widget(ScreenModelWidget())



