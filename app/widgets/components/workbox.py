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
from app.config.settings import query_products, query_register, config, blue_weco

#Components
from app.widgets.components.products_buttons import ProductButton
from app.widgets.components.table_registers import TableRegisterWidget

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
        for pk, name in products:
            self.ids.container_buttons.add_widget(
                ProductButton(
                    text=name,
                    group='products',
                    id_product=pk
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

    def product_selected(self, *args, **kwargs):
        product_id = ''
        for pb in self.ids.container_buttons.children:
            if pb.state =='down':
                product_id = pb.id_product
        weight = float(self.ids.weights.text[:-3])

        
        try:
            if product_id:
                data_register = {
                    "weigth": weight,
                    "product_id": product_id
                    }
                cnx = mysql.connector.connect(**config)
                cursor = cnx.cursor()
                cursor.execute(query_register, data_register)
                cnx.commit()
                cursor.close()
                cnx.close()
            else:
                pass
        except Exception as ex:
            print(ex)

