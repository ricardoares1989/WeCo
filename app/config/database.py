""" Settings to database conection."""

#Database
import os
import mysql.connector
from mysql.connector import errorcode

#Settings
from .settings import (config, 
        DB_NAME, 
        TABLES, 
        add_product,
        products)


def database_decorator(func):
    def wrapper(*args, **kwargs):
        try:
            func(*args, **kwargs)
            return func
        except mysql.connector.Error as err:
            print(err)
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            else:
                print(err)
                exit(1)
        return func
    return wrapper

class DatabaseManagement:
    """Class it has the methods to manage the database in mysql."""

    @database_decorator
    def create_database(self, cursor):
        """Create database if not exists."""
        cnx = mysql.connector.connect(**config)
        cursor = cnx.cursor()
        cursor.execute(
                f"CREATE DATABASE {DB_NAME} DEFAULT CHARACTER SET 'utf8'"
            )

    @database_decorator
    def use_database(self):
        """Function to focus in the database."""
        cnx = mysql.connector.connect(**config)
        cursor = cnx.cursor()
        cursor.execute(f"USE {DB_NAME};")
        cursor.close()
        return 

    @database_decorator
    def create_tables(self):
        """Create the neccesary tables products and registers.""" 
        cnx = mysql.connector.connect(**config)
        cursor = cnx.cursor()
        for table_name in TABLES:
            table_desciption = TABLES[table_name]
            print(f"Creating table{table_name}", end ='')
            cursor.execute(table_desciption)
        cursor.close()
        return 

    @database_decorator
    def proof_database(self):
        cnx = mysql.connector.connect(**config)
        cursor = cnx.cursor()
        return cursor
    
    @database_decorator
    def create_product(self):
        cnx = mysql.connector.connect(**config)
        cursor = cnx.cursor()
        for product in products:
            try:
                cursor.execute(add_product, product)
                cnx.commit()
            except mysql.connector.Error as err:
                if err.errno == 1062:
                    pass
        cursor.close()
        return 


    @staticmethod
    def db_executor():
        cnx = mysql.connector.connect(**config)
        cursor = cnx.cursor()
        return cursor
    


