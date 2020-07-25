"Component for create a work box for the screen model widget"

import csv

#widgets
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.togglebutton import ToggleButton

#My sql
import mysql.connector

# clock
from kivy.clock import Clock

# Properties
from kivy.properties import StringProperty, ObjectProperty

#Config
from app.config.settings import query_products, config, blue_weco


class WorkBoxWidget(BoxLayout):

    weight_read = StringProperty(f"0 kg")
    color_text = ObjectProperty(blue_weco)
    
    def __init__(self, *args, **kwargs):
        super(WorkBoxWidget, self).__init__(*args, **kwargs)
        self.size_hint = [1 , .8]
        self.orientation = 'horizontal'
        cnx = mysql.connector.connect(**config)
        cursor = cnx.cursor()
        cursor.execute(query_products)
        products = cursor
        for name in products:
            name = str(name[0])
            self.ids.container_buttons.add_widget(
                ToggleButton(
                    background_color=blue_weco,
                    text=name,
                    border=(0,5,0,5),
                    group='products'
                    ))
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

