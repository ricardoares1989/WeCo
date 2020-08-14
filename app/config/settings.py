

import os
from dotenv import load_dotenv
load_dotenv()

USER = os.getenv("USER")
PASSWORD_DB = os.getenv("PASSWORD_DB")
HOST = os.getenv("HOST")
DB_NAME = os.getenv("DB_NAME")
DB_PORT = os.getenv("DB_PORT")


#DATABASE SETTINGS
config = {
    'user': USER,
    'password': PASSWORD_DB,
    'host': HOST,
    'database': DB_NAME,
    'port': DB_PORT
}


TABLES = {}

TABLES['products'] = (
    """
    CREATE TABLE IF NOT EXISTS public.products
    (
    product_id serial,
    name character varying(50) NOT NULL,
    CONSTRAINT product_id PRIMARY KEY (product_id),
    CONSTRAINT name UNIQUE (name)
    );
    """
    )

TABLES['registers'] = (
    "CREATE TABLE IF NOT EXISTS registers ("
    "`register_id` BIGINT PRIMARY KEY NOT NULL AUTO_INCREMENT,"
    "`weigth` FLOAT(6,2) NOT NULL,"
    "`product_id` INTEGER NOT NULL,"
    "`created_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,"
    "`updated_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP"
    "   ON UPDATE CURRENT_TIMESTAMP,"
    "FOREIGN KEY (product_id) REFERENCES products(product_id)"
    ")")

add_product = ("INSERT INTO products "
                "(name)"
                "VALUES (%(name)s)"
    )
products = [
    {'name': 'naranja'}, 
    {'name': 'jitomate'}, 
    {'name': 'pepino'},
    {'name': 'arandano'},
    {'name': 'Saladette'},
    ]

query_products = (
                "SELECT product_id, name FROM `weco`.`products`"
                "ORDER BY name"
                ) 

blue_weco = [8/255, 61/255, 119/255, 0.6]
white_weco = [235/255, 235/255, 211/255, 1]
yellow_weco = [244/255, 211/255, 94/255, 1]
orange_weco = [249/255, 87/255, 56/255, 1]

query_register = (
    "INSERT INTO registers"
    "(weigth, product_id)" 
    "VALUES (%(weigth)s, %(product_id)s)"
)