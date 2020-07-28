""" Table component that shows the last ten registers"""

#Layouts
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

#Graphics
from kivy.graphics import Color, Ellipse

#My sql
import mysql.connector

#Utils
from app.config import orange_weco, blue_weco, config

class HeadTableWidget(Button):

    def __init__(self, *args, **kwargs):
        super(HeadTableWidget, self).__init__(*args, **kwargs)
    
class CellTableWidget(Button):

    def __init__(self, *args, **kwargs):
        super(CellTableWidget, self).__init__(*args, **kwargs)
    
          
class TableRegisterWidget(GridLayout):
    """The widget table of registers."""
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()
    select_product = ("SELECT r.register_id, r.weigth, p.name, r.created_at "
                    "FROM registers as r "
                    "JOIN products as p "
                    "ON r.product_id = p.product_id "
                    "ORDER BY r.register_id DESC "
                    "LIMIT 10;")
    def __init__(self, *args, **kwargs):
        super(TableRegisterWidget, self).__init__(*args, **kwargs)
        self.cols = 4
        self.rows = 11
        self.headers = ['ID', 'Weight', 'Product', 'Date']
        for head in self.headers:
            if head == 'ID' or head == 'Weight':
                self.add_widget(HeadTableWidget(
                    size_hint_x=0.5,
                    text=head,
                    color=orange_weco,
                    size_hint_y=None,
                    height=50,
                ))
            else:
                self.add_widget(HeadTableWidget(
                    text=head,
                    color=orange_weco,
                    size_hint_y=None,
                    height=50,
                ))

        self.create_table()
    
    def create_table(self):
        try:
            self.cursor = self.cnx.cursor()
            self.cursor.execute(self.select_product)
            registers = self.cursor
            for reg_if, wei, p_name, date_created in registers:
                self.add_widget(CellTableWidget(
                    size_hint_x=0.5,
                    text=str(reg_if),
                    color=blue_weco,

                ))
                self.add_widget(CellTableWidget(
                    size_hint_x=0.5,
                    text=str(wei) + " kg",
                    color=blue_weco,

                ))
                self.add_widget(CellTableWidget(
                    text=p_name,
                    color=blue_weco,
                ))
                self.add_widget(CellTableWidget(
                    text=str(date_created),
                    color=blue_weco,
                ))
            self.cursor.close()

        except Exception as excep:
            print(excep)

            
    
    def update_table(self):
        try:
            self.cursor = self.cnx.cursor(buffered=True)
            self.cursor.execute(self.select_product)
            registers = self.cursor
            first_child = self.children
            while len(first_child) > 4:
                for i in first_child:
                    if type(i) == CellTableWidget:
                        self.remove_widget(i)

            for reg_if, wei, p_name, date_created in registers:
                self.add_widget(CellTableWidget(
                    size_hint_x=0.5,
                    text=str(reg_if),
                    color=blue_weco,
                ))
                self.add_widget(CellTableWidget(
                    size_hint_x=0.5,
                    text=str(wei) + " kg",
                    color=blue_weco,
                ))
                self.add_widget(CellTableWidget(
                    text=p_name,
                    color=blue_weco,
                ))
                self.add_widget(CellTableWidget(
                    text=str(date_created),
                    color=blue_weco,
                ))
                
            self.cnx.commit()
            self.cursor.close()

        except Exception as excep:
            print(excep)
