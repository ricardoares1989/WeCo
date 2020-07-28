"""Widget for toggle buttons."""

#widgets
from kivy.uix.togglebutton import ToggleButton

# Properties
from kivy.properties import StringProperty, ObjectProperty

#Config
from app.config.settings import query_products, config, blue_weco


class ProductButton(ToggleButton):

    def __init__(self, id_product, *args, **kwargs):
        super(ProductButton, self).__init__(*args, **kwargs)
        self.background_color = blue_weco
        self.border = (0,5,0,5)
        self.id_product = id_product
        