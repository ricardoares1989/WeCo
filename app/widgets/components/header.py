"""header for all the screens except the startscreen"""

#widgets
from kivy.uix.boxlayout import BoxLayout

#Properties
from kivy.properties import OptionProperty, ListProperty






class headerWidget(BoxLayout):
    def __init__(self, *args, **kwargs):
        super(headerWidget, self).__init__(*args, **kwargs)
        self.orientation = OptionProperty('horizontal')
        self.size_hint = ListProperty([None, None])
