"Component for create a work box for the screen model widget"

import csv

#widgets
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

# clock
from kivy.clock import Clock

#Properties
from kivy.properties import StringProperty



class WorkBoxWidget(BoxLayout):

    weight_read = StringProperty(f"0 kg")
    
    def __init__(self, *args, **kwargs):
        super(WorkBoxWidget, self).__init__(*args, **kwargs)
        self.size_hint = [1 , .8]
        self.orientation = 'horizontal'
        for i in range(30):
            self.ids.container.add_widget(Button())
        self.weights = Clock.schedule_interval(self.last_weight,1)

    def last_weight(self, *args, **kwargs):
        file_path = './pesos.csv'
        rows = []
        with open(file_path, newline='') as csvfile:
            row_reader = csv.reader(csvfile, delimiter=',')
            for row in row_reader:
                rows.append(row)
            last_row = rows[-1]
            self.weight_read = last_row[0] + ' kg'

