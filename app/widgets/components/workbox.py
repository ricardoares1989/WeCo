"Component for create a work box for the screen model widget"

#widgets
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label


class WorkBoxWidget(BoxLayout):
    def __init__(self, *args, **kwargs):
        super(WorkBoxWidget, self).__init__(*args, **kwargs)


