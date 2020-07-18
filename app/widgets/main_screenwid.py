
#kivy
from kivy.uix.screenmanager import ScreenManager, Screen

#Widgets
from .startscreen import StartScreenWid
from .weight_screen import WeightScreenWid

class MainScreenWidget(ScreenManager):
    """Class which contains the widget for initialize the app."""
    def __init__(self, **kwargs):
        super(MainScreenWidget, self).__init__()
        StartScreenWidget = StartScreenWid(self, orientation='vertical')
        WeightScreenWidget = WeightScreenWid(self)

        wid = Screen(name='start')
        wid.add_widget(StartScreenWidget)
        self.add_widget(wid)

        wid = Screen(name='weight')
        wid.add_widget(WeightScreenWidget)
        self.add_widget(wid)

        self.goto_start()


    def goto_start(self):
        self.current = 'start'

    def goto_weigth(self):
        self.current = 'weight'
